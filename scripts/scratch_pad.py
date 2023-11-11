import logging

from obsidian_helper import file_admin, read_obsidian, write_obsidian

# index_admin.update_indices()
logging.basicConfig(level=logging.INFO)

for file in read_obsidian.get_obsidian_files():
    obsidian_file = read_obsidian.read_obsidian_file(str(file))
    file_admin.update_tags(obsidian_file)
    write_obsidian.write_obsidian_file(obsidian_file)
