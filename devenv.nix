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
  ];

  scripts.lecture.exec = "uv run scripts/lecture.py";

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
