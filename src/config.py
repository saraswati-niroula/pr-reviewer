# src/config.py

# Diff processing
MAX_HUNK_LENGTH = 1500  # Used in split_diff_into_hunks
CLEAN_DIFF_PATTERNS = [  # Used in clean_diff
    r"^diff --git a/.*? b/.*?$",
    r"^index \w+\.\.\w+ \d+$",
    r"^--- a/.*?$",
    r"^\+\+\+ b/.*?$"
]

# Model configuration
PR_REVIEW_MODEL = "codellama/CodeLlama-34b-Instruct-hf"
MAX_RESPONSE_TOKENS = 1024
MODEL_TEMPERATURE = 0.2

# Safety limits
MAX_OUTPUT_LENGTH = 3000  # Used in postprocess_review
