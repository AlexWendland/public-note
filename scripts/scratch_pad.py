# import logging

# from obsidian_helper import daily

# # index_admin.update_indices()
# logging.basicConfig(level=logging.INFO)

# daily.main()

import os

from git import Repo

from obsidian_helper import constants


def get_last_commit_date(file_path, repo_path=constants.OBSIDIAN_DIR):
    repo = Repo(repo_path)

    try:
        # Get the commit history for the file
        commit_log = repo.log('--follow', '--', file_path)

        # Get the latest commit that modified the file
        last_commit = next(commit_log)

        # Get the commit date
        commit_date = last_commit.committed_date
        return commit_date
    except StopIteration:
        # No commit history for the file
        return None

if __name__ == "__main__":
    file_path = r'D:\obsidian\public-note\general\Wrap 3rd party libraries.md'

    if os.path.exists(file_path):
        last_commit_date = get_last_commit_date(file_path)

        if last_commit_date is not None:
            print(f"The file was last edited on: {last_commit_date}")
        else:
            print("No commit history for the file.")
    else:
        print(f"File not found: {file_path}")
