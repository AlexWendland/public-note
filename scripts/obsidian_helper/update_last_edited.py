import datetime
import os
from pathlib import Path

from constants import OBSIDIAN_DIR
from read_obsidian import read_obsidian_file

directory = Path(OBSIDIAN_DIR)

for file in directory.rglob('*'):
    if file.is_file() and file.suffix == '.md':

        timestamp = os.path.getmtime(file)
        reported_last_edited = read_obsidian_file(str(file)).metadata.get('last_edited', None)

        print(file, datetime.date.fromtimestamp(timestamp), reported_last_edited)
