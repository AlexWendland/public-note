import datetime
import logging
from pathlib import Path

from git import Repo

from note_helper import constants, file_admin, models, read_note, write_note

logger = logging.getLogger(__name__)


def update_last_edited(note_file: models.NoteFile):
    """
    Updates the last edited timestamp of a NoteFile object.
    """
    last_edited = get_last_edited(note_file.file_path)
    if not last_edited:
        last_edited = datetime.date.fromtimestamp(Path(note_file.file_path).stat().st_mtime)
        logger.info(
            f"{note_file.file_path} INFO: No commit history found for file using local last edited date {last_edited}."
        )
    if constants.LAST_EDITED_FIELD not in note_file.metadata:
        logger.info(f"{note_file.file_path} CHANGE: Adding last edited timestamp {last_edited}.")
    elif note_file.metadata[constants.LAST_EDITED_FIELD] < last_edited:
        logger.info(
            f"{note_file.file_path} CHANGE: Updating last edited timestamp from "
            f"{note_file.metadata[constants.LAST_EDITED_FIELD]} to {last_edited}."
        )
    note_file.metadata[constants.LAST_EDITED_FIELD] = last_edited


def get_last_edited(file_path, repo_path=constants.NOTES_DIR) -> datetime.date | None:
    repo = Repo(repo_path)

    try:
        commit_log = repo.iter_commits(paths=file_path)
        last_commit = next(commit_log)
        commit_date = datetime.date.fromtimestamp(last_commit.committed_date)
        return commit_date
    except StopIteration:
        # No commit history for the file
        return None


def update_tags(note_file: models.NoteFile):
    old_tags_raw = note_file.metadata.get("tags", None)
    # Normalize old_tags to a list for comparison
    if isinstance(old_tags_raw, str):
        old_tags = [old_tags_raw]
        new_tags = [old_tags_raw]
    elif isinstance(old_tags_raw, list):
        old_tags = old_tags_raw
        new_tags = []
        for current_tag in old_tags_raw:
            current_tag = str(current_tag).strip()
            if "," in current_tag:
                new_tags.extend(
                    [tag.strip() for tag in current_tag.split(",") if tag.strip() != "list[str]" and len(tag) > 0]
                )
            elif current_tag != "list[str]":
                new_tags.append(current_tag)
    else:
        old_tags = []
        new_tags = []
    log_difference_in_tags(note_file, new_tags, old_tags)
    note_file.metadata["tags"] = new_tags


def log_difference_in_tags(note_file: models.NoteFile, new_tags: list[str], old_tags: list[str]):
    """
    Logs the difference between the tags in the file and the new tags.
    """
    if isinstance(old_tags, str):
        logger.info(f"{note_file.file_path} CHANGE: Converting tags ({old_tags}) field from string to list.")
        return
    elif not isinstance(old_tags, list):
        logger.info(f"{note_file.file_path} CHANGE: Adding tags field to metadata.")
        return

    tags_not_in_file = [tag for tag in new_tags if tag not in old_tags]
    if tags_not_in_file:
        logger.info(f"{note_file.file_path} INFO: Tags added to file: {tags_not_in_file}")

    removed_tags = [tag for tag in old_tags if tag not in new_tags]
    if removed_tags:
        logger.info(f"{note_file.file_path} INFO: Tags removed from file: {removed_tags}")


def run_last_updated_check():
    """
    Updates the last edited timestamp of all note files.
    """

    logger.info("Running last updated check on all files.")

    for file in read_note.get_note_files(templates=False):
        note_file = read_note.read_note_file(str(file))
        file_admin.update_last_edited(note_file)
        write_note.write_note_file(note_file)
