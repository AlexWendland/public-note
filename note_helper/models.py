from pathlib import Path
from typing import Any

import pydantic
import yaml


class IndentedDumper(yaml.Dumper):
    """A Dumper that will indent lists by two spaces and represent None as empty."""

    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


# Represent None as empty string instead of 'null'
def represent_none(self, data):
    return self.represent_scalar("tag:yaml.org,2002:null", "")


IndentedDumper.add_representer(type(None), represent_none)


class MarkdownSection(pydantic.BaseModel):
    title: str | None = None
    depth: pydantic.PositiveInt | None = None
    lines: list[str] | None = None

    @pydantic.model_validator(mode="before")
    @classmethod
    def check_title_and_depth(cls, values: dict[str, Any]) -> dict[str, Any]:
        if (values.get("title") is None and values.get("depth") is not None) or (
            values.get("title") is not None and values.get("depth") is None
        ):
            raise ValueError("Must must provide a title and depth or neither.")
        return values

    def set_lines(self, lines: list[str]) -> None:
        self.lines = lines

    def to_string(self) -> str:
        """Convert section to markdown string."""
        section_string = ""
        if self.title:
            depth = self.depth if self.depth else 0
            section_string += "#" * depth + " " + self.title + "\n"
        if not self.lines:
            return section_string

        for line in self.lines:
            section_string += line + "\n"

        return section_string


class NoteFile(pydantic.BaseModel):
    file_path: str
    metadata: dict[str, Any]
    sections: list[MarkdownSection]

    @property
    def file_name(self) -> str:
        return Path(self.file_path).stem

    @pydantic.validator("file_path")
    @classmethod
    def filepath_be_a_markdown_file(cls, value: str):
        if not value.endswith(".md"):
            raise ValueError("file_path must be a markdown (.md) file.")
        return value

    def to_content(self) -> str:
        """Convert the NoteFile back to markdown content (without frontmatter)."""
        return "".join(section.to_string() for section in self.sections)

    def metadata_to_string(self) -> str:
        """Convert metadata to YAML frontmatter string."""
        if not self.metadata:
            return ""
        result = "---\n"
        result += yaml.dump(self.metadata, Dumper=IndentedDumper, sort_keys=True)
        result += "---\n"
        return result

    def to_string(self) -> str:
        """Convert the NoteFile to full markdown string with frontmatter."""
        return self.metadata_to_string() + self.to_content()

    def write(self, path: str | None = None) -> None:
        """Write note to file.

        Args:
            path: Optional path to write to. If not provided, uses self.file_path
        """
        target_path = path or self.file_path
        Path(target_path).write_text(self.to_string())


class NoteLink(pydantic.BaseModel):
    file_name: str
    section: str | None = None
    alias: str | None = None

    @property
    def link(self) -> str:
        text = self.file_name
        if self.section:
            text += f"#{self.section}"
        if self.alias:
            text += f" | {self.alias}"
        return f"[[{text}]]"

    def clean_representation(self) -> str:
        return self.alias if self.alias else self.file_name

    @classmethod
    def from_string(cls, text: str) -> "NoteLink":
        file_name = text
        section = None
        alias = None
        if "|" in file_name:
            file_name, alias = file_name.split("|")
        if "#" in file_name:
            file_name, section = file_name.split("#")
        return cls(
            file_name=file_name.strip(),
            section=section.strip() if section else None,
            alias=alias.strip() if alias else None,
        )

    def __hash__(self) -> int:
        return str.__hash__(str(self))
