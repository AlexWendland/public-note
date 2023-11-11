from obsidian_helper import file_admin, read_obsidian, write_obsidian

for file in read_obsidian.get_obsidian_files():
    obsidian_file = read_obsidian.read_obsidian_file(str(file))
    file_admin.update_last_edited(obsidian_file)
    write_obsidian.write_obsidian_file(obsidian_file)
