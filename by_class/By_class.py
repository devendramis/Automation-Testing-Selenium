from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.spirithalloween.com/")
time.sleep(5)

driver.find_element(By.CLASS_NAME,"js-keyword combobox__native-control rfk_sb").click("Search")
