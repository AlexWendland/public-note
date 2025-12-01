"""Admin script to maintain note repository metadata and indices."""

import logging

from rich.console import Console
from rich.progress import track

from note_helper import file_admin, index_admin, read_note, write_note

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

console = Console()


def main():
    """Run administrative tasks on the note repository."""
    console.print("\n[bold cyan]Running repository admin tasks...[/bold cyan]\n")

    # Update tags and metadata for all files
    files = list(read_note.get_note_files(templates=False))
    for file_path in track(files, description="[cyan]Updating note metadata..."):
        note_file = read_note.read_note_file(str(file_path))
        file_admin.update_tags(note_file)
        write_note.write_note_file(note_file)

    # Update indices
    console.print("[cyan]Updating indices...[/cyan]")
    index_admin.update_indices()

    # Update last_edited timestamps (needs to be at the end as it may edit files)
    console.print("[cyan]Updating last_edited timestamps from git...[/cyan]")
    file_admin.run_last_updated_check()

    console.print("\n[bold green]✓ Repository admin tasks completed![/bold green]")
    console.print("[yellow]Check git status to review any changes.[/yellow]\n")


if __name__ == "__main__":
    main()
