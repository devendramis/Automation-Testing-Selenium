from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time 

class Radio_Button:
    def check_radio_button(self):
        driver = webdriver.Chrome()
        driver.get("https://demos.jquerymobile.com/1.4.5/checkboxradio-radio/")
        driver.maximize_window()
        time.sleep(3)

        try:
            print(driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/form/div[1]/input").is_selected())
            ID1 = "/html/body/div[1]/div[3]/div[1]/form/div[1]/label"
            driver.find_element(By.XPATH,ID1).click()
            time.sleep(2)
            print(driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/form/div[1]/input").is_selected())

            ID2 = "/html/body/div[1]/div[3]/div[1]/form/div[2]/label"
            driver.find_element(By.XPATH,ID2).click()
            time.sleep(2)
            print(driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/form/div[1]/input").is_selected())

        except NoSuchElementException:
            print("Radio Botton is not Working")

        finally:
            driver.quit()

k=Radio_Button()
k.check_radio_button()
