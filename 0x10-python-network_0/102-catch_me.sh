#!/bin/bash
# Make a request to the URL and display the response body
curl -s -L -X PUT 0.0.0.0:5000/catch_me -d "user_id=98"
