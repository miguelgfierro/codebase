from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def create_page_driver(url):
    """Generates the selenium driver to parse a web
    Parameters:
        url (str): URL to parse
    Returns:
        driver (obj): Driver of the web
    Example:
        >>> url = 'http://miguelgfierro.com/'
        >>> driver = create_page_driver(url)
        >>> driver.title
        'Sciblog - A blog designed like a scientific paper'

    """
    #TODO: check other drivers
    driver = webdriver.Safari()
    driver.get(url)
    return driver


def search_form(driver, html_class_form, search_term):
    """Generates the selenium broswer to parse a web
    Parameters:
        driver (obj): driver of the web
        html_class_form (str): html class in form
        search_term (str): Term to search
    Returns:
        driver (obj): driver of the web
    Example:
        >>> driver = create_page_driver('http://miguelgfierro.com/')
        >>> search_form(driver, 'navigation-bar-search-input', 'deep learning')
        >>> driver.current_url
        'https://miguelgfierro.com/search?q=deep+learning'

    """
    element = driver.find_element_by_class_name(html_class_form)
    element.clear()
    element.send_keys(search_term + Keys.RETURN)
    driver.implicitly_wait(10)
