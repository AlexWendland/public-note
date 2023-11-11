import io
from pathlib import Path
from typing import Any, Dict, Generator, List, Optional, Tuple

import pydantic
import yaml

from obsidian_helper.constants import OBSIDIAN_DIR
from obsidian_helper.models import MarkdownSection, ObsidianFile


def read_metadata_from_obsidian_file(metadata_lines: List[str]) -> Dict[str, Any]:
    """
    Reads YAML metadata from an obsidian file.

    Parameters:
    - file_name (str): Path to the markdown file.

    Returns:
    - dict: A dictionary containing the parsed YAML metadata.
            Returns an empty dictionary if no metadata is found.
    """
    yaml_str = "".join(metadata_lines)
    metadata = yaml.safe_load(yaml_str)

    return metadata


def read_obsidian_file(file_name: str) -> ObsidianFile:
    """
    Reads a markdown file and returns an ObsidianFile object.

    Parameters:
    - file_name (str): Path to the markdown file.

    Returns:
    - ObsidianFile: An ObsidianFile object containing the file's metadata and sections.
    """
    with open(file_name, "r", errors="ignore") as file:
        first_line = next(file, None).strip()
        if first_line is None:
            return ObsidianFile(file_name=file_name, metadata={}, sections=[])

        metadata = {}
        if first_line == "---":
            metadata = extract_metadata(file)
            first_line = next(file, None)

        sections = []

        while True:
            first_line, next_section = extract_section(first_line, file)
            sections.append(next_section)
            if first_line is None:
                break

        return ObsidianFile(file_name=file_name, metadata=metadata, sections=sections)


def extract_metadata(file: io.StringIO) -> Dict[str, Any]:
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
    return yaml.safe_load(metadata)


def extract_section(first_line: str, file: io.StringIO) -> Tuple[str, MarkdownSection]:
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
) -> Tuple[Optional[str], Optional[pydantic.PositiveInt]]:
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
    if line[1] not in ["#", " "]:
        return False
    return True

EXCLUDED_DIRECTORIES = [
    'Excalidraw',
    'scripts',
    '.obsidian',
]

def get_obsidian_files(templates: bool = True) -> Generator[str, None, None]:
    """
    Gets all obsidian files in the vault. It skips over some common files you will want to ignore.

    Parameters:
        templates (bool,optional): Whether to include templates in the search. Defaults to True.

    Yields:
        Generator[str, None, None]: The files in the vault.
    """
    directory = Path(OBSIDIAN_DIR)

    excluded_directories = EXCLUDED_DIRECTORIES.copy()
    if not templates:
        excluded_directories.append("templates")

    for file in directory.rglob("*.md"):
        if any(excluded in file.parts for excluded in excluded_directories):
            continue
        yield str(file)
