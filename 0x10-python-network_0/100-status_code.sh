#!/bin/bash
# # Send a request to the URL and display the status code of the response
curl -sLw "%{http_code}" -o /dev/null "$1"
