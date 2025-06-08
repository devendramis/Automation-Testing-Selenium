from selenium import webdriver
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome()
driver.get("https://selenium-python.readthedocs.io/installation.html")
try:
    k = driver.find_element(By.NAME, "installation")
    print("Element found:", k)
except Exception as e:
    print("Element not found:", e)

time.sleep(10)

