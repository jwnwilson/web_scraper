"""
    @Author: Noel Wilson (jwnwilson@hotmail.co.uk)
    Date: 11/01/2016

    Entry point for web scrapper exercise
"""
import logging
import json
import logging.config
import argparse
from web_scrapper_modules.sainsbury_webscrapper import SainsburyWebscrapper

parser = argparse.ArgumentParser(description='Simple Web scrapper exercise.')
parser.add_argument('-c','--command', default='default', help='Command to run on web scrapper',
                    required=True)
parser.add_argument('-a','--args', nargs='*', help='Command arguments, please consult README for details.',
                    required=True)
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
    Run command line args and call the Sainsbry_Webscrapper tool to return data
    :return: None
    """
    web_scrapper = SainsburyWebscrapper()
    logger.info("Sainsbury web scrapper initialized loaded running command: %s" % args.command)

    if args.command == "default":
        json_data = web_scrapper.get_product_data()
        logger.info("Found %s products with the following data:" % len(json_data["results"]))
        print json.dumps(json_data, indent=4, sort_keys=True)
    else:
        logger.error("Command not recognised please try again or run -h for help.")

if __name__ == "__main__":
    process_cmd()
