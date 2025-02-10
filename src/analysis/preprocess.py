import re

from config import MAX_HUNK_LENGTH, CLEAN_DIFF_PATTERNS


def clean_diff(diff_text):
    """
    Cleans the PR diff by removing unnecessary metadata and keeping only meaningful code changes.
    """
    for pattern in CLEAN_DIFF_PATTERNS:
        diff_text = re.sub(pattern, "", diff_text, flags=re.MULTILINE)
    if not diff_text:
        return ""
    return diff_text


def split_diff_into_hunks(diff_text, max_hunk_length=MAX_HUNK_LENGTH):
    """
    Splits diff into logical hunks while respecting length limits.
    Maintains context within each code change block.
    """
    hunks = []
    current_hunk = []

    for line in diff_text.split("\n"):
        if line.startswith("@@"):
            if current_hunk:
                hunks.append("\n".join(current_hunk))
                current_hunk = []
        current_hunk.append(line)

        if len("\n".join(current_hunk)) > max_hunk_length:
            hunks.append("\n".join(current_hunk))
            current_hunk = []

    if current_hunk:
        hunks.append("\n".join(current_hunk))
    return hunks
