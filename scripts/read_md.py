import os
from dataclasses import dataclass
from typing import Any, Dict, List

import yaml


@dataclass
class ObsidianFile:
    metadata: Dict[str, Any]
    section_content: Dict[str, str]
    section_depth: Dict[str, int]
    section_order: List[str]


def read_metadata_from_obsidian_file(file_lines: List[str]) -> Dict[str, Any]:
    """
    Reads YAML metadata from an obsidian file.

    Parameters:
    - file_name (str): Path to the markdown file.

    Returns:
    - dict: A dictionary containing the parsed YAML metadata.
            Returns an empty dictionary if no metadata is found.
    """
    if file_lines[0].strip() != "---":
        return {}
    end_yaml = file_lines.index("---\n", 1)

    yaml_str = "".join(file_lines[1:end_yaml])
    metadata = yaml.safe_load(yaml_str)

    return metadata


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
