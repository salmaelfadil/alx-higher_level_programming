#!/bin/bash
# takes in a URL and displays the body of the response after POST method
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1" 
