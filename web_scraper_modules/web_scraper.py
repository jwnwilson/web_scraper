"""
    @Author: Noel Wilson
    @Date : 17/01/2016

    Generic webscraper will use requests and beautifulsoup to parse a given website then have functions to return data
    from the returned object
"""
import requests
import urlparse
import urllib
import logging
from requests.exceptions import HTTPError, ConnectionError, MissingSchema
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class Webscraper(object):
    """
    Webscraper designed to pull data from the test site and wrap around beautiful soup to turn data.

    Will parse multiple paths for current website to make reading of static data from multiple pages easier
    """
    def __init__(self, **kwargs):
        self.web_object = {}
        self.url = None
        self.current_path = None

        if "url" in kwargs:
            self.url = kwargs.get("url")
            self.read_site(self.url)


    def _get_path(self, url):
        """
        Get path from url, e.g. http://wwww.google.com/test/test
        return "/test/test"
        :param url: url to get path from
        :return: string path from url
        """
        url_obj = urlparse.urlparse(url)
        path = url_obj.path
        return path

    def _get_hostname(self, url):
        """
        Get hostname from url e.g. http://wwww.google.com/test/test
        return "/test/test"

        :param url: url to get host from
        :return: string host from url
        """
        url_obj = urlparse.urlparse(url)
        host = url_obj.scheme + "://" +url_obj.netloc
        return host

    def read_site(self, url):
        """
        Parse a site using beautiful soup and save object in instance, will use a subdomain key to store each subdomain
        object in the web object dict ot make reading multiple pages easier
        :param url: target url to parse
        :return:
        """
        # Get url path
        path = self._get_path(url)
        hostname = self._get_hostname(url)

        try:
            http_data = requests.get(url)
        except (ConnectionError, MissingSchema) as e:
            logger.error("Unable to connect to url: %s" % url, exc_info=True)
            raise

        if self.url is None:
            self.url = hostname
        # If blank subdomain we're parsing a new website
        if path == "" and self.url != hostname:
            logger.debug("New website host found, clearing existing data")
            self.url = hostname
            self.web_object = {}

        self.web_object[path] = BeautifulSoup(http_data.text, "html.parser")
        self.current_path = path
        logger.info("Successfully loaded site: %s" % url)

    def get_web_object(self, path=None):
        """
        Get the webobject for a path on the parsed website, default is the current_path or last read page
        :param path: string path key to get web object for
        :return: Object parsed web object
        """
        if path is None:
            path = self.current_path
        if self.url is None:
            error_msg = "Can't get web object for path: %s no website parsed." % path
            logger.error(error_msg)
            raise RuntimeError(error_msg)
        if path not in self.web_object:
            error_msg = "Can't get web object for path: %s parsed path not found." % path
            logger.error(error_msg)
            raise RuntimeError(error_msg, exc_info=True)

        return self.web_object.get(path)

    def get_web_object_from_url(self, url):
        """
        Get the webobject from a url, this is a convenience method
        :param path: string url to get web object for
        :return: Object parsed web object
        """
        path = self._get_path(url)
        return self.get_web_object(path)

    def set_current_path(self, path):
        """
        Set the current path of the webobject we want to work with
        :param path: path key
        :return: None
        """
        # check it's not the full path
        if path not in self.web_object:
            path = self._get_path(path)
        if path not in self.web_object:
            error_msg = "Can't set current path to: '%s' not parsed in web object" % path
            logger.error(error_msg)
            raise RuntimeError(error_msg)
        self.current_path = path

    def get_title(self):
        """
        Get the title of passed or current path
        :return: string title of current page
        """
        return self.get_web_object().title.string

    def get_description(self, path=None):
        """
        Get the description of passed or current path
        :return: string meta tag description of the current page
        """
        if path is None:
            path = self.current_path
        desc = ""
        for meta in self.get_web_object(path).findAll("meta"):
            metaname = meta.get('name', '').lower()
            metaprop = meta.get('property', '').lower()
            if 'description' == metaname.lower() or metaprop.find("description")>0:
                desc = meta['content'].strip()
        return desc

    def get_child_elements(self, element, tagname, ids=None, class_names=None, ):
        """
        Return child elements of inputed element

        :param tagname: tagname to searh for
        :param ids: id to search for
        :param class_names: class names to search for
        :return: list of web elements
        """
        if ids is None:
            ids = []
        if class_names is None:
            class_names = []
        if isinstance(ids, type([])) is False or isinstance(class_names, type([])) is False:
            error_msg = "get_elements expects a list of ids and a list of class_names"
            logger.error(error_msg)
            raise TypeError(error_msg)

        found_child_elements = element.findAll(tagname, {"id": ids, "class" : class_names})
        return found_child_elements

    def get_elements(self, tagname, ids=None, class_names=None ):
        """
        Return a list of all elements on current page with ids or classnames matching those in the params

        :param ids: ids of href DOM elements to search for
        :param class_names: class_names of href DOM elements to search for
        :return: list of href elements
        """
        web_obj = self.get_web_object()
        # Beautiful soup search dict
        found_elements = self.get_child_elements(web_obj, tagname, ids, class_names)

        logger.info("Found %s elements with ids: %s and classNames: %s" %
                    (len(found_elements), str(ids), str(class_names)))

        return found_elements

    @classmethod
    def get_url_page_size_in_btyes(cls, url):
        """
        Get size in bytes of page at url
        :param url: url to query
        :return: int in bytes
        """
        file = urllib.urlopen(url)
        size = file.headers.get("content-length")
        # In case there is no content-length header
        if not size:
            size = len(file.read())
        file.close()
        return size

    @classmethod
    def get_url_page_size(cls, url):
        """
        Get size in bytes, kb or mb of page at url
        :param url: url to query
        :return: string size in bytes, kb or mg
        """
        def sizeof_fmt(num, suffix='B'):
            """
            Shamlessly stolen from:
            http://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size

            :param num: number of bytes to format
            :param suffix: string to append to result
            :return: formated human readable bytes size
            """
            num = int(num)
            for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
                if abs(num) < 1024.0:
                    return "%3.1f%s%s" % (num, unit, suffix)
                num /= 1024.0
            return "%.1f%s%s" % (num, 'Yi', suffix)

        bytes = cls.get_url_page_size_in_btyes(url)
        return sizeof_fmt(bytes)
