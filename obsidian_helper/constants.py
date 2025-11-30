from pathlib import Path

# Get repo root (parent of obsidian_helper) and join with notes directory
OBSIDIAN_DIR = str(Path(__file__).resolve().parent.parent / "notes")
CHECKED_FIELD = "checked"
LAST_EDITED_FIELD = "last_edited"
INDEX_FILES = ["Git Index", "Maths Index", "Programming Index", "Python Index"]
ALIAS_FIELD = "aliases"
