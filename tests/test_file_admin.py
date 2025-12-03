"""End-to-end tests for file administration behavior."""

import datetime
import tempfile
from pathlib import Path
from unittest.mock import patch

from note_helper.file_admin import update_last_edited
from note_helper.models import MarkdownSection, NoteFile
from note_helper.read_note import read_note_file


def test_migration_date_skipped_in_last_edited():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        # Create a file with an old last_edited date
        old_date = "2023-11-11"
        metadata = {
            "title": "Test",
            "last_edited": old_date,
        }

        note = NoteFile(
            file_path=tmp_path,
            metadata=metadata,
            sections=[MarkdownSection(title="Test", depth=1, lines=[])],
        )
        note.write()

        # Mock get_last_edited to return the migration date
        migration_date = datetime.date(2025, 12, 1)
        with patch("note_helper.file_admin.get_last_edited") as mock_get_last_edited:
            mock_get_last_edited.return_value = migration_date

            # Read the file and try to update last_edited
            note = read_note_file(tmp_path)
            original_last_edited = note.metadata["last_edited"]

            update_last_edited(note)

            # Verify last_edited was NOT changed (migration date skipped)
            assert note.metadata["last_edited"] == original_last_edited
            assert note.metadata["last_edited"] == old_date

    finally:
        Path(tmp_path).unlink(missing_ok=True)


def test_non_migration_date_updates_last_edited():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        # Create a file with an old last_edited date
        old_date = "2023-11-11"
        metadata = {
            "title": "Test",
            "last_edited": old_date,
        }

        note = NoteFile(
            file_path=tmp_path,
            metadata=metadata,
            sections=[MarkdownSection(title="Test", depth=1, lines=[])],
        )
        note.write()

        # Mock get_last_edited to return a different date (not migration date)
        new_date = datetime.date(2025, 12, 4)
        with patch("note_helper.file_admin.get_last_edited") as mock_get_last_edited:
            mock_get_last_edited.return_value = new_date

            # Read the file and update last_edited
            note = read_note_file(tmp_path)
            update_last_edited(note)

            # Verify last_edited WAS changed (not migration date)
            assert note.metadata["last_edited"] == new_date

    finally:
        Path(tmp_path).unlink(missing_ok=True)


def test_last_edited_handles_string_dates():
    """Test that last_edited comparison works with string dates in metadata."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        # Create a file with string date (as stored in YAML)
        old_date_str = "2023-11-11"
        metadata = {
            "title": "Test",
            "last_edited": old_date_str,
        }

        note = NoteFile(
            file_path=tmp_path,
            metadata=metadata,
            sections=[MarkdownSection(title="Test", depth=1, lines=[])],
        )
        note.write()

        # Mock get_last_edited to return a newer date (after migration date to avoid skip)
        new_date = datetime.date(2025, 12, 15)
        with patch("note_helper.file_admin.get_last_edited") as mock_get_last_edited:
            mock_get_last_edited.return_value = new_date

            # Read the file (last_edited will be a string from YAML)
            note = read_note_file(tmp_path)
            assert isinstance(note.metadata["last_edited"], str)

            # Update - this should not crash despite string comparison
            update_last_edited(note)

            # Write back to file to persist the change
            note.write()

            # Re-read and verify it was updated
            note = read_note_file(tmp_path)
            # YAML may deserialize as date object or string - both are fine
            actual_date = note.metadata["last_edited"]
            if isinstance(actual_date, str):
                assert actual_date == str(new_date)
            else:
                assert actual_date == new_date

    finally:
        Path(tmp_path).unlink(missing_ok=True)


def test_last_edited_not_downgraded():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        # Create a file with a recent date
        recent_date = "2025-10-15"
        metadata = {
            "title": "Test",
            "last_edited": recent_date,
        }

        note = NoteFile(
            file_path=tmp_path,
            metadata=metadata,
            sections=[MarkdownSection(title="Test", depth=1, lines=[])],
        )
        note.write()

        # Mock get_last_edited to return an older date
        old_date = datetime.date(2025, 9, 1)
        with patch("note_helper.file_admin.get_last_edited") as mock_get_last_edited:
            mock_get_last_edited.return_value = old_date

            # Read and update
            note = read_note_file(tmp_path)
            update_last_edited(note)

            # Verify last_edited was NOT downgraded
            assert note.metadata["last_edited"] == recent_date

    finally:
        Path(tmp_path).unlink(missing_ok=True)
