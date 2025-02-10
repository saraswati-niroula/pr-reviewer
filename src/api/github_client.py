import os
import requests
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


class GitHubClient:
    def __init__(self, repo_owner, repo_name):
        self.repo_owner = repo_owner
        self.repo_name = repo_name
        self.base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
        self.headers = {"Authorization": f"token {GITHUB_TOKEN}"}

    def get_pull_request(self, pr_number):
        """Fetch pull request details"""
        url = f"{self.base_url}/pulls/{pr_number}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: {response.status_code}, {response.json()}")
            return None

    def get_pr_diff(self, pr_number):
        """Fetch the diff (code changes) of a pull request"""
        url = f"{self.base_url}/pulls/{pr_number}"
        response = requests.get(url, headers={**self.headers, "Accept": "application/vnd.github.v3.diff"})

        if response.status_code == 200 and response.text.strip():
            return response.text
        else:
            print(f"Error: {response.status_code}, {response.text}")
            return None
