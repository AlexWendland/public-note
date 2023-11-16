import logging
import os
from typing import Callable, List

import pydantic

from obsidian_helper import constants, models, read_obsidian, write_obsidian

GIT_INDEX_FILE = os.path.join(constants.OBSIDIAN_DIR, "Git Index.md")
MATHS_INDEX_FILE = os.path.join(constants.OBSIDIAN_DIR, "Maths Index.md")
PROGRAMMING_INDEX_FILE = os.path.join(constants.OBSIDIAN_DIR, "Programming Index.md")
PYTHON_INDEX_FILE = os.path.join(constants.OBSIDIAN_DIR, "Python Index.md")

logger = logging.getLogger(__name__)

class IndexFile(pydantic.BaseModel):
    obsidian_file: models.ObsidianFile
    is_in_index: Callable[List[str], bool]

    def update_index(self, notes: List[str]):
        """
        Adds a file to the index.
        """
        self.log_difference_between_index_and_notes(notes)
        lines = [""]
        for note in sorted(notes):
            lines.append(self.make_index_entry(note))
        self.get_index_section().lines = lines
        write_obsidian.write_obsidian_file(self.obsidian_file)

    def log_difference_between_index_and_notes(self, notes: List[str]):
        """
        Logs the difference between the index and the notes.
        """
        current_index_entries = self.get_current_index_entries()

        notes_not_in_index = [note for note in notes if note not in current_index_entries]
        if notes_not_in_index:
            logger.info(f"{self.obsidian_file.file_path} INFO: Notes not in index: {notes_not_in_index}")

        removed_notes = [note for note in current_index_entries if note not in notes]
        if removed_notes:
            logger.info(f"{self.obsidian_file.file_path} INFO: Notes removed from index: {removed_notes}")

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
        Returns the section of the obsidian file that contains the index.
        """
        for section in self.obsidian_file.sections:
            if section.title == "Index":
                return section
        index_section = models.MarkdownSection(title="Index", depth=1, lines=[])
        self.obsidian_file.sections.append(index_section)
        return index_section


INDEX_FILES = [
    IndexFile(
        obsidian_file= read_obsidian.read_obsidian_file(GIT_INDEX_FILE),
        is_in_index=lambda tags: "git" in tags,
    ),
    IndexFile(
        obsidian_file= read_obsidian.read_obsidian_file(MATHS_INDEX_FILE),
        is_in_index=lambda tags: "maths" in tags,
    ),
    IndexFile(
        obsidian_file= read_obsidian.read_obsidian_file(PROGRAMMING_INDEX_FILE),
        is_in_index=lambda tags: "programming" in tags and "python" not in tags and "git" not in tags,
    ),
    IndexFile(
        obsidian_file= read_obsidian.read_obsidian_file(PYTHON_INDEX_FILE),
        is_in_index=lambda tags: "python" in tags,
    ),
]

def update_indices():
    """
    Updates all the indices.
    """
    logger.info("Updating indices.")
    for index_file in INDEX_FILES:
        index_file.update_index(get_all_notes(index_file))

def get_all_notes(index_file: IndexFile):
    """
    Returns a list of all the notes in the vault.
    """
    notes = []
    for file in read_obsidian.get_obsidian_files(templates=False):
        obsidian_file = read_obsidian.read_obsidian_file(str(file))
        if index_file.is_in_index(obsidian_file.metadata.get("tags", [])):
            notes.append(obsidian_file.file_name)
    return notes
