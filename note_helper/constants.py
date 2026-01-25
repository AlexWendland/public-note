from pathlib import Path

# Get repo root (parent of note_helper)
REPO_ROOT = str(Path(__file__).resolve().parent.parent)
# Notes directory
NOTES_DIR = str(Path(REPO_ROOT) / "content")
CHECKED_FIELD = "checked"
DATE_CHECKED_FIELD = "date_checked"
LAST_EDITED_FIELD = "last_edited"
INDEX_FILES = ["Git Index", "Maths Index", "Programming Index", "Python Index"]
ALIAS_FIELD = "aliases"

# Required frontmatter fields (will be added if missing)
REQUIRED_FIELDS = {
    DATE_CHECKED_FIELD: None,  # Default value: None
}

# Banned/deprecated frontmatter fields (will be removed if present)
BANNED_FIELDS = [
    CHECKED_FIELD,  # Replaced by DATE_CHECKED_FIELD
]

# Allowed admonition types for the personal theme
ALLOWED_ADMONITIONS = {
    "note",
    "example",
    "important",
    "warning",
    "lemma",
    "definition",
    "quote",
    "question",
}
