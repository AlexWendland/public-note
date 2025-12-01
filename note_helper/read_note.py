from collections.abc import Generator
from pathlib import Path
from typing import Any, TextIO

import pydantic
import yaml

from note_helper.constants import NOTES_DIR
from note_helper.models import MarkdownSection, NoteFile


def read_metadata_from_note_file(metadata_lines: list[str]) -> dict[str, Any]:
    """
    Reads YAML metadata from a note file.

    Parameters:
    - file_name (str): Path to the markdown file.

    Returns:
    - dict: A dictionary containing the parsed YAML metadata.
            Returns an empty dictionary if no metadata is found.
    """
    yaml_str = "".join(metadata_lines)
    result = yaml.safe_load(yaml_str)

    return result if isinstance(result, dict) else {}


def read_note_file(file_path: str) -> NoteFile:
    """
    Reads a markdown file and returns a NoteFile object.

    Parameters:
    - file_name (str): Path to the markdown file.

    Returns:
    - NoteFile: A NoteFile object containing the file's metadata and sections.
    """
    with Path(file_path).open(errors="ignore") as file:
        first_line_raw = next(file, None)
        if first_line_raw is None:
            return NoteFile(file_path=file_path, metadata={}, sections=[])
        first_line = first_line_raw.strip()

        metadata = {}
        first_line_for_sections: str | None = first_line
        if first_line == "---":
            metadata = extract_metadata(file)
            first_line_for_sections = next(file, None)

        sections = extract_all_sections(first_line_for_sections, file)

        return NoteFile(file_path=file_path, metadata=metadata, sections=sections)


def extract_metadata(file: TextIO) -> dict[str, Any]:
    """
    Extracts YAML metadata from a markdown file.
    """
    metadata = ""
    while True:
        line = next(file, None)
        if line is None:
            raise ValueError("No end to metadata found.")
        if line.strip() == "---":
            break
        metadata += line
    result = yaml.safe_load(metadata)
    return result if isinstance(result, dict) else {}


def extract_all_sections(first_line: str | None, file: TextIO) -> list[MarkdownSection]:
    sections = []

    while True:
        first_line, next_section = extract_section(first_line, file)
        sections.append(next_section)
        if first_line is None:
            break

    return sections


def extract_section(first_line: str | None, file: TextIO) -> tuple[str | None, MarkdownSection]:
    """
    Extracts a section from a markdown file.
    """
    if first_line is None:
        raise ValueError("No section found.")

    title, depth = parse_section_title(first_line)

    lines = []

    if title is None:
        lines.append(first_line.rstrip())

    while True:
        line = next(file, None)
        if line is None or is_title(line):
            break
        lines.append(line.rstrip())

    return line, MarkdownSection(title=title, depth=depth, lines=lines)


def parse_section_title(
    line: str,
) -> tuple[str | None, pydantic.PositiveInt | None]:
    """
    Parses a section title.
    """
    if not is_title(line):
        return None, None
    depth = 0
    for char in line:
        if char == "#":
            depth += 1
        else:
            break
    title = line[depth:].strip()
    return title, depth


def is_title(line: str) -> bool:
    """
    Checks if a line is a section title.
    """
    if len(line) < 2:
        return False
    if line[0] != "#":
        return False
    return line[1] in ["#", " "]


EXCLUDED_DIRECTORIES = [
    "Excalidraw",
    "scripts",
    ".obsidian",
]


def get_note_files(templates: bool = True) -> Generator[str]:
    """
    Gets all note files in the repository. It skips over some common files you will want to ignore.

    Parameters:
        templates (bool,optional): Whether to include templates in the search. Defaults to True.

    Yields:
        Generator[str, None, None]: The files in the repository.
    """
    directory = Path(NOTES_DIR)

    excluded_directories = EXCLUDED_DIRECTORIES.copy()
    if not templates:
        excluded_directories.append("templates")

    for file in directory.rglob("*.md"):
        if any(excluded in file.parts for excluded in excluded_directories):
            continue
        yield str(file)
