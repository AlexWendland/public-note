"""End-to-end tests for note file writing behavior."""

import tempfile
from pathlib import Path

from note_helper.models import MarkdownSection, NoteFile
from note_helper.write_note import write_note_file


def test_frontmatter_is_alphabetically_sorted():
    """Test that frontmatter fields are written in alphabetical order."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        # Create metadata with fields in random order
        metadata = {
            "week": 5,
            "aliases": ["Test"],
            "type": "lecture",
            "checked": False,
            "course": "[[Test Course]]",
            "created": "2025-01-01",
            "last_edited": "2025-01-01",
            "draft": True,
            "tags": ["test"],
        }

        note = NoteFile(
            file_path=tmp_path,
            metadata=metadata,
            sections=[MarkdownSection(title="Test", depth=1, lines=[])],
        )

        write_note_file(note)

        # Read the file and check frontmatter order
        with Path(tmp_path).open() as f:
            content = f.read()

        # Extract frontmatter lines (between --- markers)
        lines = content.split("\n")
        assert lines[0] == "---"
        frontmatter_end = lines[1:].index("---") + 1
        frontmatter_lines = lines[1:frontmatter_end]

        # Get field names (lines with ':' that aren't list items)
        field_names = [
            line.split(":")[0].strip() for line in frontmatter_lines if ":" in line and not line.strip().startswith("-")
        ]

        # Verify alphabetical order
        assert field_names == sorted(field_names), f"Fields not alphabetical: {field_names}"

        # Verify specific expected order
        expected_order = ["aliases", "checked", "course", "created", "draft", "last_edited", "tags", "type", "week"]
        assert field_names == expected_order

    finally:
        Path(tmp_path).unlink(missing_ok=True)


def test_none_values_write_as_blank():
    """Test that None values in metadata write as blank instead of 'null'."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        metadata = {
            "aliases": None,  # Should write as 'aliases:' not 'aliases: null'
            "course": "[[Test]]",
            "tags": ["test"],
        }

        note = NoteFile(
            file_path=tmp_path,
            metadata=metadata,
            sections=[MarkdownSection(title="Test", depth=1, lines=[])],
        )

        write_note_file(note)

        # Read and verify
        with Path(tmp_path).open() as f:
            content = f.read()

        # Check that 'aliases: null' does not appear
        assert "aliases: null" not in content, "None should not write as 'null'"

        # Check that 'aliases:' appears with nothing after it
        lines = content.split("\n")
        aliases_line = next(line for line in lines if line.startswith("aliases:"))
        assert aliases_line == "aliases:", f"Expected 'aliases:', got '{aliases_line}'"

    finally:
        Path(tmp_path).unlink(missing_ok=True)


def test_multiline_metadata_values_preserved():
    """Test that complex metadata structures are preserved correctly."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        metadata = {
            "tags": ["tag1", "tag2", "tag3"],
            "aliases": ["Alias 1", "Alias 2"],
            "title": "Test",
        }

        note = NoteFile(
            file_path=tmp_path,
            metadata=metadata,
            sections=[MarkdownSection(title="Test", depth=1, lines=["Line 1", "Line 2"])],
        )

        write_note_file(note)

        # Read back and verify structure
        with Path(tmp_path).open() as f:
            content = f.read()

        # Verify tags are on separate lines with proper indentation
        assert "tags:\n  - tag1\n  - tag2\n  - tag3" in content or "tags:\n- tag1\n- tag2\n- tag3" in content

        # Verify content after frontmatter is preserved
        assert "# Test\nLine 1\nLine 2\n" in content

    finally:
        Path(tmp_path).unlink(missing_ok=True)
