#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status and displays
the body of the response in a specific format.
"""

import requests


def fetch_status(url):
    response = requests.get(url)
    body = response.text
    print("Body response:")
    print(f"\t- type: {type(body)}")
    print(f"\t- content: {body}")


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    fetch_status(url)
