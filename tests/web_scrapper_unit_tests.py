"""
    @Author: Noel Wilson (jwnwilson@hotmail.co.uk)
    @Date: 17/01/2016

    Web Scrapper unit tests
"""
import os
import sys
import unittest
import logging
from web_scrapper_modules.web_scrapper import WebScrapper
from requests.exceptions import ConnectionError, MissingSchema

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger(__name__)


class TestUnitTests(unittest.TestCase):
    """
    Unit tests for exercise
    """
    def test_webscrapper_constructor(self):
        """
        Test WebScrapper constructor parsed a website as intended
        as a number
        :return: None
        """
        websc = WebScrapper(url="http://www.google.com")
        web_obj = websc.web_object['']

        self.assertEqual(web_obj.title.string, "Google")

    def test_webscrapper_read_site(self):
        """
        Test WebScrapper read site command returns expected output and raises exceptions
        as a number
        :return: None
        """
        websc = WebScrapper()
        websc.read_site("http://www.google.com")
        web_obj = websc.web_object['']

        self.assertEqual(web_obj.title.string, "Google")
        self.assertRaises(MissingSchema, websc.read_site, "not a website")
        self.assertRaises(ConnectionError, websc.read_site, "https://www.testtestest.com")

    def test_webscrapper_get_object(self):
        """
        Test WebScrapper get object will return a parsed webpage
        :return:
        """
        websc = WebScrapper()
        websc.read_site("http://www.google.com")
        web_obj = websc.get_web_object()

        self.assertEqual(web_obj.title.string, "Google")

if __name__ == "__main__":
    unittest.main()