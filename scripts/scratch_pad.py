import logging

from obsidian_helper import link_handling, read_obsidian, write_obsidian

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():

    for file_path in read_obsidian.get_obsidian_files(templates=False):
        obsidian_file = read_obsidian.read_obsidian_file(str(file_path))
        link_handling.clean_aliases_from_file(obsidian_file)
        # rehydration_map = link_handling.build_rehydration_map()
        # link_handling.rehydrate_file(obsidian_file, rehydration_map)
        write_obsidian.write_obsidian_file(obsidian_file):

    print("\n------------------------\n")
    print("Finished updating Obsidian files but you will still need to check the differences in the git logs.")
    print("\n------------------------\n")

main()
