from sys import executable
from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
# Adding headless option to keep Heroku from opening an actual browser
chrome_options.add_argument("--headless")
# Writes shared memory into /tmp instead of /dev/shm
chrome_options.add_argument("--disable-dev-shm-usage")
# Sandbox is a feature that only exists on actual Chrome browsers
chrome_options.add_argument("--no-sandbox")
# Heroku environment variables
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), 
                          chrome_options=chrome_options)

driver.get("https://www.juniorminingnetwork.com/")

print(driver.page_source)

driver.quit()

print("Finished!")