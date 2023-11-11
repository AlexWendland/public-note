import os
from typing import Any, Dict, List, Optional

import pydantic


class MarkdownSection(pydantic.BaseModel):
    title: Optional[str]
    depth: Optional[pydantic.PositiveInt]
    lines: Optional[List[str]]

    @pydantic.model_validator(mode='before')
    @classmethod
    def check_title_and_depth(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        if (values.get("title") is None and values.get("depth") is not None) or (
            values.get("title") is not None and values.get("depth") is None
        ):
            raise ValueError("Must must provide a title and depth or neither.")
        return values


class ObsidianFile(pydantic.BaseModel):
    file_path: str
    metadata: Dict[str, Any]
    sections: List[MarkdownSection]

    @property
    def file_name(self) -> str:
        return os.path.splitext(os.path.basename(self.file_path))[0]

    @pydantic.validator('file_path')
    def filepath_be_a_markdown_file(cls, value: str):
        if not value.endswith('.md'):
            raise ValueError('file_path must be a markdown (.md) file.')
        return value
