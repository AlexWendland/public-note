import io
from pathlib import Path
from typing import Any

import yaml

from note_helper import models


class IndentedDumper(yaml.Dumper):
    """
    A Dumper that will indent lists by two spaces.
    """

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def write_note_file(note_file: models.NoteFile):
    """
    Writes a NoteFile object to a markdown file.
    """
    with Path(note_file.file_path).open("w") as file:
        if note_file.metadata:
            write_metadata(file, note_file.metadata)

        for section in note_file.sections:
            file.write(turn_section_to_string(section))


def write_metadata(file: io.TextIOWrapper, metadata: dict[str, Any]) -> None:
    file.write("---\n")
    yaml.dump(metadata, file, Dumper=IndentedDumper)
    file.write("---\n")


def turn_section_to_string(section: models.MarkdownSection) -> str:
    section_string = ""
    if section.title:
        depth = section.depth if section.depth else 0
        section_string += "#" * depth + " " + section.title + "\n"
    if not section.lines:
        return section_string

    for line in section.lines:
        section_string += line + "\n"

    return section_string
