#!/usr/bin/env bash

venv="web_scrapper_venv"

# Create virtual env for app if needed
if [ ! -d $venv ]
then
    virtualenv $venv
    source ${venv}/bin/activate
    pip install -r requirements.txt
else
    source ${venv}/bin/activate
fi

python main.py $@
