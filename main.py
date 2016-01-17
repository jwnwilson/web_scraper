"""
    @Author: Noel Wilson (jwnwilson@hotmail.co.uk)
    Date: 11/01/2016

    Entry point for web scraper exercise
"""
import logging
import json
import logging.config
import argparse
from web_scraper_modules.sainsbury_webscraper import SainsburyWebscraper

parser = argparse.ArgumentParser(description='Simple Web scraper exercise.')
parser.add_argument('-v','--verbose', action='store_true')

args = parser.parse_args()

# Configure simple logger
if args.verbose:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

def process_cmd():
    """
    Run command line args and call the Sainsbry_Webscraper tool to return data
    :return: None
    """
    web_scraper = SainsburyWebscraper()
    logger.info("Sainsbury web scraper initialized and loaded data from SainsburyWebscraper")

    json_data = web_scraper.get_product_data()
    logger.info("Found %s products with the following data:" % len(json_data["results"]))
    print json.dumps(json_data, indent=4, sort_keys=True)

if __name__ == "__main__":
    process_cmd()
