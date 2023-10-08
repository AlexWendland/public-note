import os
from typing import Any, Dict, List, Optional, Tuple
import io

import pydantic
import yaml


class MarkdownSection(pydantic.BaseModel):
    title: Optional[str]
    depth: Optional[pydantic.PositiveInt]
    content: str

    @pydantic.root_validator(pre=True)
    @classmethod
    def check_title_and_depth(cls, values):
        if (values.get("title") is None and values.get("depth") is not None) or (
            values.get("title") is not None and values.get("depth") is None
        ):
            raise ValueError("Must must provide a title and depth or neither.")


class ObsidianFile(pydantic.BaseModel):
    file_name: str
    metadata: Dict[str, Any]
    sections: List[MarkdownSection]

    @pydantic.root_validator(pre=True)
    @classmethod
    def check_sections(cls, values):
        if len(values.get("sections")) > 0:
            for section in values.get("sections")[1:]:
                if section.title is None:
                    raise ValueError(
                        "All sections after the first section must have a title."
                    )


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
    with open(file_name, "r") as file:
        first_line = next(file, None).strip()
        if first_line is None:
            return ObsidianFile(file_name=file_name, metadata={}, sections=[])

        if first_line == "---":
            metadata = extract_metadata(file)

        sections = []

        while True:
            next_first_line, next_section = extract_section(first_line, file)
            sections.append(next_section)
            if next_first_line is None:
                break

        return ObsidianFile(file_name=file_name, metadata=metadata, sections=sections)


def extract_metadata(file: io.TextIO) -> Dict[str, Any]:
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


def extract_section(first_line: str, file: io.TextIO) -> MarkdownSection:
    """
    Extracts a section from a markdown file.
    """
    if first_line is None:
        raise ValueError("No section found.")

    title, depth = parse_section_title(first_line)

    content = ""

    if title is None:
        content += first_line

    while True:
        line = next(file, None)
        if line is None or is_title(line):
            break
        content += line

    return line, MarkdownSection(title=title, depth=depth, content=content)


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


if __name__ == "__main__":
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    metadata_test_file = os.path.join(
        current_file_directory, "example_with_metadata.md"
    )
    no_metadata_test_file = os.path.join(
        current_file_directory, "example_with_no_metadata.md"
    )
    print(read_metadata_from_obsidian_file(metadata_test_file))
    print(read_metadata_from_obsidian_file(no_metadata_test_file))
