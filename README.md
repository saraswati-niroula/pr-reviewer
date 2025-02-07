# PR Reviewer 🤖

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

An AI-powered code review assistant that analyzes GitHub pull requests using large language models (LLMs) to provide actionable feedback on code changes.

## Features ✨

- 🧹 **Diff Cleaning**: Removes metadata from GitHub diffs
- 🧩 **Context-Aware Chunking**: Splits large diffs into logical hunks
- 🤖 **LLM Integration**: Supports multiple code-aware models (CodeLlama, StarCoder)
- 🔍 **Structured Analysis**: Identifies bugs, security issues, and performance concerns
- 📋 **Formatted Output**: Generates Markdown-ready reviews with line number references

## Installation 📦

1. Clone the repository:

```bash
    git clone git@github.com:saraswati-niroula/pr-reviewer.git
    cd pr-reviewer

```

2. Create and activate virtual environment:

```bash
    python -m venv venv
    source venv/bin/activate # Linux/MacOS
    venv\Scripts\activate # Windows
```

3. Install dependencies:

```bash
    pip install -r requirements.txt

```

4. Create environment file:

```bash
    touch .env
```

## Configuration

1. Set environment variables:
   GITHUB_TOKEN=your_github_personal_access_token
   HF_API_KEY=your_huggingface_api_key

2. Setup config file (src/config.py) (optional):

   # Model configuration

   MAX_RESPONSE_TOKENS = 1024 # Response length limit
   MODEL_TEMPERATURE = 0.2 # Creativity control (0-1)

   # Processing parameters

   MAX_HUNK_LENGTH = 1500 # Diff chunk size in characters
