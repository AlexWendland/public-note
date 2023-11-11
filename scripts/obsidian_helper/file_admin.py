import datetime
import logging
import os
from typing import List

from obsidian_helper import constants, file_admin, models, read_obsidian, write_obsidian

logger = logging.getLogger(__name__)

def update_last_edited(obsidian_file: models.ObsidianFile, switch_checked_field: bool = True):
    """
    Updates the last edited timestamp of an ObsidianFile object.
    """
    last_edited = datetime.date.fromtimestamp(os.path.getmtime(obsidian_file.file_path))
    if constants.LAST_EDITED_FIELD not in obsidian_file.metadata:
        logger.info(f"{obsidian_file.file_path} CHANGE: Adding last edited timestamp {last_edited}.")
        if switch_checked_field:
            obsidian_file.metadata[constants.CHECKED_FIELD] = False
    elif obsidian_file.metadata[constants.LAST_EDITED_FIELD] < last_edited:
        logger.info(
            f"{obsidian_file.file_path} CHANGE: Updating last edited timestamp from "
            f"{obsidian_file.metadata[constants.LAST_EDITED_FIELD]} to {last_edited}."
        )
        if switch_checked_field:
            obsidian_file.metadata[constants.CHECKED_FIELD] = False
    obsidian_file.metadata[constants.LAST_EDITED_FIELD] = last_edited

def update_tags(obsidian_file: models.ObsidianFile):
    old_tags = obsidian_file.metadata.get("tags", None)
    if isinstance(old_tags, str):
        new_tags = [old_tags]
    elif not isinstance(old_tags, List):
        new_tags = []
    else:
        new_tags = []
        for current_tag in old_tags:
            current_tag = str(current_tag).strip()
            if "," in current_tag:
                new_tags.extend(
                    [tag.strip() for tag in current_tag.split(",") if tag.strip() != "list[str]" and len(tag) > 0]
                )
            elif current_tag != "list[str]":
                new_tags.append(current_tag)
    log_difference_in_tags(obsidian_file, new_tags, old_tags)
    obsidian_file.metadata["tags"] = new_tags

def log_difference_in_tags(obsidian_file: models.ObsidianFile, new_tags:List[str], old_tags:List[str]):
    """
    Logs the difference between the tags in the file and the new tags.
    """
    if isinstance(old_tags, str):
        logger.info(f"{obsidian_file.file_path} CHANGE: Converting tags ({old_tags}) field from string to list.")
        return
    elif not isinstance(old_tags, List):
        logger.info(f"{obsidian_file.file_path} CHANGE: Adding tags field to metadata.")
        return

    tags_not_in_file = [tag for tag in new_tags if tag not in old_tags]
    if tags_not_in_file:
        logger.info(f"{obsidian_file.file_path} INFO: Tags added to file: {tags_not_in_file}")

    removed_tags = [tag for tag in old_tags if tag not in new_tags]
    if removed_tags:
        logger.info(f"{obsidian_file.file_path} INFO: Tags removed from file: {removed_tags}")

def run_last_updated_check(switch_checked_field: bool = True):
    """
    Updates the last edited timestamp of all Obsidian files.
    """

    logger.info("Running last updated check on all files.")

    for file in read_obsidian.get_obsidian_files(templates=False):
        obsidian_file = read_obsidian.read_obsidian_file(str(file))
        file_admin.update_last_edited(obsidian_file, switch_checked_field)
        write_obsidian.write_obsidian_file(obsidian_file)

