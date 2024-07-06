#!/usr/bin/python3
import urllib.request
import sys

"""A script that
fetches https://intranet.hbtn.io/status.
"""


def fetch_x_request_id(url):
    try:
        with urllib.request.urlopen(url) as response:
            headers = response.getheaders()
            for header in headers:
                if header[0].lower() == 'x-request-id':
                    print(header[1])
                    return
            print("X-Request-Id header not found")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_x_request_id(url)
