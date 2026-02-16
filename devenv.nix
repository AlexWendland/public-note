{ pkgs, lib, config, inputs, ... }:

{
  languages.python = {
    enable = true;
    uv = {
      enable = true;
      sync = {
        enable = true;
        allExtras = true;
      };
    };
    venv.enable = true;
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
    pkgs.graphviz
    # Dependencies for node-canvas (required by excalidraw_export)
    pkgs.pkg-config
    pkgs.cairo
    pkgs.pango
    pkgs.pixman
    pkgs.giflib
    pkgs.libjpeg
  ];

  scripts.lecture.exec = "uv run scripts/lecture.py";
  scripts.definition.exec = "uv run scripts/definition.py";
  scripts.admin.exec = "uv run scripts/admin.py";
  scripts.undraft.exec = "uv run scripts/undraft.py";

  scripts.up.exec = ''
    hugo server
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
    mkdir -p static
    mkdir -p static/images
    mkdir -p static/images/excalidraw

    echo "Exporting Excalidraw diagrams to SVG..."

    # Export all .excalidraw files to .svg using excalidraw_export
    npx excalidraw_export excalidraw/*.excalidraw

    # Move generated SVG files to static/images/excalidraw/
    mv excalidraw/*.svg static/images/excalidraw/

    echo ""
    echo "✓ Exported diagram(s) to static/images/excalidraw/"
  '';

  scripts.graphviz-compile.exec = ''
    #!/bin/bash
    set -e

    # Create output directory if it doesn't exist
    mkdir -p static
    mkdir -p static/images
    mkdir -p static/images/graphviz

    echo "Exporting Graphviz diagrams to SVG..."

    # Check if there are any .gv files to process
    if ls graphviz/*.gv 1> /dev/null 2>&1; then
      # Export all .gv files to .svg using dot
      for file in graphviz/*.gv; do
        filename=$(basename "$file")
        echo "  Processing $filename..."
        dot -Tsvg "$file" -o "static/images/graphviz/$filename.svg"
      done

      echo ""
      echo "✓ Exported diagram(s) to static/images/graphviz/"
    else
      echo "No .gv files found in graphviz/ directory"
    fi
  '';

  scripts.check.exec = ''
    echo "Running all git hook checks..."
    pre-commit run --all-files
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
