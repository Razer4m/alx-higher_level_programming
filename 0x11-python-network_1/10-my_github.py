#!/usr/bin/python3
"""
A script that takes your GitHub credentials
(username and personal access token)
and uses the GitHub API to display your user id.
"""

import requests
import sys


def fetch_github_user_id(username, token):
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get("id"))
    else:
        print("None")


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    fetch_github_user_id(username, token)
