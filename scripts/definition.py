import sys
from datetime import datetime
from pathlib import Path

import questionary
from rich.console import Console
from rich.table import Table

from note_helper.models import MarkdownSection, NoteFile
from note_helper.read_note import read_note_file

console = Console()


def find_existing_notes(notes_dir: Path, title: str) -> list[tuple[Path, str]]:
    """Search for existing notes with matching title or alias.

    Returns:
        List of (file_path, match_type) tuples where match_type is "title" or "alias"
    """
    matches = []
    title_lower = title.lower()

    for note_file in notes_dir.glob("*.md"):
        try:
            note = read_note_file(str(note_file))

            # Check title match
            note_title = note.metadata.get("title", "")
            if note_title and note_title.lower() == title_lower:
                matches.append((note_file, "title"))
                continue

            # Check aliases match
            aliases = note.metadata.get("aliases")
            if aliases and isinstance(aliases, list):
                for alias in aliases:
                    if alias and alias.lower() == title_lower:
                        matches.append((note_file, f"alias: {alias}"))
                        break
        except Exception as e:
            # Skip files that can't be read
            console.print(f"[yellow]Warning: Could not read {note_file}: {e}[/yellow]")
            continue

    return matches


def display_conflicts_table(conflicts: list[tuple[Path, str]]) -> None:
    """Display a table of conflicting notes."""
    table = Table(title="Existing Notes Found", show_header=True, header_style="bold red")
    table.add_column("File", style="cyan")
    table.add_column("Match Type", style="yellow")

    for file_path, match_type in conflicts:
        table.add_row(file_path.name, match_type)

    console.print(table)


def create_slug(title: str) -> str:
    """Convert title to filename slug (lowercase with underscores)."""
    # Replace spaces with underscores, convert to lowercase
    slug = title.lower().replace(" ", "_")
    # Remove or replace other problematic characters
    slug = slug.replace("/", "_").replace("\\", "_")
    # Remove any characters that aren't alphanumeric, underscore, or hyphen
    slug = "".join(c for c in slug if c.isalnum() or c in "_-")
    return slug


def create_definition_file(title: str, notes_dir: Path) -> Path:
    """Create a new definition file from the template."""
    # Create file path with lowercase and underscores (no spaces)
    file_name = f"{create_slug(title)}.md"
    file_path = notes_dir / file_name

    # Check if file already exists (shouldn't happen if we checked properly)
    if file_path.exists():
        console.print(f"[red]Error: File already exists: {file_path}[/red]")
        sys.exit(1)

    # Create metadata
    today_str = datetime.now().strftime("%Y-%m-%d")
    metadata = {
        "aliases": None,
        "checked": False,
        "created": today_str,
        "draft": True,
        "last_edited": today_str,
        "tags": None,
        "title": title,
        "type": "definition",
    }

    # Create empty sections (no content)
    sections: list[MarkdownSection] = []

    note_file = NoteFile(file_path=str(file_path), metadata=metadata, sections=sections)

    # Write the file
    note_file.write()
    console.print(f"[green]✓ Created definition file: {file_path}[/green]")

    return file_path


def main():
    """Main entry point for the definition CLI tool."""
    console.print("\n[bold blue]═══ Create New Definition Note ═══[/bold blue]\n")

    # Get repo root (parent of scripts directory)
    repo_root = Path(__file__).parent.parent
    notes_dir = repo_root / "content" / "notes"

    if not notes_dir.exists():
        console.print("[red]Error: notes directory not found![/red]")
        sys.exit(1)

    # Prompt for definition title
    title = questionary.text(
        "Definition title:",
        validate=lambda text: len(text.strip()) > 0 or "Title cannot be empty",
    ).ask()

    if not title:
        console.print("[yellow]Input cancelled.[/yellow]")
        sys.exit(0)

    title = title.strip()

    # Search for existing notes
    console.print("\n[cyan]Searching for existing notes...[/cyan]")
    conflicts = find_existing_notes(notes_dir, title)

    if conflicts:
        console.print()
        display_conflicts_table(conflicts)
        console.print(f"\n[yellow]Found {len(conflicts)} existing note(s) with matching title or alias.[/yellow]")

        # Ask user if they want to continue anyway
        should_continue = questionary.confirm(
            "Create note anyway?",
            default=False,
        ).ask()

        if not should_continue:
            console.print("[yellow]Cancelled.[/yellow]")
            sys.exit(0)
    else:
        console.print("[green]✓ No conflicts found.[/green]")

    # Create the definition file
    console.print()
    create_definition_file(title, notes_dir)

    console.print("\n[bold green]✓ Definition note created successfully![/bold green]\n")


if __name__ == "__main__":
    main()
