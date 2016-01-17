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
from web_scrapper import WebScrapper

logger = logging.getLogger(__name__)


class SainsburyWebscrapper(object):
    """
    Sainsbury Webscrapper designed to pull data from the test site in the format expected.
    """
    def __init__(self, target_url=None, **kwargs):
        if target_url:
            self.target_url = target_url
        else:
            self.target_url = "http://hiring-tests.s3-website-eu-west-1.amazonaws.com/2015_Developer_Scrape/5_products.html"
        self.web_scrapper = WebScrapper(url=self.target_url)

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
        pass

    def get_product_links(self):
        """
        Get all the product links from the home page for products
        :return: list of link objects
        """
        product_links = []
        product_divs = self.web_scrapper.get_elements("div", class_names=["productInfo"])
        for product_div in product_divs:
            child_header = self.web_scrapper.get_child_elements(product_div, "h3")[0]
            product_link = self.web_scrapper.get_child_elements(child_header, "a")[0]
            product_links.append(product_link)

        return product_links

    def load_product_links(self):
        """
        Load all product links into web scrapper memeory
        :return: None
        """
        product_links = self.get_product_links()
        self.web_scrapper.read_site()