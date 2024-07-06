#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL, and displays
the value of the X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys


def fetch_x_request_id(url):
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as resp:
        print(dict(resp.headers).get("X-Request-Id"))


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_x_request_id(url)
