import io
from typing import Any, Dict

import yaml

from obsidian_helper.models import MarkdownSection, ObsidianFile


class IndentedDumper(yaml.Dumper):
    """
    A Dumper that will indent lists by two spaces.
    """

    def increase_indent(self, flow=False, indentless=False):
        return super(IndentedDumper, self).increase_indent(flow, False)

def write_obsidian_file(obsidian_file:ObsidianFile):
    """
    Writes an ObsidianFile object to a markdown file.
    """
    with open(obsidian_file.file_path, "w") as file:
        if obsidian_file.metadata:
            write_metadata(file, obsidian_file.metadata)

        for section in obsidian_file.sections:
            write_section(file, section)

def write_metadata(file: io.StringIO, metadata: Dict[str, Any]) -> None:
    file.write("---\n")
    yaml.dump(metadata, file, Dumper=IndentedDumper)
    file.write("---\n")

def write_section(file: io.StringIO, section: MarkdownSection) -> None:
    if section.title:
        file.write("#" * section.depth + " " + section.title + "\n")
    if section.lines:
        for line in section.lines:
            file.write(line + "\n")
