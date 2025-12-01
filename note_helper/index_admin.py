import logging
from collections.abc import Callable
from pathlib import Path

import pydantic

from note_helper import constants, models, read_note, write_note

GIT_INDEX_FILE = str(Path(constants.NOTES_DIR) / "Git Index.md")
MATHS_INDEX_FILE = str(Path(constants.NOTES_DIR) / "Maths Index.md")
PROGRAMMING_INDEX_FILE = str(Path(constants.NOTES_DIR) / "Programming Index.md")
PYTHON_INDEX_FILE = str(Path(constants.NOTES_DIR) / "Python Index.md")

logger = logging.getLogger(__name__)


class IndexFile(pydantic.BaseModel):
    note_file: models.NoteFile
    is_in_index: Callable[[list[str]], bool]

    def update_index(self, notes: list[str]):
        """
        Adds a file to the index.
        """
        self.log_difference_between_index_and_notes(notes)
        lines = [""]
        for note in sorted(notes):
            lines.append(self.make_index_entry(note))
        self.get_index_section().lines = lines
        write_note.write_note_file(self.note_file)

    def log_difference_between_index_and_notes(self, notes: list[str]):
        """
        Logs the difference between the index and the notes.
        """
        current_index_entries = self.get_current_index_entries()

        notes_not_in_index = [note for note in notes if note not in current_index_entries]
        if notes_not_in_index:
            logger.info(f"{self.note_file.file_path} INFO: Notes not in index: {notes_not_in_index}")

        removed_notes = [note for note in current_index_entries if note not in notes]
        if removed_notes:
            logger.info(f"{self.note_file.file_path} INFO: Notes removed from index: {removed_notes}")

    def get_current_index_entries(self):
        """
        Returns a list of all the notes currently in the index.
        """
        index_section = self.get_index_section()
        return [self.get_index_entry(line) for line in index_section.lines if self.is_index_entry(line)]

    def make_index_entry(self, note: str):
        """
        Make an index entry for the note.
        """
        return f"- [[{note}]]"

    def is_index_entry(self, line: str):
        """
        Checks if a line is an index entry.
        """
        return line.startswith("- [[") and line.endswith("]]")

    def get_index_entry(self, line: str):
        """
        Returns the note name from an index entry.
        """
        return line[4:-2]

    def get_index_section(self):
        """
        Returns the section of the note file that contains the index.
        """
        for section in self.note_file.sections:
            if section.title == "Index":
                return section
        index_section = models.MarkdownSection(title="Index", depth=1, lines=[])
        self.note_file.sections.append(index_section)
        return index_section


def get_index_files() -> list[IndexFile]:
    """
    Lazy-load index files to avoid import-time failures if files don't exist.
    Returns only the index files that actually exist.
    """
    from pathlib import Path

    index_configs = [
        (GIT_INDEX_FILE, lambda tags: "git" in tags),
        (MATHS_INDEX_FILE, lambda tags: "maths" in tags),
        (PROGRAMMING_INDEX_FILE, lambda tags: "programming" in tags and "python" not in tags and "git" not in tags),
        (PYTHON_INDEX_FILE, lambda tags: "python" in tags),
    ]

    index_files = []
    for file_path, is_in_index_fn in index_configs:
        # Only load index if the file exists
        if Path(file_path).exists():
            try:
                index_files.append(
                    IndexFile(
                        note_file=read_note.read_note_file(file_path),
                        is_in_index=is_in_index_fn,
                    )
                )
            except Exception as e:
                logger.warning(f"Failed to load index file {file_path}: {e}")
        else:
            logger.debug(f"Skipping non-existent index file: {file_path}")

    return index_files


def update_indices():
    """
    Updates all the indices.
    """
    logger.info("Updating indices.")
    index_files = get_index_files()

    if not index_files:
        logger.info("No index files found to update.")
        return

    for index_file in index_files:
        index_file.update_index(get_all_notes(index_file))


def get_all_notes(index_file: IndexFile):
    """
    Returns a list of all the notes in the repository.
    """
    notes = []
    for file in read_note.get_note_files(templates=False):
        note_file = read_note.read_note_file(str(file))
        if index_file.is_in_index(note_file.metadata.get("tags", [])):
            notes.append(note_file.file_name)
    return notes
