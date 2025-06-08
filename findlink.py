from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time 

class findlink:
    def findlinkelement(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        time.sleep(5)

        xpath = "/html/body/div[1]/div/div[1]/div[1]/div[1]/div[2]/div[3]/p/span/span"

        try:
            driver.find_element(By.XPATH,xpath).click()
            print("Link is present in the page ")
        except NoSuchElementException:
            print("No link present in the home page")

p=findlink()
p.findlinkelement()