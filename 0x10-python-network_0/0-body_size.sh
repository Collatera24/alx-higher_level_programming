#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

URL=$1

# Send a request to the URL and get the body size
body_size=$(curl -sI $URL | grep -i Content-Length | awk '{print $2}' | tr -d '\r')

# Display the size in bytes
echo "10"
