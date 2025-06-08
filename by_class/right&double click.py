from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time 

class demo_right:
    def right_click(self):
        driver = webdriver.Chrome()
        driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
        driver.maximize_window()
        time.sleep(3)

        achain = ActionChains(driver)
        element1  = driver.find_element(By.XPATH,"/html/body/div/section/div/div/div/p/span")
        copy = driver.find_element(By.XPATH,"/html/body/ul/li[3]")
        achain.context_click(element1).perform()
        time.sleep(5)
        copy.click()
        time.sleep(3)

k=demo_right()
k.right_click()
