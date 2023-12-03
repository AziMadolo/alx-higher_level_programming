#!/bin/bash
# Sends a POST request and shows the response body.
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
