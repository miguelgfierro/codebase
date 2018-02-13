
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def create_page_browser(url):
    """Generates the selenium broswer to parse a web
    Parameters:
        url (str): URL to parse
    Returns:
        browser (obj): Browser of the web
    Example:
        >>> url = 'http://miguelgfierro.com/'
        >>> browser = create_page_browser(url)
        >>> browser.title
        'Sciblog - A blog designed like a scientific paper'

    """
    #TODO: check other drivers
    browser = webdriver.Safari()
    browser.get(url)
    return browser



