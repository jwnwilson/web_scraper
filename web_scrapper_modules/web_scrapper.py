"""
    @Author: Noel Wilson
    @Date : 17/01/2016

    Generic webscrapper will use requests and beautifulsoup to parse a given website then have functions to return data
    from the returned object
"""
import requests
import logging
from requests.exceptions import HTTPError, ConnectionError, MissingSchema
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class Webscrapper(object):
    """
    Sainsbury Webscrapper designed to pull data from the test site in the format expected.
    """
    def __init__(self, **kwargs):
        self.web_object = None

        if "url" in kwargs:
            url = kwargs.get("url")
            self.read_site(url)

    def read_site(self, url):
        """
        Parse a site using beautiful soup and save object in instance
        :param url:
        :return:
        """
        try:
            http_data = requests.get(url)
        except (ConnectionError, MissingSchema) as e:
            logger.error("Unable to connect to url: %s" % url, exc_info=True)
            raise

        self.web_object = BeautifulSoup(http_data.text, "html.parser")
        logger.info("Successfully loaded site: %s" % url)