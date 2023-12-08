from .constants import ALIAS_FIELD
from .models import ObsidianFile, MarkdownSection

ALIAS_LINKS = dict()

def set_alias_link(alias: str, file: str):
    current_link = ALIAS_LINKS.get(alias)

    if not current_link
        ALIAS_LINKS[alias] = file
    elif current_link != file:
        raise ValueError(f"Alias {alias} has multiple links: {current_link} and {file}")

def set_aliases_from_metadata(obsidian_file: ObsidianFile) -> None:
    """
    Gets all aliases from the metadata of an obsidian file.
    """
    aliases = obsidian_file.metadata.get(ALIAS_FIELD, [])
    file_name = obsidian_file.file_name()
    set_alias_link(file_name, file_name)
    if isinstance(aliases, str):
        aliases = [aliases]
    for alias in aliases:
        set_alias_link(alias, file_name)

def set_aliases_from_section(obsidian_file: ObsidianFile, section: MarkdownSection) -> None:
    """
    Gets all aliases from a section of an obsidian file.
    """
    aliases = section.title.split(",")
    file_name = obsidian_file.file_name()
    set_alias_link(file_name, file_name)
    for alias in aliases:
        set_alias_link(alias, file_name)
