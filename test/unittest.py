from utilizer_selense import utilizer
from selenium import webdriver

driver = webdriver.Chrome('/Users/vganesan/PycharmProjects/nu_tls_automation/drivers/chromedriver')
utilizer.instance(driver)
print(utilizer.get_current_url())