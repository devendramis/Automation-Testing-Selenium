from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time 

class dropdown_list:
    def check_check_dropdown_list(self):
        driver = webdriver.Chrome()
        driver.get("https://getbootstrap.com/docs/5.3/components/dropdowns/")
        driver.maximize_window()
        time.sleep(3)

        try:
            dropdown = driver.find_element(By.CLASS_NAME,"Dropdown button").is_selected()
            dd = Select(dropdown)

            dd.select_by_index(1)
            time.sleep(2)

            dd.select_by_visible_text("Action")

            # dd.select_by_value("")

        
        except NoSuchElementException:
            print("Radio Botton is not Working")

        finally:
            driver.quit()

k=dropdown_list()
k.check_check_dropdown_list()