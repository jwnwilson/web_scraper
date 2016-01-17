#!/usr/bin/env bash

command_exists () {
    type "$1" &> /dev/null ;
}

if [[ "$OSTYPE" == "darwin"* ]]; then
    # Mac OSX
    open cover/index.html
else
    # Default to linux look for browser command
    if command_exists google-chrome ; then
        google-chrome cover/index.html
    elif command_exists firefox ; then
        firefox cover/index.html
    else
        echo "Unable to open cover/index.html from terminal please open it with browser manually."
    fi
fi