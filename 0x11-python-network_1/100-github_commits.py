#!/usr/bin/python3
"""
A script that takes 2 arguments (repository name and owner name) and lists
the 10 most recent commits from the specified repository using the GitHub API.
Prints all commits in the format: <sha>: <author name>
"""

import requests
import sys


def list_commits(repo_name, owner_name):
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url, params={'per_page': 10})
    commits = response.json()
    for commit in commits:
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")


if __name__ == "__main__":
    repository_name = sys.argv[1]
    owner_name = sys.argv[2]
    list_commits(repository_name, owner_name)
