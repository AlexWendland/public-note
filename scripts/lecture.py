"""CLI tool to create a new OMSCS lecture note."""

import re
import sys
from datetime import date, datetime
from pathlib import Path

import questionary
from rich.console import Console
from rich.table import Table

from note_helper.file_admin import get_last_edited
from note_helper.models import MarkdownSection, NoteFile
from note_helper.read_note import read_note_file
from note_helper.write_note import write_note_file

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
    """Discover all OMSCS courses in the notes directory."""
    omscs_dir = repo_root / "notes" / "OMSCS"
    if not omscs_dir.exists():
        console.print("[red]Error: OMSCS directory not found![/red]")
        sys.exit(1)

    courses = []

    # Find all course index files (e.g., "CS6210 Advanced Operating Systems.md")
    for index_file in omscs_dir.glob("*.md"):
        # Extract course code and name from filename
        filename = index_file.stem  # Remove .md extension
        match = re.match(r"(CS\d{4})\s+(.+)", filename)
        if not match:
            continue

        code, name = match.groups()
        course_dir = omscs_dir / code

        # Skip if course directory doesn't exist
        if not course_dir.is_dir():
            continue

        # Get the most recent file edit in the course directory
        last_edited = None
        for file in course_dir.glob("*.md"):
            file_last_edited = get_last_edited(str(file), repo_path=str(repo_root))
            if file_last_edited and (not last_edited or file_last_edited > last_edited):
                last_edited = file_last_edited

        courses.append(CourseInfo(code, name, course_dir, index_file, last_edited))

    # Sort by last edited date (most recent first), then by code
    courses.sort(key=lambda c: (c.last_edited is None, c.last_edited or date.min, c.code), reverse=True)

    return courses


def get_next_week_number(course: CourseInfo) -> int:
    """Auto-detect the next week number based on existing files in the course directory."""
    week_numbers = []

    # Find all lecture files matching "Week X - *.md"
    for file in course.directory.glob("Week *.md"):
        match = re.match(r"Week (\d+)", file.name)
        if match:
            week_numbers.append(int(match.group(1)))

    # Return the next week number, or 1 if no weeks exist
    return max(week_numbers, default=0) + 1


def create_lecture_file(name: str, week: str, course: CourseInfo) -> Path:
    """Create a new lecture file from the template."""
    # Create file path
    file_name = f"Week {week} - {name}.md"
    file_path = course.directory / file_name

    # Check if file already exists
    if file_path.exists():
        console.print(f"[red]Error: File already exists: {file_path}[/red]")
        sys.exit(1)

    # Create metadata from template
    today = datetime.now().strftime("%Y-%m-%d")
    metadata = {
        "aliases": None,
        "checked": False,
        "course": f"[[{course.file}]]",
        "created": today,
        "last_edited": today,
        "draft": True,
        "tags": ["OMSCS"],
        "type": "lecture",
        "week": int(week),
    }

    # Create the file content (title includes week number)
    title = f"Week {week} - {name}"
    sections = [MarkdownSection(title=title, depth=1, lines=[])]

    note_file = NoteFile(file_path=str(file_path), metadata=metadata, sections=sections)

    # Write the file
    write_note_file(note_file)
    console.print(f"[green]✓ Created lecture file: {file_path}[/green]")

    return file_path


def add_lecture_to_course_file(name: str, week: str, course: CourseInfo) -> None:
    """Add the new lecture to the course index file."""
    # Read the existing course file
    course_file = read_note_file(str(course.index_file))

    # Find the Lectures section
    lectures_section = None
    for section in course_file.sections:
        if section.title == "Lectures":
            lectures_section = section
            break

    if not lectures_section:
        console.print("[yellow]Warning: Could not find Lectures section in course file[/yellow]")
        return

    # Create the new lecture link
    lecture_name = f"Week {week} - {name}"
    new_lecture_link = f"- [[{lecture_name}]]"

    # Add the new lecture to the lines
    if lectures_section.lines is None:
        lectures_section.lines = []

    # Insert in the correct position (sorted by week number)
    inserted = False
    for i, line in enumerate(lectures_section.lines):
        if line.startswith("- [[Week "):
            # Extract week number from existing line
            try:
                existing_week = int(line.split("Week ")[1].split(" ")[0])
                if int(week) < existing_week:
                    lectures_section.lines.insert(i, new_lecture_link)
                    inserted = True
                    break
            except (IndexError, ValueError):
                continue

    # If not inserted, append to the end
    if not inserted:
        lectures_section.lines.append(new_lecture_link)

    # Write the updated course file
    write_note_file(course_file)
    console.print(f"[green]✓ Added lecture to course file: {course.index_file}[/green]")


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

    # Add to course file
    add_lecture_to_course_file(name, week, selected_course)

    console.print("\n[bold green]✓ Lecture created successfully![/bold green]\n")


if __name__ == "__main__":
    main()
