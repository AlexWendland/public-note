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
    file_name: str
    metadata: Dict[str, Any]
    sections: List[MarkdownSection]

    @pydantic.model_validator(mode='before')
    @classmethod
    def check_title_and_depth(cls, values: Dict[str, Any]) -> Dict[str, Any]:
        title = values.get("title")
        depth = values.get("depth")

        if (title is None and depth is not None) or (title is not None and depth is None):
            raise ValueError("Must provide both a title and depth or neither.")

        return values
