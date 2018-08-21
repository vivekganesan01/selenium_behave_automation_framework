__author__ = "Vivek Ganesan"
__copyright__ = "Specialist titles"
__email__ = "vivek.ganesan@ntsindia.co.uk"
__version__ = "1.0.1"


from selenium.common.exceptions import WebDriverException,NoSuchElementException,ElementNotVisibleException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import sys, time, requests
import logging
import configparser
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# driver global variable to hold live web driver instance
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
    if str(parser[context.instance][key]).strip().upper() is not None:
        return str(parser[context.instance][key]).strip()
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
    logging.info(" <.> - open_url Method : ({})".format(url))
    driver.get(url)
    logging.info(" <.> - Opening the url")

def navigate_to(url):
    """
    Method to open the url in browser
    :param url: url
    :return: none
    """
    logging.info(" <.> - Navigating to url : ({})".format(url))
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

def validate_page_title(expected_title):
    """
     Method the validate the title of the page in order to make sure we are in the right page
    :param expected_title: title to be validated
    :return: none
    """
    actual = get_title()
    logging.info(" <.> - Expected title - {}".format(expected_title))
    assert str(actual).lower() == str(expected_title).lower() , "Actual title is not equal to expected title"


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
        assert True == False, "Exception has occurred in list_dom_locator()"


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


def page_element_validator(webelement,stringvalue = ""):
    """
    Method to validate the element
    :param webelement: webelement
    :return: webelement
    """
    locator = stringvalue if stringvalue!="" or stringvalue else "on page"
    logging.info(" <.> - Validating presence of element : {}".format(locator))
    if webelement is None:
        logging.info(" <.> - Element {} Not Found: Returning Assertion error".format(locator))
        logging.info(" <.//\... Exception: ...//\.> ")
        logging.info("\n******* \nReason : {} \n*******".format("Element from page object return Nonetype"))
        assert True==False, log_it(" * - Please check your locator/xpath - {}".format(webelement))
    else:
        logging.info(" <.> - Element present : Returning : {}".format(locator))
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
    """
    Method to perform type / sendkeys to web element
    :param webelement: DOM
    :param word: value to be entered
    :return: none
    """
    result = page_element_validator(webelement)
    if result is not None and word is not None:
        webelement.send_keys(word)
    else:
        try:
            raise AttributeError('Value must be passed to type inside the web element')
        except Exception:
            logging.info(" <.//\... Exception : send keys operation FAILED ...//\.> ")
            logging.info("\n******* \nReason : {} \n*******".format(sys.exc_info()[1]))
            logging.info("Failed Method : {}".format("type_on_element(webelement, word)"))
            assert True == False, log_it("click_on_element method failed due to exception - {}".format(sys.exc_info()[1]))


def click_on(location, locator):
    """
    Method to click on web element
    :param location: locator
    :param locator: DOM
    :return: none
    """
    temp_element = dom_locator(location, locator)
    temp_element.click()


def click_on_element(webelement = None,stringvalue = None):
    """
    Method to click on web element
    :param webelement: web element
    :return: none
    """
    result = page_element_validator(webelement,stringvalue)
    try:
        element_name = stringvalue if stringvalue else ""
        logging.info(" <.> - Clicking on element = {}".format(element_name))
        result.click()
    except Exception:
        logging.info("")
        logging.info(" <.//\... Exception : Click operation FAILED ...//\.> ")
        logging.info("\n******* \nReason : {} \n*******".format(sys.exc_info()[1]))
        logging.info("Failed Method : {}".format("click_on_element(webelement)"))
        assert True == False, "click_on_element method failed due to exception - {}".format(sys.exc_info()[1])


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

def get_text_webelement(webelement):
    """
    Getting outer html text from DOM
    :param webelement: DOM
    :return: string text
    """
    text = webelement.text
    if text is not None or "":
        return text
    else:
        try:
            raise WebDriverException()
        except Exception:
            logging.info(" <.> - Get text method returned None")
            logging.info("Method : get_text_webelement(webelement)")
            assert True == False, "No text present in the outer html"


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


def visibility_of_ele_located(webelement,locatorname):
    """
    Method to check the presence of element in current page and also its height and
    width is not less than or equal to zero
    :param webelement: locator
    :return: element
    """
    logging.info(" <.> - Verifying visibility of element : {}".format(locatorname))
    try:
        wait = WebDriverWait(driver, 7)
        element = wait.until(expected_conditions.visibility_of(webelement))
        return element
    except Exception:
        logging.info(" <.> - Element not visible exception")
        logging.info("Reason : {}".format(sys.exc_info()[1]))
        logging.info("Method : {}".format("visibility_of_ele_located({})".format(locatorname)))
        assert True == False, log_it("Assertion Error : Element not visible")


def verify_text_present(webelement,text):
    """
    Method to verify text present in the DOM
    :param webelement: DOM
    :param text: string to be verified
    :return: none
    """
    logging.info(" <.> - Verify the presence of text : {}".format(text))
    visibility_of_ele_located(webelement,text)
    text_webelement = get_text_webelement(webelement)
    logging.info(" <.> - Actual Value : {}".format(text_webelement.upper()))
    logging.info(" <.> - Expected Value : {}".format(text.upper()))
    assert str(text_webelement).lower() == str(text).lower() , log_it("Given text not matching with DOM text on webelement")
    logging.info(" <.> - Text matches , Looks Good !!")

def element_should_not_visible(webelement):
    """
    Method to make sure element not present in the DOM
    :param webelement: DOM
    :return: webelement/None
    """
    logging.info(" <.> - verify Element should not be visible")
    if webelement is None:
        logging.info(" * - Element not available in the page")
        return None
    else:
        logging.info(" * - Looks like element is visible in the page")
        try:
            wait = WebDriverWait(driver, 7)
            element = wait.until(expected_conditions.visibility_of(webelement))
            return element
        except ElementNotVisibleException:
            logging.info(" <.> - Element not visible exception")
            logging.info("Reason : {}".format(sys.exc_info()[1]))
            logging.info("Method : {}".format("element_should_not_visible(webelement)"))
            return None


def perform_enter():
    """
    To perform key board enter
    :return: none
    """
    ActionChains(active_driver_instance()).send_keys(Keys.ENTER).perform()


def double_click(webelement):
    """
    To perform double click on particular element
    :param webelement: DOM element
    :return: none
    """
    ActionChains(active_driver_instance()).double_click(webelement).perform()


def log_it(st):
    """
    Just for logging at time of assertion
    :param st:
    :return:
    """
    logging.info(" <.> -  Assertion Error")
    logging.info("REASON : {} ".format(st))


def scroll_to_height(height):
    """
    Scroll to given height
    :param height: int height
    :return: none
    """
    logging.info(" <.> - Scrolling page to height - {}".format(height))
    ht = int(height)
    d = active_driver_instance()
    d.execute_script("window.scrollTo(0, {});".format(ht))


def scroll_to_bottom():
    """
    scroll to end of the page
    :return: none
    """
    logging.info(" <.> - Scrolling to bottom")
    d = active_driver_instance()
    d.execute_script("window.scrollTo(0, document.body.scrollHeight);")


def move_to_element_click(webelement):
    """
    Move to given web element and perform click
    :param webelement: DOM
    :return: none
    """
    logging.info(" <.> - Mouse over to element and perform clicking")
    ActionChains(active_driver_instance()).move_to_element(webelement).click().perform()



def move_to_element(webelement):
    """
    Move to given web element
    :param webelement: DOM
    :return: none
    """
    logging.info(" <.> - Mouse over to element")
    ActionChains(active_driver_instance()).move_to_element(webelement).perform()