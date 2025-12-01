from pathlib import Path

# Get repo root (parent of note_helper)
REPO_ROOT = str(Path(__file__).resolve().parent.parent)
# Notes directory
NOTES_DIR = str(Path(REPO_ROOT) / "notes")
CHECKED_FIELD = "checked"
LAST_EDITED_FIELD = "last_edited"
INDEX_FILES = ["Git Index", "Maths Index", "Programming Index", "Python Index"]
ALIAS_FIELD = "aliases"
