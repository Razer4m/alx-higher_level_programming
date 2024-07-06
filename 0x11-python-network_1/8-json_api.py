#!/usr/bin/python3
"""
A script that takes in a letter, sends a POST request
to http://0.0.0.0:5000/search_user
with the letter as a parameter, and handles the JSON response.
"""

import requests
import sys


def search_user(letter):
    url = "http://0.0.0.0:5000/search_user"
    data = {'q': letter}
    response = requests.post(url, data=data)
    try:
        json_response = response.json()
        if json_response:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    search_user(letter)
