"""
    @Author: Noel Wilson (jwnwilson@hotmail.co.uk)
    @Date: 17/01/2016

    Sainsbury Web Scrapper unit tests
"""
import os
import sys
import unittest
import logging
from web_scrapper_modules.sainsbury_webscrapper import Sainsbury_Webscrapper

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger(__name__)


class TestUnitTests(unittest.TestCase):
    """
    Unit tests for exercise
    """
    def test_webscrapper_create(self):
        """
        Test webscrapper initializes correctly
        :return: None
        """
        pass


if __name__ == "__main__":
    unittest.main()