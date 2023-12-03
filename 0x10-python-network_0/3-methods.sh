#!/bin/bash
# Requests and lists accepted HTTP methods for a URL.
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
