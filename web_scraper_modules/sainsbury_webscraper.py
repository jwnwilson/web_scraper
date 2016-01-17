#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
    @Author: Noel Wilson
    @Date : 17/01/2016

    This Tool will connect to the url:
    "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html"

    The tool will then read all products get their:
    - Title
    - Cost
    Then navigate to their details url and add the following to a json to return
    - Details
    - Details page HTML size
"""
import logging
from web_scraper import Webscraper

logger = logging.getLogger(__name__)


class SainsburyWebscraper(object):
    """
    Sainsbury Webscraper designed to pull data from the test site in the format expected.
    """
    def __init__(self, target_url=None, **kwargs):
        if target_url:
            self.target_url = target_url
        else:
            self.target_url = "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html"

        self.web_scraper = Webscraper(url=self.target_url)
        self.load_product_links();

    def get_product_data(self):
        """
        Get the products data from the home page and turn the desired data in json format
        :return: string JSON data of products in format:
        {
            "results":[
            {
            "title":"Sainsbury's Avocado, Ripe & Ready x2",
            "size": "90.6kb",
            "unit_price": 1.80,
            "description": "Great to eat now - refrigerate at home 1 of 5 a day 1 avocado counts as 1 of your 5..."
            },
            {
            "title":"Sainsbury's Avocado, Ripe & Ready x4",
            "size": "87kb",
            "unit_price": 2.00,
            "description": "Great to eat now - refrigerate at home 1 of 5 a day 1 avocado counts as 1 of your 5..."
            }
            ],
            "total": 3.80
        }
        """
        output_json = {
            "results" : [],
            "total" : 0
        }
        for link in self.get_product_links():
            product_data = {}
            product_data["title"] = self.get_product_title(link.get('href'))
            product_data["description"] = self.get_product_description(link.get('href'))
            product_data["unit_price"] = self.get_product_price_per_unit(link.get('href'))
            product_data["size"] = self.get_product_html_size(link.get('href'))
            output_json["results"].append(product_data)
            output_json["total"] += float(product_data["unit_price"].replace(unicode("£",'utf-8'),""))

        return output_json

    def get_product_links(self):
        """
        Get all the product links from the home page for products
        :return: list of link objects
        """
        product_links = []
        self.web_scraper.set_current_path("/2015_Developer_Scrape/5_products.html")
        product_divs = self.web_scraper.get_elements("div", class_names=["productInfo"])
        for product_div in product_divs:
            child_header = self.web_scraper.get_child_elements(product_div, "h3")[0]
            product_link = self.web_scraper.get_child_elements(child_header, "a")[0]
            product_links.append(product_link)

        return product_links

    def load_product_links(self):
        """
        Load all product links into web scraper memeory
        :return: None
        """
        product_links = self.get_product_links()
        for link in product_links:
            self.web_scraper.read_site(link.get('href'))
        logger.info("All product links parsed into Web Scraper.")

    def get_product_title(self, product_path):
        """
        Get product page title from it's parsed data
        :return: string string product url
        """
        self.web_scraper.set_current_path(product_path)
        return self.web_scraper.get_title()

    def get_product_description(self, product_path):
        """
        Get product page description from it's parsed data
        :return: string string product url
        """
        self.web_scraper.set_current_path(product_path)
        return self.web_scraper.get_description()

    def get_product_price_per_unit(self, product_path):
        """
        Get product price per unit from it's parsed data
        :param product_path: string product url
        :return: string price per unit value
        """
        web_obj = self.web_scraper.get_web_object_from_url(product_path)
        price_unit_p = self.web_scraper.get_child_elements(web_obj, "p", class_names=["pricePerUnit"])[0]
        return price_unit_p.find(text=True).strip()

    def get_product_html_size(self, product_path):
        """
        Return the size of the html file at the product path
        :param product_path: string product url
        :return: string size of product_path in kb / mg
        """
        return self.web_scraper.get_url_page_size(product_path)