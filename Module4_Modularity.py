#!/usr/bin/env python3
"""Pluralsight Module 4 thing

Usage: py Module4_Modularity <URL>
"""


import sys
from urllib.request import urlopen


def get_items_from_url(url):
    """Fetch a list of words from a URL.
    Args:
        url: The url of  a UTF-8 text document

    Returns:
        A list of string containing the words from the document
    """
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
        return story_words


def print_items(items):
    """Prints a list of items
        Args:
            items: The list of items(iterable)

        Returns:
            None
        """
    for word in items:
        print(word)


def main(url):
    """Prints each word from a text document from a URL
    Args:
        url: The url of  a UTF-8 text document

    Returns:
        None
    """
    result = get_items_from_url(url)
    print_items(result)


#this is how we can execute our function as a script
if __name__=='__main__':
    main(sys.argv[1])
