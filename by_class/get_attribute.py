from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time 

class check_attribute:
    def get_attribute(self):
        driver = webdriver.Chrome()
        driver.get("https://www.googleadservices.com/pagead/aclk?sa=L&ai=DChcSEwiZ16DX2_2MAxXwo2YCHe6EJOEYABA2GgJzbQ&co=1&gclid=Cj0KCQjw8cHABhC-ARIsAJnY12xI7Qe2mdWfvwIkOaba-gClJhqVGxaGp_4u8t0y-qVVc7rEouIidyUaAhIXEALw_wcB&ohost=www.google.com&cid=CAESVuD2Dscw7E0sWTrEWlyWp4UG8u0WzSzDPx6YerfBVf2-QgsRwps2dvmUyFbsyh-Vrq5ts2Wt68bWT_AMXEhqfC65fSXcXq8fLNmiMC96ybQExo4cHvh-&sig=AOD64_3eO3_MpzOHxOYWCMr8W3ctMgBKTg&q&adurl&ved=2ahUKEwi6xZzX2_2MAxVayzgGHRttHxcQ0Qx6BAgOEAE")
        time.sleep(4)

        element = "//body/script[1]"

        try:
            value = driver.find_element(By.XPATH,element)
            value_print = value.get_attribute("src")
            print("These Value is present in website ",value_print)

        except NoSuchElementException:
            print("No href tag is present in website")

k=check_attribute()
k.get_attribute()