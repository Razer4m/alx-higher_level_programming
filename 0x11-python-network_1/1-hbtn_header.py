#!/usr/bin/python3
import urllib.request
import sys

"""A script that
fetches https://intranet.hbtn.io/status.
"""


def fetch_x_request_id(url):
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as resp:
        print(dict(resp.headers).get("X-Request-Id"))


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_x_request_id(url)
