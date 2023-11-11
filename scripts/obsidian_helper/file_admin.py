import datetime
import logging
import os

from obsidian_helper import constants, file_admin, models, read_obsidian, write_obsidian

logger = logging.getLogger(__name__)

def update_last_edited(obsidian_file: models.ObsidianFile):
    """
    Updates the last edited timestamp of an ObsidianFile object.
    """
    last_edited = datetime.date.fromtimestamp(os.path.getmtime(obsidian_file.file_path))
    if constants.LAST_EDITED_FIELD not in obsidian_file.metadata:
        logger.info(f"{obsidian_file.file_path} CHANGE: Adding last edited timestamp {last_edited}.")
    elif obsidian_file.metadata[constants.LAST_EDITED_FIELD] < last_edited:
        logger.info(f"{obsidian_file.file_path} CHANGE: Updating last edited timestamp from {obsidian_file.metadata[constants.LAST_EDITED_FIELD]} to {last_edited}.")
    obsidian_file.metadata[constants.LAST_EDITED_FIELD] = last_edited

def run_last_updated_check():
    """
    Updates the last edited timestamp of all Obsidian files.
    """

    logger.info("Running last updated check on all files.")

    for file in read_obsidian.get_obsidian_files(templates=False):
        obsidian_file = read_obsidian.read_obsidian_file(str(file))
        file_admin.update_last_edited(obsidian_file)
        write_obsidian.write_obsidian_file(obsidian_file)

def regular_check():
    run_last_updated_check()
