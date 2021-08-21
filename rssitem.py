class RssItem:
    """A class used to represent an RSS post"""

    def __init__(self, title, description, link, pub_date):
        self.title = title
        self.description = description
        self.link = link
        self.pub_date = pub_date