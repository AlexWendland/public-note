from obsidian_helper import file_admin, index_admin, read_obsidian, write_obsidian


def main():

    for file_path in read_obsidian.get_obsidian_files(templates=False):
        obsidian_file = read_obsidian.read_obsidian_file(str(file_path))
        file_admin.update_tags(obsidian_file)
        write_obsidian.write_obsidian_file(obsidian_file)

    index_admin.update_indices()

    # Needs to be at the end as the script might edit files!
    file_admin.run_last_updated_check()

    print("\n------------------------\n")
    print("Finished updating Obsidian files but you will still need to check the differences in the git logs.")
    print("\n------------------------\n")

