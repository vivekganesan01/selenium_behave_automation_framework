from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--no-sandbox')
#chrome_options.add_argument('--headless')
#chrome_options.add_argument('--disable-gpu')
#chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--disable-dev-shm-usage")
capabilities = chrome_options.to_capabilities()
driver = webdriver.Remote(
                    command_executor='http://localhost:4444/wd/hub',
                    desired_capabilities=capabilities)
driver.get("http://anthillpro.newsint.co.uk/")
driver.close()
driver.quit()