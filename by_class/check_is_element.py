from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time 

class check_element:
    def check_element_condition(self):
        driver = webdriver.Chrome()
        driver.get("https://www.facebook.com/instagram/")
        time.sleep(4)

        try:
            xpath1 = "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[4]/div/div/label/div/input"
            xpath2 = "/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[5]/div/div/label/div/input"
            driver.find_element(By.XPATH,xpath1).send_keys("7309606029")
            time.sleep(3)
            driver.find_element(By.XPATH,xpath2).send_keys("babashiv")
            time.sleep(3)
            elemet = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div[5]/div/div/div[1]/div/div[2]/div/div/div/div[2]/form/div/div[6]/div/div").is_enabled()
            print(elemet)

        except NoSuchElementException:
            print("It Does not enables")

k = check_element() 
k.check_element_condition()