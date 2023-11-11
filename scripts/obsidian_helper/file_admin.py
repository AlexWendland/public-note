import datetime
import os

from obsidian_helper.constants import LAST_EDITED_FIELD
from obsidian_helper.models import ObsidianFile


def update_last_edited(obsidian_file: ObsidianFile):
    """
    Updates the last edited timestamp of an ObsidianFile object.
    """
    last_edited = datetime.date.fromtimestamp(os.path.getmtime(obsidian_file.file_path))
    obsidian_file.metadata[LAST_EDITED_FIELD] = last_edited
