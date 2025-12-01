import logging

from note_helper import file_admin, index_admin, read_note, write_note

logger = logging.getLogger(__name__)


def main():
    for file_path in read_note.get_note_files(templates=False):
        logger.info(f"{file_path} INFO: Updating...")
        note_file = read_note.read_note_file(str(file_path))
        file_admin.update_tags(note_file)
        # if not note_file.metadata.get("checked", False):
        #     openai_note_check.update_article(note_file)
        logger.info(f"{file_path} INFO: Updated.")
        write_note.write_note_file(note_file)

    index_admin.update_indices()

    # Needs to be at the end as the script might edit files!
    file_admin.run_last_updated_check()

    print("\n------------------------\n")
    print("Finished updating note files but you will still need to check the differences in the git logs.")
    print("\n------------------------\n")
