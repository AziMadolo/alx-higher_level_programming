#!/bin/bash
# Fetches URL and prints response body size.
curl -s "$1" | wc -c
