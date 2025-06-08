from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.select import Select

class DemoDropdownMultiSelect():
    def demo_dropdoen(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select_multiple")
        driver.maximize_window()
        time.sleep(2)

        dd_demo = driver.find_element(By.ID,"cars")
        dd_multi = Select(dd_demo)
        
        dd_multi.select_by_index(1)
        dd_multi.select_by_value("saab")
        dd_multi.select_by_visible_text("Opel")
        time.sleep(10)


k=DemoDropdownMultiSelect()
k.demo_dropdoen