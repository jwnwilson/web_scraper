"""
    @Author: Noel Wilson (jwnwilson@hotmail.co.uk)
    @Date: 17/01/2016

    Web Scrapper unit tests
"""
import os
import sys
import unittest
import logging
from web_scrapper_modules.web_scrapper import Webscrapper
from requests.exceptions import HTTPError

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger(__name__)


class TestUnitTests(unittest.TestCase):
    """
    Unit tests for exercise
    """
    def test_webscrapper_create(self):
        """
        Test Station can be created with only uppercase Letters and distance
        as a number
        :return: None
        """
        websc = Webscrapper("http://www.google.com")

        self.assertEqual(websc.web_object.title, "Google")
        self.assertRaises(HTTPError, Webscrapper, "not a website")


if __name__ == "__main__":
    unittest.main()