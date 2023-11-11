import io
from typing import Any, Dict

import yaml

from obsidian_helper import models


class IndentedDumper(yaml.Dumper):
    """
    A Dumper that will indent lists by two spaces.
    """

    def increase_indent(self, flow=False, indentless=False):
        return super(IndentedDumper, self).increase_indent(flow, False)

def write_obsidian_file(obsidian_file:models.ObsidianFile):
    """
    Writes an ObsidianFile object to a markdown file.
    """
    with open(obsidian_file.file_path, "w") as file:
        if obsidian_file.metadata:
            write_metadata(file, obsidian_file.metadata)

        for section in obsidian_file.sections:
            file.write(turn_section_to_string(section))

def write_metadata(file: io.StringIO, metadata: Dict[str, Any]) -> None:
    file.write("---\n")
    yaml.dump(metadata, file, Dumper=IndentedDumper)
    file.write("---\n")

def turn_section_to_string(section: models.MarkdownSection) -> str:
    section_string = ""
    if section.title:
        section_string += ("#" * section.depth + " " + section.title + "\n")
    if not section.lines:
        return section_string

    for line in section.lines:
        section_string += line + "\n"

    return section_string


