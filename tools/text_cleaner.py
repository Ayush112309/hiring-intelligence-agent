# tools/text_cleaner.py

import re


def clean_text(text: str) -> str:
    """
    Cleans and normalizes text for better LLM processing.
    """

    if not text:
        return ""

    # Lowercase
    text = text.lower()

    # Remove special characters (keep basic punctuation)
    text = re.sub(r"[^a-z0-9\s.,]", " ", text)

    # Normalize spaces
    text = re.sub(r"\s+", " ", text)

    return text.strip()