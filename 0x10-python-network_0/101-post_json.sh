#!/bin/bash
# Script sends a JSON POST request to a URL first argument, displays the body of response
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
