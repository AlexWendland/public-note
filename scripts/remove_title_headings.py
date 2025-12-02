#!/usr/bin/env python3
"""
Remove duplicate title headings from markdown files and decrease heading levels.

If a note has a title in frontmatter and the first section heading matches it,
remove that section and decrease all other heading depths by 1.
"""

from pathlib import Path

from rich.console import Console
from rich.progress import track

from note_helper import read_note, write_note
from note_helper.constants import NOTES_DIR

console = Console()


def should_remove_title_section(note_file) -> bool:
    """Check if the first section should be removed (matches frontmatter title)."""
    if not note_file.sections:
        return False

    first_section = note_file.sections[0]

    # Check if first section has a title
    if not first_section.title:
        return False

    # Check if frontmatter has a title
    if "title" not in note_file.metadata:
        return False

    # Check if they match (case-insensitive, stripped)
    frontmatter_title = str(note_file.metadata["title"]).strip().lower()
    section_title = first_section.title.strip().lower()

    return frontmatter_title == section_title


def remove_title_and_decrease_depth(note_file):
    """Remove first section if it matches title, and decrease all heading depths by 1."""
    if not should_remove_title_section(note_file):
        console.print(f"[dim]  Skipping {note_file.file_path} (no matching title)[/dim]")
        return False

    console.print(f"[yellow]  Processing {note_file.file_path}[/yellow]")

    # Remove the first section
    note_file.sections = note_file.sections[1:]

    # Decrease depth of all remaining sections by 1
    for section in note_file.sections:
        if section.depth > 0:
            section.depth -= 1

    return True


def main():
    """Process all markdown files in the notes directory."""
    console.print("\n[bold cyan]Removing duplicate title headings...[/bold cyan]\n")

    # Get all markdown files
    notes_dir = Path(NOTES_DIR)
    all_files = list(notes_dir.rglob("*.md"))

    modified_count = 0
    skipped_count = 0

    for file_path in track(all_files, description="[cyan]Processing notes..."):
        try:
            # Read the note
            note = read_note.read_note_file(str(file_path))

            # Process it
            was_modified = remove_title_and_decrease_depth(note)

            if was_modified:
                # Write it back
                write_note.write_note_file(note)
                modified_count += 1
            else:
                skipped_count += 1

        except Exception as e:
            console.print(f"[red]✗ Error processing {file_path}: {e}[/red]")

    # Summary
    console.print(f"\n[bold green]✓ Complete![/bold green]")
    console.print(f"  Modified: {modified_count} files")
    console.print(f"  Skipped:  {skipped_count} files\n")


if __name__ == "__main__":
    main()
