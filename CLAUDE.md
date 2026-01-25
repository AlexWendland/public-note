# CLAUDE.md

Personal knowledge repository: academic notes, technical documentation, and learning materials. Content published to https://notes.awendland.co.uk/ using Hugo and GitHub Pages.

## Quick Commands

```bash
# Hugo - Local Development
hugo server          # Start dev server (PaperMod theme)
hugo server -D       # Include drafts in preview
hugo-dev             # Preview personal theme (in development)
hugo                 # Build to public/

# Python - Quality Tools
ruff check --fix     # Lint and auto-fix
ruff format          # Format code
uv run mypy .        # Type checking
uv run pytest        # Run tests

# CLI Tools (see detailed section below)
lecture              # Create OMSCS lecture note
definition           # Create definition/concept note
undraft              # Interactively undraft notes
excalidraw           # Start diagram editor
excalidraw-compile   # Export diagrams to SVG
```

## Tech Stack

- **Static Site**: Hugo (content in `content/`, config in `hugo.yaml`)
- **Themes**: hugo-admonitions (callouts), personal (Tailwind)
- **Python**: UV (package manager), devenv (Nix-based environment)
- **Dev Tools**: Ruff (lint/format), Mypy (types), Pytest (tests)
- **Deployment**: GitHub Actions → GitHub Pages (auto on push to `main`)

## Project Structure

```
/
├── content/            # All markdown content - Hugo reads from here
│   ├── OMSCS/          # Georgia Tech coursework (CS6210, CS7641, etc.)
│   ├── notes/          # Technical concepts, algorithms, CS topics
│   ├── education/      # Home page - education section
│   ├── work/           # Home page - work section
│   ├── personal_projects/  # Home page - projects section
│   └── thonks/         # Public thoughts/writing
├── static/images/      # Images and compiled diagrams
├── excalidraw/         # Excalidraw source files (.excalidraw)
├── scripts/            # CLI tools (lecture.py, undraft.py, etc.)
├── note_helper/        # Shared Python library for note management
├── layouts/            # Custom Hugo layouts/partials
├── themes/             # Hugo themes (PaperMod, hugo-admonitions, personal)
├── tests/              # Test suite
└── templates/          # Note templates (omscs-lecture.md, etc.)
```

## Hugo & Publishing

**Content source**: `content/` directory
**Images**: `static/` directory
**Build output**: `public/` directory
**Config**: `hugo.yaml`

**Features**:
- Math: MathJax 4 (`$$` for display, `$` for inline)
- Callouts: Obsidian-style via hugo-admonitions (`> [!note]`, `> [!example]`, `> [!warning]`)

**Deployment**: Auto-deploys to https://notes.awendland.co.uk/ on push to `main` via GitHub Actions.

## CLI Tools

### `lecture` - Create OMSCS Lecture Note
```bash
lecture
# Interactive prompts for course, lecture name, week number
# Auto-detects next week number from existing files
# Creates: content/OMSCS/CS6210/week_X_-_<name_slug>.md (lowercase, underscores)
# Updates: content/OMSCS/CS6210/_index.md
```

### `definition` - Create Definition/Concept Note
```bash
definition
# Interactive prompt for definition title
# Searches existing notes for duplicate title or alias matches
# Warns if conflicts found, allows override
# Creates: content/notes/<title_slug>.md (lowercase, underscores, hyphens preserved)
# Example: "B-tree" -> content/notes/b-tree.md
```

### `undraft` - Interactively Undraft Notes
```bash
undraft
# TUI for finding notes with draft: true
# Multi-select with Space, sorted by last edited (earliest first)
# Removes draft: true from frontmatter
```

### `excalidraw` - Create Diagrams
```bash
excalidraw
# Starts local Excalidraw on http://localhost:5173 (Docker)
# Save .excalidraw files to excalidraw/ directory
```

### `excalidraw-compile` - Export Diagrams to SVG
```bash
excalidraw-compile
# Exports excalidraw/*.excalidraw → static/images/excalidraw/*.excalidraw.svg
# Reference: ![name](../../static/images/excalidraw/diagram-name.excalidraw.svg)
```

**Excalidraw Workflow**:
1. Run `excalidraw` → create/edit diagrams
2. Save `.excalidraw` files to `excalidraw/` (pure JSON format, not Obsidian wrapper)
3. Run `excalidraw-compile` → exports to SVG
4. Reference in markdown notes

## Content Guidelines

**CRITICAL - File Naming**:
- **NO SPACES in filenames** - breaks Hugo URL generation and internal linking
- Lecture files use: `week_X_-_title_in_lowercase.md` (lowercase, underscores, no spaces)
- Example: `week_1_-_introduction_to_compilers.md`
- NOT `Week 1 - Introduction to Compilers.md`

**Format**:
- Markdown with YAML frontmatter
- Frontmatter fields: `created`, `last_edited`, `draft`, `tags`, `type`, `week`, `course_code`, `course_name`, `date_checked`
- Internal links: `[Page Name](page.md)` (not Obsidian's `[[Page Name]]`)
- Drafts: Use `draft: true` for work-in-progress
