__author__ = "Vivek Ganesan"
__copyright__ = "Specialist titles"
__email__ = "vivek.ganesan@ntsindia.co.uk"

"""
This environment.py offers dependent functions to behave.Utilized before any BDD feature file executes via
behave framework.
"""

from selenium import webdriver
import logging
import requests
from datetime import datetime
import configparser
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
from utilizer_selense import utilizer
import platform

def _config_parser(context):
    """
    Method to read .ini file and store it as {key,pair} values
    :param context: Behave framework object variable
    :return: none
    """
    context.parser = configparser.ConfigParser()
    __ini_path = utilizer.get_project_root() + "framework.ini"
    try:
        context.parser.read(__ini_path)
    except Exception:
        print(" <../\\ framework.ini file not found ../\\>")
        assert False , "framework.ini file not found .."
    context.env_var = {}  # variable to store all the ini file properties,Shared across the framework
    for section in context.parser.sections():
        for x, y in context.parser.items(section):
            context.env_var[x.upper()] = y
    # Variable to hold the instance info - will be from -D instance=option | option is from jenkins pipeline
    context.instance = str(context.config.userdata['instance']).upper()

def _log_config(logfile):
    """
    logger configuration,create a log file,config to console and file
    :param logfile: name for logfile
    :return: none
    """
    __logname = "{}.log".format(logfile.lower())
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(name)-5s [%(levelname)-s]: * - %(message)s',
                        datefmt='%m-%d %H:%M:%S',
                        filename=__logname,
                        filemode='w')
    console = logging.StreamHandler()  # define a Handler which writes INFO messages to console
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)-8s %(message)s')
    console.setFormatter(formatter)  # Tell the handler to use this format
    logging.getLogger('').addHandler(console)      # add the handler to the root logger
    logging.info('''
 ____                          _           _   _         _     _____   _   _     _        
/ ___|   _ __     ___    ___  (_)   __ _  | | (_)  ___  | |_  |_   _| (_) | |_  | |   ___ 
\___ \  | '_ \   / _ \  / __| | |  / _` | | | | | / __| | __|   | |   | | | __| | |  / _ \\
 ___) | | |_) | |  __/ | (__  | | | (_| | | | | | \__ \ | |_    | |   | | | |_  | | |  __/
|____/  | .__/   \___|  \___| |_|  \__,_| |_| |_| |___/  \__|   |_|   |_|  \__| |_|  \___| 'S
        |_|                                                                               
        ''')
    logging.info(" <<<<<<<<<<< SETTING UP LOG >>>>>>>>>>>>>")


def _application_log(context, logfile):
    """
    Just for application information to be logged on reporting
    :param context: Behave object holder variable
    :param logfile: log file name
    :return: none
    """
    logging.info("{}".format("*" * 83))
    logging.info("* - *-                                  {}".format(context.env_var.get("APPLICATION_NAME")))
    logging.info("{}".format("*" * 83))
    logging.info("DATED : {}".format(datetime.now().strftime("%x") + " - " + datetime.now().strftime("%c")))
    logging.info("{}".format("^" * 75))
    logging.info(" * - Setting up the logger : Location - {}.log".format(logfile.lower()))


def _sauce_lab(context):
    """
    For cloud sauce lab integration
    :param context: Behave object holder variable
    :return: none
    """
    logging.info("Triggering Sauce lab")
    desired_cap = {
        'platform': "Mac OS X 10.9",
        'browserName': "chrome",
        'version': "31",
    }
    context.driver = webdriver.Remote(
        command_executor='http://viveknts:6892bd79-c34e-4e3d-9de0-a678cf2dd4d4@ondemand.saucelabs.com:80/wd/hub',
        desired_capabilities=desired_cap)

def _environment_config(context):
    """
    For setting up automation environment to be used for test execution.
    :param context: Behave object holder variable
    :return: none
    """
    logging.info("")
    logging.info(" <<<<<<<<<<< SETTING UP AUTOMATION ENVIRONMENT >>>>>>>>>>>>>")
    device_stack = context.env_var.get("DEVICE")
    logging.info(" * - Setting up the device platform - {}".format(device_stack))
    logging.info(" * - Setting up the web driver instance")

    # Setting up the driver executable based on OS running
    # exe_path = "drivers/mac/chromedriver" if 'Darwin'in str(platform.platform()) else "drivers/chromedriver"
    exe_path = "drivers/chromedriver"

    if device_stack == "Mobile":
        logging.info(" * - Mobile emulator - Pixel 2")
        # Define mobile emulator model
        mobile_emulation = {"deviceName": "Pixel 2"}
        # Define a variable to hold all the configurations we want
        chrome_options = webdriver.ChromeOptions()
        # Add the mobile emulation to the chrome options variable
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        # Create driver, pass it the path to the chromedriver file and the special configurations you want to run
        logging.info(" * - Setting up chrome for mobile environment")
        try:
            context.driver = webdriver.Chrome(
                executable_path="drivers/chromedriver",
                options=chrome_options)
        except Exception:
            logging.info(" * - < ..... Exception : unable to config chrome driver ")
            logging.info(" * - <.....> - {}".format(sys.exc_info()[1]))
            assert False, "Issue in Chrome driver"

    elif device_stack == "Website":
        # Browser driver configuration
        browser_stack = context.env_var.get("BROWSER").upper()
        logging.info(" * - BROWSER DEFINED : {}".format(browser_stack))

        if browser_stack == "GC" or browser_stack == "GOOGLECHROME" or browser_stack == "CHROME":
            logging.info(" * - Configuring Google Chrome driver ")
            try:
                #context.driver = webdriver.Chrome(executable_path="drivers/chromedriver")
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--no-sandbox')
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
                chrome_options.add_argument("--disable-extensions")
                chrome_options.addArguments("--disable-dev-shm-usage")
                capabilities = chrome_options.to_capabilities()
                context.driver = webdriver.Remote(
                    command_executor='http://localhost:4444/wd/hub',
                    desired_capabilities=capabilities)
                #context.driver = webdriver.Chrome(executable_path="drivers/chromedriver", options=chrome_options)
                context.driver.set_page_load_timeout(20)
            except Exception:
                logging.info(" * - < ..... Exception : unable to config chrome driver ")
                logging.info(" * - <.....> - {}".format(sys.exc_info()[1]))
                assert False, "Issue in Chrome driver"
        elif browser_stack == "FF" or browser_stack == "FIREFOX" or browser_stack == "MORZILLAFIREFOX":
            logging.info(" * - Configuring Firefox driver .")
            caps = DesiredCapabilities.FIREFOX
            #caps["pageLoadStrategy"] = "normal"  # complete
            caps["pageLoadStrategy"] = "eager"  #  interactive
            #caps["pageLoadStrategy"] = "none"
            try:
                context.driver = webdriver.Firefox(capabilities=caps)
            except Exception:
                logging.info(" * - < ..... Exception : unable to config Firefox driver ")
                logging.info("<.....> - {}".format(sys.exc_info()[1]))
                assert False , "Issue in firefox driver"
        elif browser_stack == "SAFARI":
            try:
                logging.info(" * - Configuring Safari driver .")
                context.driver = webdriver.Safari()
            except Exception:
                logging.info(" * - < ..... Exception : unable to config safari driver ")
                logging.info("<.....> - {}".format(sys.exc_info()[1]))
                assert False, "Issue in chrome driver"

    else:
        logging.info(" * - Configuring Firefox driver ")
        caps = DesiredCapabilities.FIREFOX
        # caps["pageLoadStrategy"] = "normal"  # complete
        caps["pageLoadStrategy"] = "eager"  # interactive
        # caps["pageLoadStrategy"] = "none"
        try:
            context.driver = webdriver.Firefox(capabilities=caps)
        except Exception:
            logging.info(" * - < ..... Exception : unable to config Firefox driver ")
            logging.info("<.....> - {}".format(sys.exc_info()[1]))
            assert False, "Issue in firefox driver"


def _app_specific_config(context):
    """
    Text application specific configuration to be logged in report
    :param context: Behave object variable
    :return: none
    """
    logging.info("")
    logging.info(" <<<<<<<<<<< SETTING UP FRAMEWORK PARAMETER >>>>>>>>>>>>>")
    context.TIME = context.env_var.get("SLEEP")
    logging.info(" * - App Name : {}".format(context.env_var['APPLICATION_NAME']))
    context.url = context.parser[context.instance]['URL']
    logging.info(" * - App URL : {}".format(context.url))
    logging.info(" * - Browser : {}".format(context.env_var['BROWSER']))
    logging.info(" * - Device : {}".format(context.env_var['DEVICE']))
    logging.info(" * - Time defined for lazy loading : {}".format(context.TIME))
    logging.info("")


def _driver_utility(context):
    """
    This serves for creating object for driver utility class which in turn creates webdriver instance.
    :param context: Behave object variable
    :return: None
    """
    utilizer.instance(context.driver)
    utilizer.open_url(context.url)
    utilizer.set_maximize()
    # Verifying the URL:
    logging.info(" * - Verify the http of URL")
    req = requests.get(context.url)
    logging.info(" STATUS CODE : {}".format(req.status_code))

    if int(req.status_code) is not int(200):
        try:
            logging.info("Raising exception since url is throwing {}".format(req.status_code))
        except Exception:
            logging.info("< . /\\ Exception .. >")
            logging.info("REASON: URL {} is throwing {} status code".format(context.url, req.status_code))
            assert False,"Please check the URL"


def before_all(context):
    """
    Initial runner method for behave framework.
    :param context: Behave object holder
    :return: none
    """
    _config_parser(context)
    _log_config(context.env_var.get("APPLICATION_NAME"))
    _application_log(context,context.env_var.get("APPLICATION_NAME"))
    #_sauce_lab(context)
    _environment_config(context)
    _app_specific_config(context)
    _driver_utility(context)


def before_feature(context,feature):
    """
    Runs before all feature to log feature name
    :param context: Behave variable
    :param feature: Behave variable
    :return: none
    """
    logging.info(" ")
    logging.info("{}".format("^" * 75))
    logging.info("FEATURE - {}".format(feature.name))
    logging.info("{}".format("^" * 75))
    logging.info(" ")


def before_scenario(context,scenario):
    """
    Runs before all scenario to log scenario name
    :param context: Behave variable
    :param scenario: Behave variable
    :return: none
    """
    logging.info("{}".format("*" * 75))
    logging.info("SCENARIO - {}".format(scenario.name))
    logging.info("{}".format("*" * 75))
    logging.info(" ")
    # re opening url again before all the scenario so that any test will start from home page
    utilizer.open_url(context.url)



def after_scenario(context,scenario):
    """
    Runs after all scenario to log scenario status
    :param context: Behave variable
    :param scenario: Behave variable
    :return: none
    """
    logging.info("{}".format("*" * 75))
    STATUS = "PASS" if "passed" in str(scenario.status) else "FAIL"
    logging.info("{} : {}".format(scenario.name, STATUS))
    logging.info("{}".format("*" * 75))
    logging.info(" ")


def before_step(context,step):
    """
    Runs before all steps to log step name
    :param context: Behave variable
    :param step: Behave variable
    :return: none
    """
    logging.info("STEP : {}".format(step.name))
    logging.info(" ")


def after_step(context,step):
    """
    Runs after all steps to log step status
    :param context: Behave variable
    :param step: Behave variable
    :return: none
    """
    logging.info("")
    STATUS = "PASS" if "passed" in str(step.status) else "FAIL"
    logging.info("---------------------------- STEP : {} - {} ".format(step.name,STATUS))
    #logging.info("{}".format("-"*75))
    logging.info("")


def after_all(context):
    """
    Runs after everything is completed.To close web driver instance and send email
    :param context: Behave variable
    :return: none
    """
    logging.info("")
    logging.info("----------------------------------------- THE END -----------------------------------------------------------")
    logging.info("@@@ - Closing driver instance")
    context.driver.close()
    #if context.env_var.get("EMAIL_NOTIFICATION").lower() != "no":
        # logging.info(" <<< SENDING EMAIL >>")
        # context.utility.send_email("@gmail.com","@gmail.com","StylePlay","styleplay.log")
        # logging.info("Email has been sent.")
    context.driver.quit()
    logging.info("Bye.")