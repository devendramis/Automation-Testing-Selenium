from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

class ifram():
    def handle_ifram(self):
        driver = webdriver.Chrome()
        driver.get("https://www.geeksforgeeks.org/html-iframes/")
        time.sleep(3)

        try:
            driver.find_element(By.XPATH,"/html/body/div/form/button[1]/h3").click()

        except NoSuchElementException:
            print("Error is occure")

        finally:
            driver.quit()

k = ifram()
k.handle_ifram()