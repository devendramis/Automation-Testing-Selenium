from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

class IsDisplay:
    def is_displayed(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/HOWTO/howto_js_toggle_hide_show.asp")
        time.sleep(3)

        try:
            element = driver.find_element(By.XPATH, "//button[normalize-space()='Toggle Hide and Show']")
            element1 = driver.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div[1]/div[1]/div[3]")

            print("Is displayed:", element.is_displayed(),element1.is_displayed())

        except NoSuchElementException:
            print("Element not found.")
        finally:
            driver.quit()

# To run the method:
check = IsDisplay()
check.is_displayed()
