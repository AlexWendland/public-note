import io
import logging
from enum import Enum
from typing import List, Optional

import openai

from obsidian_helper import constants, models, read_obsidian, write_obsidian

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are a content creator's assistant. "
    "The content is mathematically rigorous, concise, and has to be correct but is designed to be understandable by a "
    "layman. "
    "The content creator is a mathematician who is a native English speaker. "
    "He is dyslexic and has trouble with spelling and grammar. "
    "Below is one article he has written by him in Obsidian so items enclosed by [[]] represent another article "
    "otherwise it should follow markdown syntax. "
    "If you edit the article please leave all links enclosed by [[]] instead of in markdown syntax. "
    "Please check it over for accuracy, ease of understanding, spelling, and grammar. "
    "If there are not any major errors or the article is empty please write NO ERRORS only. "
    "If it is worth correcting errors please return a corrected version of the article only. "
)

class OpenAIOutput(Enum):
    NO_CHANGE = 1,
    ERRORS = 2

def query_article(article:str) -> Optional[str]:
    tries = 0
    max_tries = 3
    completion = None
    while tries < max_tries:
        try:
            completion = openai.chat.completions.create(
                model="gpt-4-1106-preview",
                messages=[
                    {
                        "role": "system",
                        "content": SYSTEM_PROMPT},
                    {"role": "user", "content": article}
                ]
            )
        except openai.APITimeoutError:
            tries += 1
            continue

    if completion is None:
        return OpenAIOutput.ERRORS

    content = completion.choices[0].message.content

    if content == "NO ERRORS":
        return OpenAIOutput.NO_CHANGE
    else:
        return content


def update_article(obsidian_file: models.ObsidianFile):
    article = turn_sections_to_string(obsidian_file.sections)
    reviewed_article = query_article(article)

    if reviewed_article == OpenAIOutput.ERRORS:
        logger.error(f"{obsidian_file.file_path} ERROR: OpenAI timed out file not checked.")
        return

    if reviewed_article == OpenAIOutput.NO_CHANGE:
        logger.info(f"{obsidian_file.file_path} INFO: No changes made to file.")
        obsidian_file.metadata[constants.CHECKED_FIELD] = True
        return

    file = io.StringIO(reviewed_article)
    reviewed_article_sections = read_obsidian.extract_all_sections(next(file, None), file)
    obsidian_file.sections = reviewed_article_sections
    logger.info(f"{obsidian_file.file_path} INFO: OpenAI updated the file.")

    obsidian_file.metadata[constants.CHECKED_FIELD] = True


def check_different_sections(old_sections: List[models.MarkdownSection], new_sections: List[models.MarkdownSection]):
    """
    Checks if the sections are different.
    """
    for index, (old_section, new_section) in enumerate(zip(old_sections, new_sections)):
        if old_section.title != new_section.title:
            print(f"Different section titles at the {index}'th section.")
            print(f"Old title: {old_section.title}")
            print(f"New title: {new_section.title}")
        if old_section.depth != new_section.depth:
            print(f"Changed section depth at the {index}'th section.")
            print(f"Old depth: {old_section.depth}")
            print(f"New depth: {new_section.depth}")

def turn_sections_to_string(sections: List[models.MarkdownSection]) -> str:
    """
    Turns a list of sections into a string.
    """
    string = ""
    for section in sections:
        string += write_obsidian.turn_section_to_string(section)
    return string
