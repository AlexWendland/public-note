"""CLI tool to create a new OMSCS lecture note."""

import sys
from datetime import datetime
from pathlib import Path

from note_helper.models import MarkdownSection, NoteFile
from note_helper.read_note import read_note_file
from note_helper.write_note import write_note_file


def prompt_input(prompt: str) -> str:
    """Prompt user for input."""
    return input(f"{prompt}: ").strip()


def create_lecture_file(name: str, week: str, repo_root: Path) -> Path:
    """Create a new lecture file from the template."""
    # Create file path
    file_name = f"Week {week} - {name}.md"
    file_path = repo_root / "notes" / "OMSCS" / "CS6210" / file_name

    # Check if file already exists
    if file_path.exists():
        print(f"Error: File already exists: {file_path}")
        sys.exit(1)

    # Create metadata from template
    today = datetime.now().strftime("%Y-%m-%d")
    metadata = {
        "aliases": None,
        "checked": False,
        "course": "[[CS6210 Advanced Operating Systems]]",
        "created": today,
        "last_edited": today,
        "draft": True,
        "tags": ["OMSCS"],
        "type": "lecture",
        "week": int(week),
    }

    # Create the file content
    sections = [MarkdownSection(title=name, depth=1, lines=[])]

    note_file = NoteFile(file_path=str(file_path), metadata=metadata, sections=sections)

    # Write the file
    write_note_file(note_file)
    print(f"Created lecture file: {file_path}")

    return file_path


def add_lecture_to_course_file(name: str, week: str, repo_root: Path) -> None:
    """Add the new lecture to the course index file."""
    course_file_path = repo_root / "notes" / "OMSCS" / "CS6210 Advanced Operating Systems.md"

    # Read the existing course file
    course_file = read_note_file(str(course_file_path))

    # Find the Lectures section
    lectures_section = None
    for section in course_file.sections:
        if section.title == "Lectures":
            lectures_section = section
            break

    if not lectures_section:
        print("Error: Could not find Lectures section in course file")
        sys.exit(1)

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
    print(f"Added lecture to course file: {course_file_path}")


def main():
    """Main entry point for the lecture CLI tool."""
    print("=== Create New OMSCS Lecture ===\n")

    # Get repo root (parent of scripts directory)
    repo_root = Path(__file__).parent.parent

    # Prompt for inputs
    name = prompt_input("Lecture name")
    week = prompt_input("Week number")

    # Validate week is a number
    try:
        int(week)
    except ValueError:
        print(f"Error: Week must be a number, got: {week}")
        sys.exit(1)

    # Create the lecture file
    create_lecture_file(name, week, repo_root)

    # Add to course file
    add_lecture_to_course_file(name, week, repo_root)

    print("\n✓ Lecture created successfully!")


if __name__ == "__main__":
    main()
