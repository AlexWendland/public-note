from pathlib import Path
from typing import Any

import pydantic


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


class ObsidianFile(pydantic.BaseModel):
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


class ObsidianLink(pydantic.BaseModel):
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
    def from_string(cls, text: str) -> "ObsidianLink":
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
