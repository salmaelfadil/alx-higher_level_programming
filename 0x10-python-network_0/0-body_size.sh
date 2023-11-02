#!/bin/bash
# displays the size of the body of response of URL
curl -s "$1" | wc -c
