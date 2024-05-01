#!/bin/bash

# Check if a URL is provided as an argument
curl -s "$1" | wc -c
