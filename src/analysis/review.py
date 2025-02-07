from config import MAX_OUTPUT_LENGTH


def create_review_prompt(code_chunk):
    return f"""As an experienced software engineer, review these code changes:
{code_chunk}

Analyze for:
1. Bugs or logical errors
2. Code style violations
3. Security vulnerabilities
4. Performance issues
5. Alternative approaches

Format your response with clear headings and bullet points. 
Highlight critical issues first. Be specific about line numbers."""


def postprocess_review(response_text):
    # Remove empty lines and truncate if needed
    cleaned = "\n".join([line.rstrip() for line in response_text.split("\n") if line.strip()])

    return cleaned[:MAX_OUTPUT_LENGTH]
