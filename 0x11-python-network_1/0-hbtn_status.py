#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status.
"""

import urllib.request


def fetch_status(url):
    """
    Fetches the content of the specified URL and prints the response body
    with tabulation before the hyphen.

    Args:
        url (str): The URL to fetch.

    Returns:
        None
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print("Body response:")
            print(f"\t- type: {type(body)}")
            print(f"\t- content: {body}")
            print(f"\t- utf8 content: {body.decode('utf-8')}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_status(url)
