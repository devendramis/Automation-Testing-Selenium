from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

#find element by Xpath using Selenium

class usingxpath:
    def finder(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        time.sleep(5)

        xpath = '//*[@id="login-input"]'

        try:
            element = driver.find_element(By.XPATH,xpath)
            print("Element is found ")
        except NoSuchElementException:
            print("Element not found")

k=usingxpath()
k.finder()
