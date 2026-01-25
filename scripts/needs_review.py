#!/usr/bin/env python3
"""Find notes that need proofreading based on date_checked vs last_edited."""

import datetime
from pathlib import Path

import typer
from rich.console import Console
from rich.table import Table

from note_helper import constants, read_note

console = Console()
app = typer.Typer()


def find_notes_needing_review(limit=None):
    """
    Find notes where date_checked is None or < last_edited.

    Args:
        limit: Maximum number of notes to return (None for all)

    Returns:
        List of tuples: (file_path, last_edited_date)
    """
    needs_review = []

    for file_path in read_note.get_note_files(templates=False):
        note = read_note.read_note_file(file_path)

        date_checked = note.metadata.get(constants.DATE_CHECKED_FIELD)
        last_edited = note.metadata.get(constants.LAST_EDITED_FIELD)

        # Skip if no last_edited date (shouldn't happen, but be safe)
        if last_edited is None:
            continue

        # Convert string dates to date objects for comparison
        if isinstance(last_edited, str):
            last_edited = datetime.datetime.strptime(last_edited, "%Y-%m-%d").date()
        if isinstance(date_checked, str):
            date_checked = datetime.datetime.strptime(date_checked, "%Y-%m-%d").date()

        # Need review if never checked or checked before last edit
        if date_checked is None or date_checked < last_edited:
            needs_review.append((file_path, last_edited))

    # Sort by last_edited (most recent first)
    needs_review.sort(key=lambda x: x[1], reverse=True)

    # Apply limit if specified
    if limit is not None:
        needs_review = needs_review[:limit]

    return needs_review


@app.command()
def main(
    limit: int = typer.Option(
        10,
        "--limit",
        "-l",
        help="Maximum number of notes to show (use 0 for all)",
    ),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Show last_edited dates in table format",
    ),
):
    """Find notes that need proofreading based on date_checked vs last_edited."""
    limit_val = None if limit == 0 else limit

    notes = find_notes_needing_review(limit=limit_val)

    if not notes:
        console.print("\n[bold green]✓ All notes are up to date![/bold green]\n")
        return

    total_needing_review = len(list(find_notes_needing_review(limit=None)))

    console.print(f"\n[bold cyan]Found {total_needing_review} note(s) needing review[/bold cyan]")
    if limit_val and total_needing_review > limit:
        console.print(f"[dim]Showing most recent {limit}[/dim]\n")
    else:
        console.print()

    # Get repo root for relative paths
    repo_root = Path(constants.REPO_ROOT)

    if verbose:
        # Create a table
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Note Path", style="cyan")
        table.add_column("Last Edited", style="yellow")

        for file_path, last_edited in notes:
            rel_path = str(Path(file_path).relative_to(repo_root))
            table.add_row(rel_path, str(last_edited))

        console.print(table)
    else:
        # Simple list
        for file_path, _ in notes:
            rel_path = str(Path(file_path).relative_to(repo_root))
            console.print(f"  [cyan]{rel_path}[/cyan]")

    console.print("\n[bold]To review notes:[/bold]")
    console.print("  [green]claude code[/green]")
    console.print("  Then ask: [yellow]'Proofread <path>'[/yellow]\n")


if __name__ == "__main__":
    app()
