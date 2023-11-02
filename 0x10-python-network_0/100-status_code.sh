#!/bin/bash
# takes in a URL and displays the status code
curl -so /dev/null -w "%{http_code}" "$1"
