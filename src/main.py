
from dotenv import load_dotenv
from api.github_client import GitHubClient
from analysis.preprocess import clean_diff, split_diff_into_hunks
from api.huggingface_client import HuggingFaceClient
from analysis.review import create_review_prompt, postprocess_review
from utils import setup_logging

load_dotenv()

if __name__ == "__main__":
    setup_logging()
    # repo_owner = "Call-for-Code"
    # repo_name = "Practice-Pull-Requests"
    # pr_number = 11
    repo_name = "zite-backend"
    repo_owner = "zite-io"
    pr_number = 1498

    github_client = GitHubClient(repo_owner, repo_name)
    hf_client = HuggingFaceClient()

    pr_diff = github_client.get_pr_diff(pr_number)

    if pr_diff:
        cleaned_diff = clean_diff(pr_diff)
        hunks = split_diff_into_hunks(cleaned_diff)

        print("\n--- PR Review ---\n")
        for hunk in hunks:
            prompt = create_review_prompt(hunk)
            raw_review = hf_client.generate_review(prompt)
            clean_review = postprocess_review(raw_review)
            print(f"\n## Hunk Review ##\n{clean_review}\n")
