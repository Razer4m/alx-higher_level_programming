#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL, and displays
the body of the response (decoded in utf-8).
Manages urllib.error.HTTPError exceptions and prints the error code.
"""


import urllib.request
import urllib.error
import sys


def fetch_url(url):
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)