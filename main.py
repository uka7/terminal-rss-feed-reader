import html
from rssreader import RssReader
import sys
import validators


def validate_input():
    """This function checks the input arguments if the urls are valid or not"""
    # Check if there is at least one argument
    if len(sys.argv) == 1:
        raise SystemExit("Input error: At least one url should be provided")
    # Validating if all arguments are valid urls
    for arg_index in range(1, len(sys.argv)):
        valid = validators.url(sys.argv[arg_index])
        if not valid:
            raise SystemExit("This url is not valid: " + sys.argv[arg_index])


def get_all_feed():
    """This function iterates through all urls and gets their posts"""
    items_objects = []
    for arg_index in range(1, len(sys.argv)):
        items_objects += RssReader(feed_url=sys.argv[arg_index]).get_rss_objects()
    return items_objects


def print_feed(items_objects):
    """Printing the results from all urls"""
    print("---------------------------")
    print("Number of RSS posts: ", len(items_objects))
    print("---------------------------")
    for item_object in items_objects:
        # Used html.unescape for the conversion of named and numeric character references in the rss feed response to
        # the corresponding Unicode characters
        print("Title: " + html.unescape(item_object.title))
        print("Description: " + html.unescape(item_object.description))
        print("Link: " + html.unescape(item_object.link))
        print("Publish Date: " + item_object.pub_date)
        print("********************* \n")


def main():
    validate_input()
    items_objects = get_all_feed()
    print_feed(items_objects)


if __name__ == '__main__':
    main()