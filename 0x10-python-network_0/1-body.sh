#!/bin/bash
# Retrieves and displays body if HTTP status code is 200.
VAR=$(curl -so /dev/null -I -w "%{http_code}" "$1"); if [ "$VAR" == 200 ]; then curl -sL "$1"; fi
