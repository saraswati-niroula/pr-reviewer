from api.github_client import GitHubClient

if __name__ == "__main__":
    repo_owner = "Call-for-Code"  # Repository owner
    repo_name = "Practice-Pull-Requests"  # Repository name
    pr_number = 2  # Pull request number

    github_client = GitHubClient(repo_owner, repo_name)

    # Fetch PR details
    pr_data = github_client.get_pull_request(pr_number)
    if pr_data:
        print(f"Title: {pr_data['title']}")
        print(f"Author: {pr_data['user']['login']}")

    # Fetch PR diff
    pr_diff = github_client.get_pr_diff(pr_number)
    if pr_diff:
        print("\n--- PR Diff ---\n")
        print(pr_diff[:500])  # Print only the first 500 characters
