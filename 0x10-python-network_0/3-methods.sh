#!/bin/bash
# Send an OPTIONS request to get allowed methods
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
