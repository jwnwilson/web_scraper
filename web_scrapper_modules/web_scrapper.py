"""
    @Author: Noel Wilson
    @Date : 17/01/2016

    Generic webscrapper will use requests and beautifulsoup to parse a given website then have functions to return data
    from the returned object
"""
import requests
import logging
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class Webscrapper(object):
    """
    Sainsbury Webscrapper designed to pull data from the test site in the format expected.
    """
    def __init__(self, target_url, **kwargs):
        try:
            http_data = requests.get(target_url)
        except HTTPError as e:
            logger.error("Unable to connect to url: %s" % target_url)
            raise

        self.web_object = BeautifulSoup(http_data.text())