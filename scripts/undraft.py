#!/usr/bin/env python3
"""Interactive tool to undraft notes using Textual TUI."""

from datetime import date, datetime
from pathlib import Path
from typing import ClassVar, NamedTuple

from textual import on
from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widgets import DataTable, Footer, Header, Static

from note_helper.read_note import read_note_file


class DraftNote(NamedTuple):
    """Information about a draft note."""

    path: Path
    title: str
    last_edited: date | None
    relative_path: str


class NotePreview(Static):
    """Widget to display note preview."""

    def update_note(self, note: DraftNote | None) -> None:
        """Update the preview with a new note."""
        if note is None:
            self.update("[dim]No note selected[/dim]")
            return

        try:
            note_data = read_note_file(str(note.path))

            # Build preview content
            header = f"[bold cyan]{note.title}[/bold cyan]\n[dim]{note.relative_path}[/dim]\n"

            # Use the NoteFile's to_content method
            content = note_data.to_content()

            if content.strip():
                # Display markdown content
                self.update(header + "\n" + content)
            else:
                self.update(header + "\n[dim]No content[/dim]")

        except Exception as e:
            self.update(f"[red]Error reading note: {e}[/red]")


class UndraftApp(App):
    """Textual app for undrafting notes."""

    CSS = """
    Screen {
        layout: horizontal;
    }

    #notes-container {
        width: 60%;
        border-right: solid $primary;
    }

    #preview-container {
        width: 40%;
        padding: 1 2;
    }

    DataTable {
        height: 1fr;
    }

    #preview {
        height: 1fr;
    }

    .title {
        text-style: bold;
        background: $boost;
        padding: 1;
    }
    """

    BINDINGS: ClassVar[list[Binding | tuple[str, str] | tuple[str, str, str]]] = [
        Binding("q", "quit", "Quit"),
        Binding("u", "undraft_selected", "Undraft"),
        Binding("a", "select_all", "Select All"),
        Binding("n", "select_none", "Clear Selection"),
    ]

    def __init__(self):
        super().__init__()
        self.draft_notes: list[DraftNote] = []
        self.selected_rows: set[int] = set()

    def compose(self) -> ComposeResult:
        """Create child widgets."""
        yield Header()

        with Horizontal():
            with Vertical(id="notes-container"):
                yield Static("Draft Notes", classes="title")
                yield DataTable(cursor_type="row")

            with VerticalScroll(id="preview-container"):
                yield Static("Preview", classes="title")
                yield NotePreview(id="preview")

        yield Footer()

    def on_mount(self) -> None:
        """Set up the application on mount."""
        # Configure the data table
        table = self.query_one(DataTable)
        table.cursor_type = "row"
        table.zebra_stripes = True

        # Add columns
        table.add_column("Title", key="title")
        table.add_column("Last Edited", key="date")
        table.add_column("Path", key="path")

        # Load draft notes
        self.load_draft_notes()

        # Populate table
        self.refresh_table()

        # Focus the table
        table.focus()

    def load_draft_notes(self) -> None:
        """Find all notes marked as draft: true."""
        repo_root = Path(__file__).parent.parent
        notes_dir = repo_root / "notes"
        draft_notes = []

        for md_file in notes_dir.rglob("*.md"):
            # Skip _index.md files
            if md_file.name == "_index.md":
                continue

            try:
                note = read_note_file(str(md_file))
                if note.metadata.get("draft") is True:
                    last_edited = note.metadata.get("last_edited")

                    # Convert string dates to date objects if needed
                    if isinstance(last_edited, str):
                        try:
                            last_edited = datetime.strptime(last_edited, "%Y-%m-%d").date()
                        except (ValueError, TypeError):
                            last_edited = None

                    # Use title from metadata or filename
                    title = note.metadata.get("title", md_file.stem)

                    draft_notes.append(
                        DraftNote(
                            path=md_file,
                            title=title,
                            last_edited=last_edited,
                            relative_path=str(md_file.relative_to(repo_root)),
                        )
                    )
            except Exception:
                continue

        # Sort by last_edited (newest first)
        draft_notes.sort(
            key=lambda n: (n.last_edited is None, n.last_edited or date.max),
            reverse=True,
        )

        self.draft_notes = draft_notes
        self.title = f"Undraft Notes ({len(self.draft_notes)} drafts)"

    def refresh_table(self) -> None:
        """Refresh the data table with current notes."""
        table = self.query_one(DataTable)
        table.clear()

        for idx, note in enumerate(self.draft_notes):
            last_edited_str = str(note.last_edited) if note.last_edited else "No date"

            # Add checkmark if selected
            title_display = f"{'✓ ' if idx in self.selected_rows else '  '}{note.title}"

            table.add_row(
                title_display,
                last_edited_str,
                note.relative_path,
                key=str(idx),
            )

    @on(DataTable.RowHighlighted)
    def on_row_highlighted(self, event: DataTable.RowHighlighted) -> None:
        """Update preview when row is highlighted."""
        if event.row_key is not None and event.row_key.value is not None:
            idx = int(event.row_key.value)
            if 0 <= idx < len(self.draft_notes):
                preview = self.query_one("#preview", NotePreview)
                preview.update_note(self.draft_notes[idx])

    @on(DataTable.RowSelected)
    def on_row_selected(self, event: DataTable.RowSelected) -> None:
        """Toggle selection when row is clicked."""
        if event.row_key is not None and event.row_key.value is not None:
            idx = int(event.row_key.value)
            if idx in self.selected_rows:
                self.selected_rows.remove(idx)
            else:
                self.selected_rows.add(idx)

            # Preserve cursor position when refreshing
            table = self.query_one(DataTable)
            cursor_row = table.cursor_row
            self.refresh_table()

            # Restore cursor position if still valid
            if cursor_row < len(self.draft_notes):
                table.move_cursor(row=cursor_row)

    def action_select_all(self) -> None:
        """Select all notes."""
        self.selected_rows = set(range(len(self.draft_notes)))
        self.refresh_table()

    def action_select_none(self) -> None:
        """Clear all selections."""
        self.selected_rows.clear()
        self.refresh_table()

    def action_undraft_selected(self) -> None:
        """Undraft all selected notes."""
        if not self.selected_rows:
            self.notify("No notes selected", severity="warning")
            return

        # Get selected notes
        selected_notes = [self.draft_notes[idx] for idx in sorted(self.selected_rows, reverse=True)]

        # Undraft them
        success_count = 0
        for note in selected_notes:
            try:
                note_data = read_note_file(str(note.path))
                note_data.metadata["draft"] = False
                note_data.write()
                success_count += 1
            except Exception as e:
                self.notify(f"Error undrafting {note.title}: {e}", severity="error")

        # Remove undrafted notes from the list
        self.draft_notes = [note for idx, note in enumerate(self.draft_notes) if idx not in self.selected_rows]

        self.selected_rows.clear()
        self.title = f"Undraft Notes ({len(self.draft_notes)} drafts)"

        self.notify(f"Undrafted {success_count} note(s)", severity="information")

        if not self.draft_notes:
            self.notify("All notes undrafted!", severity="information")
            self.exit()
        else:
            self.refresh_table()


def main() -> None:
    """Main entry point."""
    app = UndraftApp()
    app.run()


if __name__ == "__main__":
    main()
