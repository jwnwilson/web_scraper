"""
    @Author: Noel Wilson (jwnwilson@hotmail.co.uk)
    @Date: 17/01/2016

    Sainsbury Web Scrapper unit tests
"""
import os
import sys
import unittest
import logging
from web_scrapper_modules.sainsbury_webscrapper import SainsburyWebscrapper

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
        sainWebSc = SainsburyWebscrapper()
        self.assertEqual(sainWebSc.web_scrapper.get_web_object().title.string, "Ripe & ready | Sainsbury's")

    def test_get_product_data(self):
        """
        Test get_product_data function returns desired json data
        :return: None
        """
        sainWebSc = SainsburyWebscrapper()
        json_data = sainWebSc.get_product_data()
        self.assertEqual("", json_data)

    def test_get_product_links(self):
        """
        Test get_product_links function returns desired json data
        :return: None
        """
        sainWebSc = SainsburyWebscrapper()
        list_links = sainWebSc.get_product_links()
        self.assertEqual(len(list_links), 7)


if __name__ == "__main__":
    unittest.main()