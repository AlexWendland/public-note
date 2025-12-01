import re

from note_helper.constants import ALIAS_FIELD
from note_helper.models import MarkdownSection, NoteFile, NoteLink

ALIAS_LINKS: dict[str, NoteLink] = {}

FILE_ALIASES: dict[str, set[NoteLink]] = {}


def _set_alias_link(alias: str, file: str):
    alias = alias.strip()
    file = file.strip()
    current_link = ALIAS_LINKS.get(alias)

    if not current_link:
        ALIAS_LINKS[alias] = NoteLink(file_name=file, alias=alias if alias != file else None)
    elif current_link.file_name != file:
        raise ValueError(f'Alias "{alias}" has multiple links: "{current_link.file_name}" and "{file}"')


def clean_aliases_from_file(note_file: NoteFile) -> None:
    """
    Gets all aliases from a list of note files.
    """
    _set_aliases_from_metadata(note_file)
    _clean_aliases_from_sections(note_file)


def _set_aliases_from_metadata(note_file: NoteFile) -> None:
    """
    Gets all aliases from the metadata of a note file.
    """
    aliases = note_file.metadata.get(ALIAS_FIELD, [])
    file_name = note_file.file_name
    _set_alias_link(file_name, file_name)
    if not aliases:
        return
    for alias in aliases:
        _set_alias_link(alias, file_name)


def _clean_aliases_from_sections(note_file: NoteFile):
    """
    Gets all aliases from a file.
    """
    links = []
    for section in note_file.sections:
        section_links = _clean_section_of_aliases(section)
        links.extend(section_links)

    file_links = set()
    for link in links:
        if not link.alias:
            continue
        if not link.section:
            _set_alias_link(link.alias, link.file_name)
            continue
        file_links.add(link)
    FILE_ALIASES[note_file.file_name] = file_links


def _clean_section_of_aliases(section: MarkdownSection) -> list[NoteLink]:
    """
    Removes all aliases from a section.
    """
    links: list[NoteLink] = []
    if section.title:
        section.title, links = _clean_string_of_aliases(section.title)
    new_lines = []
    if section.lines:
        for line in section.lines:
            new_line, line_links = _clean_string_of_aliases(line)
            links.extend(line_links)
            new_lines.append(new_line)
    section.set_lines(new_lines)
    return links


def _clean_string_of_aliases(text: str) -> tuple[str, list[NoteLink]]:
    """
    Replaces all wiki-style aliases with their string representation. Then returns the NoteLinks in a list.
    """
    print("Pre-clean string:", text)
    pattern = r"(?<!\!)\[\[(.*?)\]\]"
    matches = set(re.findall(pattern, text))
    links = []
    for match in matches:
        link = NoteLink.from_string(match)
        text = re.sub(rf"(?<!\!)\[\[{match}\]\]", link.clean_representation(), text)
        links.append(link)
    print("Post-clean string:", text)
    return text, links


def build_rehydration_map(alias_links=ALIAS_LINKS) -> dict[str, str | None]:
    """
    Builds a map of all aliases to their link.
    """
    rehydration_dictionary: dict[str, str | None] = {}
    for alias in sorted(alias_links.keys(), key=len):
        last_alias = None
        for length in range(1, len(alias)):
            sub_alias = alias[:length]
            if sub_alias in rehydration_dictionary:
                last_alias = rehydration_dictionary[sub_alias]
            else:
                rehydration_dictionary[sub_alias] = last_alias
        rehydration_dictionary[alias] = alias
    return rehydration_dictionary


def _rehydrate_string(text: str, rehydration_dictionary: dict) -> str:
    """
    Rehydrates a string with the rehydration map.
    """
    modified_text = text
    modified_index = 0
    skip = False
    while text:
        # Skip if we are in a link
        if not skip and len(text) > 1 and text[:2] == "[[":
            skip = True
            modified_index += 2
            text = text[2:]
            continue
        if skip and len(text) > 1 and text[:2] == "]]":
            skip = False
            modified_index += 2
            text = text[2:]
            continue
        if skip:
            text = text[1:]
            modified_index += 1
            continue

        # Find the longest alias that matches the text
        text_length = len(text)
        search_index = 1
        while search_index < text_length and text[:search_index] in rehydration_dictionary:
            current_alias = rehydration_dictionary[text[:search_index]]
            search_index += 1

        # If we found an alias, replace it and continue
        if current_alias:
            link = ALIAS_LINKS[current_alias]
            link_text = link.link
            modified_text = (
                modified_text[:modified_index] + link_text + modified_text[modified_index + len(current_alias) :]
            )
            text = text[len(current_alias) :]
            modified_index += len(link_text)
        else:
            text = text[1:]
            modified_index += 1

    return modified_text


def rehydrate_file(note_file: NoteFile, rehydration_dictionary: dict) -> None:
    """
    Rehydrates a note file with the rehydration map.
    """
    for section in note_file.sections:
        new_lines = []
        if section.lines:
            for line in section.lines:
                new_lines.append(_rehydrate_string(line, rehydration_dictionary))
        section.set_lines(new_lines)
