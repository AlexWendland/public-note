import re
import sys
from datetime import date, datetime
from pathlib import Path

import questionary
from rich.console import Console
from rich.table import Table

from note_helper.models import MarkdownSection, NoteFile
from note_helper.read_note import read_note_file

console = Console()


class CourseInfo:
    """Information about an OMSCS course."""

    def __init__(self, code: str, name: str, directory: Path, index_file: Path, last_edited: date | None):
        self.code = code
        self.name = name
        self.directory = directory
        self.index_file = index_file
        self.last_edited = last_edited

    @property
    def display_name(self) -> str:
        """Return formatted display name for selection."""
        return f"{self.code} - {self.name}"

    @property
    def file(self) -> str:
        """Return path to course file."""
        return f"{self.code} {self.name}.md"

    def __repr__(self) -> str:
        return f"CourseInfo({self.code}, {self.name})"


def discover_courses(repo_root: Path) -> list[CourseInfo]:
    """Discover all OMSCS courses in the content directory."""
    omscs_dir = repo_root / "content" / "OMSCS"
    if not omscs_dir.exists():
        console.print("[red]Error: OMSCS directory not found![/red]")
        sys.exit(1)

    courses = []

    # Find all course directories (CS6210, CS6215, etc.)
    for course_dir in sorted(omscs_dir.glob("CS*")):
        if not course_dir.is_dir():
            continue

        # Look for _index.md in the course directory
        index_file = course_dir / "_index.md"
        if not index_file.exists():
            console.print(f"[yellow]Warning: No _index.md found in {course_dir}[/yellow]")
            continue

        # Read the _index.md file to get course metadata
        try:
            note = read_note_file(str(index_file))
            code = note.metadata.get("course_code")
            name = note.metadata.get("course_name")

            if not code or not name:
                console.print(f"[yellow]Warning: Missing course_code or course_name in {index_file}[/yellow]")
                continue

            # Get last_edited from the index file metadata
            last_edited = note.metadata.get("last_edited")
            # Convert string date to date object if needed
            if isinstance(last_edited, str):
                try:
                    last_edited = datetime.strptime(last_edited, "%Y-%m-%d").date()
                except (ValueError, TypeError):
                    last_edited = None

            courses.append(CourseInfo(code, name, course_dir, index_file, last_edited))
        except Exception as e:
            console.print(f"[red]Error reading {index_file}: {e}[/red]")
            continue

    # Sort by last edited date (most recent first), then by code
    courses.sort(key=lambda c: (c.last_edited is None, c.last_edited or date.min, c.code), reverse=True)

    return courses


def get_next_week_number(course: CourseInfo) -> int:
    """Auto-detect the next week number based on existing files in the course directory."""
    week_numbers = []

    # Find all lecture files matching "week_X_-_*.md"
    for file in course.directory.glob("week_*.md"):
        match = re.match(r"week_(\d+)", file.name)
        if match:
            week_numbers.append(int(match.group(1)))

    # Return the next week number, or 1 if no weeks exist
    return max(week_numbers, default=0) + 1


def create_lecture_file(name: str, week: str, course: CourseInfo) -> Path:
    """Create a new lecture file from the template."""
    # Create file path with lowercase and underscores (no spaces)
    # Convert name to slug: lowercase, replace spaces with underscores
    name_slug = name.lower().replace(" ", "_").replace("/", "_")
    file_name = f"week_{week}_-_{name_slug}.md"
    file_path = course.directory / file_name

    # Check if file already exists
    if file_path.exists():
        console.print(f"[red]Error: File already exists: {file_path}[/red]")
        sys.exit(1)

    # Create metadata from template
    today_str = datetime.now().strftime("%Y-%m-%d")
    title = f"Week {week} - {name}"
    metadata = {
        "aliases": None,
        "checked": False,
        "course_code": course.code,
        "course_name": course.name,
        "created": today_str,
        "last_edited": today_str,
        "draft": True,
        "tags": ["OMSCS"],
        "title": title,  # Add title to frontmatter
        "type": "lecture",
        "week": int(week),
    }

    # Create empty sections (no H1 heading in content)
    sections: list[MarkdownSection] = []

    note_file = NoteFile(file_path=str(file_path), metadata=metadata, sections=sections)

    # Write the file
    note_file.write()
    console.print(f"[green]✓ Created lecture file: {file_path}[/green]")

    return file_path


def display_courses_table(courses: list[CourseInfo]) -> None:
    """Display a formatted table of available courses."""
    table = Table(title="Available OMSCS Courses", show_header=True, header_style="bold magenta")
    table.add_column("Code", style="cyan", width=8)
    table.add_column("Name", style="white")
    table.add_column("Last Edited", style="yellow", width=12)

    for course in courses:
        last_edited_str = course.last_edited.strftime("%Y-%m-%d") if course.last_edited else "Never"
        table.add_row(course.code, course.name, last_edited_str)

    console.print(table)


def main():
    """Main entry point for the lecture CLI tool."""
    console.print("\n[bold blue]═══ Create New OMSCS Lecture ═══[/bold blue]\n")

    # Get repo root (parent of scripts directory)
    repo_root = Path(__file__).parent.parent

    # Discover all courses
    console.print("[cyan]Discovering courses...[/cyan]")
    courses = discover_courses(repo_root)

    if not courses:
        console.print("[red]Error: No OMSCS courses found![/red]")
        sys.exit(1)

    # Display courses table
    display_courses_table(courses)
    console.print()

    # Interactive course selection
    course_choices = [course.display_name for course in courses]
    selected_display_name = questionary.select(
        "Select a course:",
        choices=course_choices,
        style=questionary.Style([("selected", "fg:cyan bold"), ("pointer", "fg:cyan bold")]),
    ).ask()

    if not selected_display_name:
        console.print("[yellow]Selection cancelled.[/yellow]")
        sys.exit(0)

    # Find the selected course
    selected_course = next(c for c in courses if c.display_name == selected_display_name)

    # Auto-detect next week number
    suggested_week = get_next_week_number(selected_course)

    console.print(f"\n[cyan]Course selected:[/cyan] [bold]{selected_course.display_name}[/bold]")
    console.print(f"[cyan]Suggested next week:[/cyan] [bold]{suggested_week}[/bold]\n")

    # Prompt for week number with suggestion
    week_input = questionary.text(
        "Week number:",
        default=str(suggested_week),
        validate=lambda text: text.isdigit() or "Please enter a valid number",
    ).ask()

    if not week_input:
        console.print("[yellow]Input cancelled.[/yellow]")
        sys.exit(0)

    week = week_input.strip()

    # Prompt for lecture name
    name = questionary.text(
        "Lecture name:",
        validate=lambda text: len(text.strip()) > 0 or "Lecture name cannot be empty",
    ).ask()

    if not name:
        console.print("[yellow]Input cancelled.[/yellow]")
        sys.exit(0)

    name = name.strip()

    # Create the lecture file
    console.print()
    create_lecture_file(name, week, selected_course)

    console.print("\n[bold green]✓ Lecture created successfully![/bold green]\n")


if __name__ == "__main__":
    main()
