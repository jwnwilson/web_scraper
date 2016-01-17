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

class Sainsbury_Webscrapper(object):
    """
    Sainsbury Webscrapper designed to pull data from the test site in the format expected.
    """
    def __init__(self):
        pass