__author__ = "Vivek Ganesan"


from selenium.common.exceptions import WebDriverException,NoSuchElementException
import sys, time, requests
import logging
import configparser
import os


# driver global variable to hold live webdriver instance
driver = None


def instance(drive):
    """
    Get live instance from behave environment.py and assign here.
    :param drive: webdriver instance
    :return: webdriver instance
    """
    logging.info(" <.> - Instantiation of the driver utility class ")
    global driver
    driver = drive
    return driver

def get_project_root():
    """
    To get the project root path
    :return: none
    """
    pgm_dir = os.path.dirname(os.path.abspath(__file__))
    dir_to_rmv = pgm_dir.split(os.sep)[-1]
    pgm_root = pgm_dir.replace(dir_to_rmv, '')
    sys.path.append(pgm_root)
    return sys.path[len(sys.path)-1]

def ini_reader(context,key):
    """
    To read the ini file value
    :param context: behave object
    :param key: value that to be fetched from ini
    :return: value for the given key
    """
    parser = configparser.ConfigParser()
    __ini_path = get_project_root()+"framework.ini"
    parser.read(__ini_path)
    if str(parser[context.Instance][key]).strip() is not None:
        return str(parser[context.Instance][key]).strip()
    else:
        try:
            raise AttributeError('ini file key - {} returned None'.format(key))

        except Exception as error:
            logging.info('Caught this error: ' + repr(error))
            logging.info(' << None value in INI file >> ')


def active_driver_instance():
    """
    Return active web driver instance
    :return: web driver object
    """
    return driver


def open_url(url):
    """
    Method to open the url in browser
    :param url: url
    :return: none
    """
    logging.info(" <.> - open_url Method({})".format(url))
    driver.get(url)
    logging.info(" <.> - Opening url")

def navigate_to(url):
    """
    Method to open the url in browser
    :param url: url
    :return: none
    """
    driver.get(url)

def get_title():
    """
    Method to get web page title
    :return: title
    """
    logging.info(" <.> - Getting title of the current page")
    title = str(driver.title).replace('\u2013', '')
    logging.info(" <.> - Current page title - {}".format(title))
    return title


def get_current_url():
    """
    Method to get the active url of web page
    :return: current url
    """
    logging.info(" <.> - Getting current url of the page")
    return driver.current_url

def dom_locator(location, locator):
    """
    Method to identify element in the web page
    :param location: locator type
    :param locator: DOM element identifier
    :return: web element
    """
    logging.info(" <.> - dom_locator Method - ({}) - ({})".format(location,locator))
    location = location.lower()
    try:
        if location == "xpath":
            logging.info(" <.> - XPATH identifier")
            return driver.find_element_by_xpath(locator)
        elif location == "css":
            logging.info(" <.> - CSS identifier")
            return driver.find_element_by_css_selector(locator)
        elif location == "id":
            logging.info(" <.> - ID identifier")
            return driver.find_element_by_id(locator)
        elif location == "name":
            logging.info(" <.> - NAME identifier")
            return driver.find_element_by_name(locator)
        elif location == "class":
            logging.info(" <.> - CLASS identifier")
            return driver.find_element_by_class_name(locator)
        elif location == "linktext":
            logging.info(" <.> - LINK TEXT identifier")
            return driver.find_element_by_link_text(locator)
        elif location == "partiallinktext":
            logging.info(" <.> - PARTIAL LINK TEXT identifier")
            return driver.find_element_by_partial_link_text(locator)
    except (WebDriverException, NoSuchElementException):
        print("< //"+("."*15)+"Exception <")
        print(" * - {}".format(sys.exc_info()[1]))
        print("> "+("."*25)+" <")
        assert True == False, "Exception has occur in dom_locator()"


def list_dom_locator(location, locator):
    """
    Method to locate list of web element
    :param location: locator type
    :param locator: DOM
    :return: web element <list>
    """
    location = location.lower()
    try:
        if location == "xpath":
            return driver.find_elements_by_xpath(locator)
        elif location == "css":
            return driver.find_elements_by_css_selector(locator)
        elif location == "id":
            return driver.find_elements_by_id(locator)
        elif location == "name":
            return driver.find_elements_by_name(locator)
        elif location == "class":
            return driver.find_elements_by_class_name(locator)
        elif location == "linktext":
            return driver.find_elements_by_link_text(locator)
        elif location == "partiallinktext":
            return driver.find_elements_by_partial_link_text(locator)
    except (WebDriverException, NoSuchElementException):
        print("< //" + ("." * 15) + "Exception <")
        print(" * - {}".format(sys.exc_info()[1]))
        print("> " + ("." * 25) + " <")
        assert True == False, "Exception has occured in list_dom_locator()"


def set_maximize():
    """
    Method to get maximum size
    :return: none
    """
    logging.info(" <.> - Maximizing browser window")
    driver.maximize_window()


def go_back():
    """
    Method to navigate back
    :return: none
    """
    driver.back()


def go_forward():
    """
    Method to navigate forward
    :return: none
    """
    driver.forward()


def __page_element_validator(webelement):
    """
    Method to validate the element
    :param webelement: webelement
    :return: webelement
    """
    if webelement is None:
        assert True==False, "Page element returned NULL/NONE"
    else:
        return webelement


def type_on(location, locator, word):
    """
    Method to perform type / sendkeys to web element
    :param location: locator type
    :param locator: DOM
    :param word: text to be entered
    :return: none
    """
    temp_element = dom_locator(location, locator)
    temp_element.send_keys(word)


def type_on_element(webelement, word):
    result = __page_element_validator(webelement)
    if result is not None and word is not None:
        webelement.send_keys(word)
    else:
        try:
            raise AttributeError('Value returned from page object is None')
        except Exception as error:
            logging.info(' << Caught this error: >>' + repr(error))


def click_on(location, locator):
    """
    Method to click on web element
    :param location: locator
    :param locator: DOM
    :return: none
    """
    temp_element = dom_locator(location, locator)
    temp_element.click()


def click_on_element(webelement):
    """
    Method to click on web element
    :param webelement: web element
    :return: none
    """
    logging.info(" <.> - Clicking on the webelement")
    webelement.click()

def get_hyper_links(location, locator):
    """
    Method to get http hyper links
    :param location: locator
    :param locator: DOM
    :return: href hyper link
    """
    temp_list = list_dom_locator(location, locator)
    href = []
    for x in temp_list:
        href.append(x.get_attribute("href"))
    return href


def time_elapsed(sec):
    """
    Method to wait for web element
    :param sec: second
    :return: none
    """
    logging.info(" <.> - Wait for {} second".format(sec))
    time.sleep(sec)


def get_http_response(url):
    """
    Method to get http response for given url
    :param url: url
    :return: status code , response time
    """
    try:
        logging.info(" <.> - Calling http service {}".format(url))
        r = requests.get(url, timeout=15,verify=False)
        respTime = str(round(r.elapsed.total_seconds(), 2))
        logging.info(" <.> - STATUS CODE : {} || RESPONSE TIME : {}".format(r.status_code,respTime))
        #logging.info(" <.> - STATUS CODE : {}".format(r.status_code))
        #logging.info(" <.> - Response time of {} website - {}".format(url,respTime))
        return r.status_code,respTime
    except Exception:
        logging.info(" <.//\... EXCEPTION ...//\.>")
        logging.info("Reason : {}".format(sys.exc_info()[1]))
        logging.info("Method : {}".format("get_http_reponse(url)"))
        assert True == False, "get_http_response method failed due to exception - {}".format(sys.exc_info()[1])


def get_text(location, locator):
    """
    Method to get text from DOM element
    :param location: locator type
    :param locator: DOM
    :return: text of outer html
    """
    temp_ele = dom_locator(location, locator)
    return temp_ele.text


def close_current_window():
    """
    Method to close current window
    :return: none
    """
    driver.close()


def close_driver_instance():
    """
    Method to kill instance of web driver
    :return: none
    """
    driver.quit()


def refresh_page():
    """
    Method to refresh the page
    :return: none
    """
    logging.info(" <.> - Browser refreshing ")
    driver.refresh()
    driver.time_elapsed(2)

