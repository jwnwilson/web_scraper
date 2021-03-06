#!/usr/bin/env bash

test_env="web_scraper_venv"
if [ ! -d "$test_env" ]
then
    virtualenv "$test_env"
    source "$test_env/bin/activate"
    pip install -r requirements.txt
else
    source "$test_env/bin/activate"
fi

# Simple python nose test script
# Run all tests:
# ./run_tests.sh
# Run all tests in module:
# ./run_tests.sh unit_tests.py
# Run all tests in class:
#./run_tests.sh unit_tests.py:TestUnitTests
# Run single test:
# ./run_tests.sh unit_tests.py:TestUnitTests.test_station_create

if [ "$1" == "" ]
then
    # Run tests
    nosetests -s tests/ --cover-package=web_scraper_module
elif [ $1 == "coverage" ]
then
    if [ ! -z "$2" ]
    then
        # Run tests
        nosetests -s "tests/$2" --with-coverage --cover-erase --cover-html --cover-package=web_scraper_modules
    else
        # Run tests
        nosetests -s tests/ --with-coverage --cover-erase --cover-html --cover-package=web_scraper_modules
    fi
else
    echo "tests/$1"
    # Run tests
    nosetests -s "tests/$1"
fi