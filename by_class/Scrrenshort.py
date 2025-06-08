from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

class Screenshot:
    def screenshort_take(self):
        driver = webdriver.Chrome()
        driver.get("https://www.makemytrip.com/")
        time.sleep(3)
        driver.maximize_window()

        try:
            driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div[1]/div[2]/div[2]/div/section/form/div[1]/div/input").send_keys("6393873957")
            time.sleep(3)
            continuedemo = driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div[1]/div[2]/div[2]/div/section/form/div[2]/button")
            continuedemo.screenshot(".\\Test.png")
            continuedemo.click()
            time.sleep(3)

            driver.get_screenshot_as_file("C:\\document\\error.png")
            driver.save_screenshot(".\\test1.png")

            print("Screen shot Sucssefully ")
            
        except NoSuchElementException:
            print("Exception is occur")

        finally:
            driver.quit()

k=Screenshot()
k.screenshort_take()