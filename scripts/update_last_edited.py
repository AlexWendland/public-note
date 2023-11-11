# import os

from obsidian_helper.read_obsidian import get_obsidian_files, read_obsidian_file
from obsidian_helper.write_obsidian import write_obsidian_file

for file in get_obsidian_files():
    # timestamp = os.path.getmtime(file)
    # reported_last_edited = read_obsidian_file(str(file)).metadata.get('last_edited', None)
    write_obsidian_file(read_obsidian_file(str(file)))

    # print(file, datetime.date.fromtimestamp(timestamp), reported_last_edited)
