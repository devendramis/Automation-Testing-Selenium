from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

#CSS Selector find using selenium

class sccselector:
    def find_css_selector(self):
        driver = webdriver.Chrome()
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        time.sleep(5)

        try:
            driver.find_element(By.CSS_SELECTOR,"#login-input")
            print("Css Selector is present")
        except NoSuchElementException:
            print("Css Selector is not present")

k=sccselector()
k.find_css_selector()

