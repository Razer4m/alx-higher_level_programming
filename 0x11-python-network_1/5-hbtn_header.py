#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL, and displays
the value of the X-Request-Id variable found in the header of the response.
"""

import requests
import sys


def fetch_x_request_id(url):
    response = requests.get(url)
    x_request_id = response.headers.get("X-Request-Id")
    print(x_request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_x_request_id(url)
