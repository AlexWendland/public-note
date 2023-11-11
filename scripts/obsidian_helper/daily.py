import logging

from obsidian_helper import file_admin, index_admin, openai_note_check, read_obsidian, write_obsidian

logger = logging.getLogger(__name__)


def main():

    file_admin.run_last_updated_check(switch_checked_field=True)

    for file_path in read_obsidian.get_obsidian_files(templates=False):
        logger.info(f"{file_path} INFO: Updating...")
        obsidian_file = read_obsidian.read_obsidian_file(str(file_path))
        file_admin.update_tags(obsidian_file)
        if not obsidian_file.metadata.get("checked", False):
            openai_note_check.update_article(obsidian_file)
        logger.info(f"{file_path} INFO: Updated.")
        write_obsidian.write_obsidian_file(obsidian_file)

    index_admin.update_indices()

    # Needs to be at the end as the script might edit files!
    file_admin.run_last_updated_check(switch_checked_field=False)

    print("\n------------------------\n")
    print("Finished updating Obsidian files but you will still need to check the differences in the git logs.")
    print("\n------------------------\n")

