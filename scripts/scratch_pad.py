import obsidian_helper.file_admin as file_admin
import obsidian_helper.read_obsidian as read_obsidian
import obsidian_helper.write_obsidian as write_obsidian

for file in read_obsidian.get_obsidian_files():
    obsidian_file = read_obsidian.read_obsidian_file(str(file))
    file_admin.update_last_edited(obsidian_file)
    write_obsidian.write_obsidian_file(obsidian_file)
