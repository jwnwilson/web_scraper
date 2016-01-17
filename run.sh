#!/usr/bin/env bash

# Create virtual env for app if needed
if [ ! -d web_scrapper ]
then
    virtualenv web_scrapper
fi
source web_scrapper/bin/activate
python run_ex.py $@
