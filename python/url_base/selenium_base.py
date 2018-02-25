from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


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
        driver (obj): Driver of the web
        html_class_form (str): HTML class in form
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
    driver.get(driver.current_url) #put driver in current page


def screenshot(driver, path='', filename='page.png'):
    """Save a screenshot of the current page.
    Parameters:
        driver (obj): Driver of the web
        path (str): Path to file
        filename (str): Filename
    Example:
        >>> driver = create_page_driver('http://miguelgfierro.com/')
        >>> screenshot(driver, filename='mig.png')

    """
    driver.get_screenshot_as_file(os.path.join(path, filename))


def find_element(driver, value, selector_type='class'):
    """Find an element using a selector
    Parameters:
        driver (obj): Driver of the web.
        value (str): Value to find.
        selector_type (str): Selector type. Valid arguments are 'class', 'id', 'tag',
                            'name', 'link_text', 'partial_link_text', 'css' or 'xpath'.
    Returns:
        driver (obj): driver of the web
    Example:
        >>> driver = create_page_driver('https://miguelgfierro.com/blog/2017/a-gentle-introduction-to-transfer-learning-for-image-classification/')
        >>> element = find_element(driver, 'title', 'class')
        >>> element.text
        ' A Gentle Introduction to Transfer Learning for Image Classification'

    """
    selector_dict = {'class': By.CLASS_NAME,
                     'id': By.ID,
                     'tag': By.TAG_NAME,
                     'name': By.NAME,
                     'link_text': By.LINK_TEXT,
                     'partial_link_text': By.PARTIAL_LINK_TEXT,
                     'css': By.CSS_SELECTOR,
                     'xpath': By.XPATH}
    if selector_type not in selector_dict:
        raise ValueError("Selector type '{}' not in {}".format(selector_type, list(selector_dict.keys())))
    try:
        by_func = selector_dict[selector_type]
        element = driver.find_element(by=by_func, value=value)
    except NoSuchElementException as e:
        print("Element {} not found".format(value))
        raise e
    return element
