{ pkgs, lib, config, inputs, ... }:

{
  languages.python = {
    enable = true;
    uv = {
      enable = true;
    };
  };

  languages.javascript = {
    enable = true;
    npm = {
      enable = true;
      install = {
        enable = true;
      };
    };
  };

  packages = [
    pkgs.ruff
    pkgs.git-lfs
    pkgs.docker
    pkgs.hugo
    # Dependencies for node-canvas (required by excalidraw_export)
    pkgs.pkg-config
    pkgs.cairo
    pkgs.pango
    pkgs.pixman
    pkgs.giflib
    pkgs.libjpeg
  ];

  scripts.lecture.exec = "uv run scripts/lecture.py";
  scripts.admin.exec = "uv run scripts/admin.py";

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
    mkdir -p static/images/excalidraw

    # Count files to export
    excalidraw_files=(excalidraw/*.excalidraw)
    if [ ! -e "''${excalidraw_files[0]}" ]; then
      echo "No .excalidraw files found in excalidraw/ directory"
      exit 0
    fi

    echo "Exporting Excalidraw diagrams to SVG..."

    # Export all .excalidraw files to .svg using excalidraw_export
    npx excalidraw_export excalidraw/*.excalidraw

    # Move generated SVG files to static/images/excalidraw/
    count=0
    for svg in excalidraw/*.svg; do
      if [ -f "$svg" ]; then
        basename=$(basename "$svg")
        mv "$svg" "static/images/excalidraw/$basename"
        echo "  • ''${basename%.svg}.excalidraw → static/images/excalidraw/$basename"
        ((count++))
      fi
    done

    echo ""
    echo "✓ Exported $count diagram(s) to static/images/excalidraw/"
  '';

  # Run admin tasks when entering the devenv shell
  enterShell = ''
    # Only run admin if we're in an interactive shell (not in a script/CI)
    if [[ $- == *i* ]]; then
      admin
    fi
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
    pytest = {
      enable = true;
      name = "pytest";
      entry = "uv run pytest";
      files = "\\.py$";
      language = "system";
      pass_filenames = false;
    };
  };
}
