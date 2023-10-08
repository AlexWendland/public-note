import os
from typing import Any, Dict, List, Optional

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


def get_metadata_line_end(file_lines: List[str]) -> Optional[int]:
    if file_lines[0].strip() != "---":
        return None
    return file_lines.index("---\n", 1)


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
        file_lines = file.readlines()

    metadata_line_end = get_metadata_line_end(file_lines)

    if metadata_line_end is None:
        metadata = {}
        sections = [MarkdownSection(content="".join(file_lines))]
    else:
        metadata_lines = file_lines[1:metadata_line_end]
        metadata = read_metadata_from_obsidian_file(metadata_lines)
        sections = [
            MarkdownSection(content="".join(file_lines[metadata_line_end + 1 :]))
        ]

    return ObsidianFile(file_name=file_name, metadata=metadata, sections=sections

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
