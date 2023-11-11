from obsidian_helper import read_obsidian, write_obsidian

# index_admin.update_indices()

for file in read_obsidian.get_obsidian_files():
    obsidian_file = read_obsidian.read_obsidian_file(str(file))
    if obsidian_file.metadata.get("tags",None) is None:
        obsidian_file.metadata["tags"] = []
    write_obsidian.write_obsidian_file(obsidian_file)
