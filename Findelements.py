from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time 

class finedelements:
    def fineelemnets(self):
        driver = webdriver.Chrome()
        driver.get("https://unstop.com/blog/deloitte-nla-2025-preparation")
        #driver.fullscreen_window()
        driver.maximize_window()
        time.sleep(4)

        try:
            list1 = driver.find_elements(By.TAG_NAME,"a")
            list2 = driver.find_elements(By.CSS_SELECTOR,".login_btn")
            for i in list1:
                print(i.text)
            print("total ancure tag in ligin button",len(list1))
            print("css selector is present in login button",len(list2))

        except NoSuchElementException:
            print("There is no element found in login botton")

class findtext:
    def all_text_in_ancure(self):
        driver=webdriver.Chrome()
        driver.get("https://www.spirithalloween.com/")
        time.sleep(3)

        try:
            list3 = driver.find_elements(By.TAG_NAME,"a")
            for i in list3:
                print(i.text)

        except NoSuchElementException:
            print("No one text is their i this page")

k=finedelements()
#p=findtext()
k.fineelemnets()
#p.all_text_in_ancure()
