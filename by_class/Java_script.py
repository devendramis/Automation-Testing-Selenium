from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

class javascrip:
    def javascrip_run(self):
        try:
            driver = webdriver.Chrome()
            driver.execute_script("window.open('https://careers.wipro.com/content/Early-Careers/?locale=en_US')")
            driver.maximize_window()
            time.sleep(5 )
            print("Program is running successfuly")

        except NoSuchElementException:
            print("Error is occer in this program")

        finally:
            driver.quit()

k=javascrip()
k.javascrip_run()
