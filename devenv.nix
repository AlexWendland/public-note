{ pkgs, lib, config, inputs, ... }:

{
  languages.python = {
    enable = true;
    uv = {
      enable = true;
    };
  };

  packages = [
    pkgs.ruff
    pkgs.git-lfs
    pkgs.docker
  ];

  scripts.lecture.exec = "uv run scripts/lecture.py";

  scripts.excalidraw-setup.exec = ''
    #!/bin/bash
    set -e

    echo "Building excalidraw-brute-export-cli Docker image..."

    # Create temp directory
    TEMP_DIR=$(mktemp -d)
    echo "Cloning repository to $TEMP_DIR..."

    # Clone the repo
    git clone https://github.com/realazthat/excalidraw-brute-export-cli.git "$TEMP_DIR"

    # Build the Docker image
    cd "$TEMP_DIR"
    echo "Building Docker image (this may take a few minutes)..."
    docker build -t excalidraw-brute-export-cli:local .

    # Clean up
    cd -
    echo "Cleaning up temporary files..."
    rm -rf "$TEMP_DIR"

    echo ""
    echo "✓ Docker image 'excalidraw-brute-export-cli:local' built successfully!"
    echo "You can now use the 'excalidraw-compile' command."
  '';

  scripts.excalidraw.exec = ''
    echo "Starting Excalidraw on http://localhost:5173"
    echo "Save your .excalidraw files to the excalidraw/ directory"
    echo "Press Ctrl+C to stop"
    docker run --rm -p 5173:80 excalidraw/excalidraw:latest
  '';

  scripts.excalidraw-compile.exec = ''
    #!/bin/bash
    set -e

    # Create output directory if it doesn't exist
    mkdir -p images/excalidraw

    # Count files to export
    excalidraw_files=(excalidraw/*.excalidraw)
    if [ ! -e "''${excalidraw_files[0]}" ]; then
      echo "No .excalidraw files found in excalidraw/ directory"
      exit 0
    fi

    echo "Exporting Excalidraw diagrams to PNG..."
    count=0

    # Export all .excalidraw files to .png using Docker
    for file in excalidraw/*.excalidraw; do
      if [ -f "$file" ]; then
        basename=$(basename "$file" .excalidraw)
        echo "  • $basename.excalidraw → images/excalidraw/$basename.png"
        docker run --rm --tty \
          -u "$(id -u):$(id -g)" \
          -v "$(pwd):/data" \
          excalidraw-brute-export-cli:local \
          -i "/data/$file" \
          -o "/data/images/excalidraw/$basename.png" \
          --format png \
          --background 1 \
          --quiet
        ((count++))
      fi
    done

    echo ""
    echo "✓ Exported $count diagram(s) to images/excalidraw/"
  '';

  git-hooks.hooks = {
    ruff-check = {
      enable = true;
      name = "ruff check";
      entry = "ruff check --fix";
      files = "\\.py$";
      language = "system";
      pass_filenames = true;
    };
    ruff-format = {
      enable = true;
      name = "ruff format";
      entry = "ruff format";
      files = "\\.py$";
      language = "system";
      pass_filenames = true;
    };
    mypy = {
      enable = true;
      name = "mypy";
      entry = "uv run mypy";
      files = "\\.py$";
      language = "system";
      pass_filenames = true;
    };
  };
}
