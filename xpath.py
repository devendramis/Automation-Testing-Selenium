from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome() 
url = driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
time.sleep(10)

xpath = '//*[@id="login-input"]'

try:
    element = driver.find_element(By.XPATH, xpath)
    print("Element found!")
except NoSuchElementException:
    print("Element not found.")

# Close the browser
driver.quit()
