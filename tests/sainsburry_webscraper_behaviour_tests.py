#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Noel Wilson (jwnwilson@hotmail.co.uk)
    @Date: 17/01/2016

    Sainsbury Web scraper unit tests
"""
import os
import sys
import unittest
import logging
from web_scraper_modules.sainsbury_webscraper import SainsburyWebscraper

TEST_DIR = os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger(__name__)


class SainsburyWebscraperBehaviourTests(unittest.TestCase):
    """
    Unit tests for exercise
    """
    @classmethod
    def setUpClass(cls):
        cls.sainWebSc = SainsburyWebscraper()

    def test_webscraper_create(self):
        """
        Test webscraper initializes correctly
        :return: None
        """
        self.assertEqual(self.sainWebSc.web_scraper.get_web_object().title.string,
                         "Sainsbury's Apricot Ripe & Ready x5 | Sainsbury's")

    def test_load_product_links(self):
        """
        Test that the product links where loaded correctly
        :return: None
        """
        # Check all 8 pages loaded into memory
        self.assertEqual(len(self.sainWebSc.web_scraper.web_object), 8)

    def test_get_product_data(self):
        """
        Test get_product_data function returns desired json data
        :return: None
        """
        expected = {'total': 15.100000000000001,
                    'results': [
                        {
                            'size': '38.3KiB',
                            'description': u"Buy Sainsbury's Apricot Ripe & Ready x5 online from Sainsbury's, the same great quality, freshness and choice you'd find in store. Choose from 1 hour delivery slots and collect Nectar points.",
                            'unit_price': u'\xa33.50',
                            'title': u"Sainsbury's Apricot Ripe & Ready x5 | Sainsbury's"
                        },
                        {'size': '38.7KiB',
                         'description': u"Buy Sainsbury's Avocado Ripe & Ready XL Loose 300g online from Sainsbury's, the same great quality, freshness and choice you'd find in store. Choose from 1 hour delivery slots and collect Nectar points.",
                         'unit_price': u'\xa31.50',
                         'title': u"Sainsbury's Avocado Ripe & Ready XL Loose 300g | Sainsbury's"
                         },
                        {
                            'size': '43.4KiB',
                            'description': u'Burgers are a summer must-have and these homemade ones are perfect for a barbecue, topped with cool avocado and served with oven-baked potato wedges.',
                            'unit_price': u'\xa31.80',
                            'title': u"Sainsbury's Avocado, Ripe & Ready x2 | Sainsbury's"
                        },
                        {
                            'size': '38.7KiB',
                            'description': u"Buy Sainsbury's Avocados, Ripe & Ready x4 online from Sainsbury's, the same great quality, freshness and choice you'd find in store. Choose from 1 hour delivery slots and collect Nectar points.",
                            'unit_price': u'\xa33.20',
                            'title': u"Sainsbury's Avocados, Ripe & Ready x4 | Sainsbury's"
                        },
                        {
                            'size': '38.5KiB',
                            'description': u"Buy Sainsbury's Conference Pears, Ripe & Ready x4 (minimum) online from Sainsbury's, the same great quality, freshness and choice you'd find in store. Choose from 1 hour delivery slots and collect Nectar points.",
                            'unit_price': u'\xa31.50',
                            'title': u"Sainsbury's Conference Pears, Ripe & Ready x4 (minimum) | Sainsbury's"
                        },
                        {
                            'size': '38.6KiB',
                            'description': u"Buy Sainsbury's Golden Kiwi x4 online from Sainsbury's, the same great quality, freshness and choice you'd find in store. Choose from 1 hour delivery slots and collect Nectar points.",
                            'unit_price': u'\xa31.80',
                            'title': u"Sainsbury's Golden Kiwi x4 | Sainsbury's"
                        },
                        {
                            'size': '39.0KiB',
                            'description': u"Buy Sainsbury's Kiwi Fruit, Ripe & Ready x4 online from Sainsbury's, the same great quality, freshness and choice you'd find in store. Choose from 1 hour delivery slots and collect Nectar points.",
                            'unit_price': u'\xa31.80',
                            'title': u"Sainsbury's Kiwi Fruit, Ripe & Ready x4 | Sainsbury's"
                        }]
                    }
        json_data = self.sainWebSc.get_product_data()
        self.assertEqual(expected, json_data)

    def test_get_product_links(self):
        """
        Test get_product_links function returns desired json data
        :return: None
        """
        list_links = self.sainWebSc.get_product_links()
        self.assertEqual(len(list_links), 7)
        valid_links = [
            "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/sainsburys-apricot-ripe---ready-320g.html",
            "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/sainsburys-avocado-xl-pinkerton-loose-300g.html",
            "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/sainsburys-avocado--ripe---ready-x2.html",
            "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/sainsburys-avocados--ripe---ready-x4.html",
            "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/sainsburys-conference-pears--ripe---ready-x4-%28minimum%29.html",
            "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/sainsburys-golden-kiwi--taste-the-difference-x4-685641-p-44.html",
            "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/sainsburys-kiwi-fruit--ripe---ready-x4.html"
        ]
        for link in list_links:
            self.assertIn(link.get('href'), valid_links)

    def test_get_product_title(self):
        """
        Test get_product_title returns expected description
        :return: None
        """
        test_url = "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/" + \
            "sainsburys-apricot-ripe---ready-320g.html"
        product_1_title = self.sainWebSc.get_product_title(test_url)
        self.assertEqual(product_1_title, "Sainsbury's Apricot Ripe & Ready x5 | Sainsbury's")

    def test_get_product_description(self):
        """
        Test get_product_description returns expected description
        :return: None
        """
        test_url = "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/" + \
            "sainsburys-apricot-ripe---ready-320g.html"
        product_1_description = self.sainWebSc.get_product_description(test_url)
        self.assertEqual(product_1_description, "Buy Sainsbury's Apricot Ripe & Ready x5 online from Sainsbury's," + \
            " the same great quality, freshness and choice you'd find in store. Choose from 1 hour delivery slots " + \
            "and collect Nectar points.")

    def test_get_product_price(self):
        """
        Test get_product_description returns expected description
        :return: None
        """
        test_url = "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/" + \
            "sainsburys-apricot-ripe---ready-320g.html"
        product_1_description = self.sainWebSc.get_product_price_per_unit(test_url)
        self.assertEqual(product_1_description, unicode("£3.50",'utf-8'))

    def test_get_product_size(self):
        """
        Test get_product_description returns expected description
        :return: None
        """
        test_url = "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/" + \
            "sainsburys-apricot-ripe---ready-320g.html"
        product_1_description = self.sainWebSc.get_product_html_size(test_url)
        self.assertEqual(product_1_description, "38.3KiB")

if __name__ == "__main__":
    unittest.main()