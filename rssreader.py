import requests
from bs4 import BeautifulSoup
from rssitem import RssItem


class RssReader:
    """The class handles the acquisition of the posts from the RSS feed url"""

    def __init__(self, feed_url):
        self._feed_url = feed_url

    def get_data(self):
        """Getting the RSS feed xml from the given url using requests"""
        try:
            response = requests.get(self._feed_url)
            response.raise_for_status()
        except requests.exceptions.RequestException as error:
            raise SystemExit(error)
        return response

    def parse_data_to_items(self):
        """Parsing the xml and getting only the items"""
        try:
            soup = BeautifulSoup(self.get_data().text, 'xml')
            return soup.findAll('item')
        except Exception as error:
            print("The xml from " + self._feed_url + " could not be parsed")
            raise SystemExit(error)

    def get_rss_objects(self):
        """Mapping the xml to RssItem Objects and returning the Data"""
        items = self.parse_data_to_items()
        rss_objects = []
        for item in items:
            obj = RssItem(title=item.title.text,
                          description=item.description.text,
                          link=item.link.text,
                          pub_date=item.pubDate.text)
            rss_objects.append(obj)
        return rss_objects