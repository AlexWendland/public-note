import logging

from note_helper import link_handling, read_note, write_note

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    for file_path in read_note.get_note_files(templates=False):
        note_file = read_note.read_note_file(str(file_path))
        link_handling.clean_aliases_from_file(note_file)
        # rehydration_map = link_handling.build_rehydration_map()
        # link_handling.rehydrate_file(note_file, rehydration_map)
        write_note.write_note_file(note_file)

    print("\n------------------------\n")
    print("Finished updating note files but you will still need to check the differences in the git logs.")
    print("\n------------------------\n")


main()
