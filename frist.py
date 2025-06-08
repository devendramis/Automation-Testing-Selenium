from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up the driver (assuming Chrome)
driver = webdriver.Chrome()  # or use a path to chromedriver if not in PATH

# Open Google
driver.get("https://www.google.com")

# Find the search box
search_box = driver.find_element(By.NAME, "q")

# Type in the search query
search_box.send_keys("xnxx")

# Press Enter
search_box.send_keys(Keys.RETURN)

# Wait for results to load
#time.sleep(2)

# Get titles of search results
results = driver.find_elements(By.CSS_SELECTOR, 'h3')
for idx, result in enumerate(results[:5], start=1):  # Limit to first 5
    print(f"{idx}. {result.text}")

# Close the browser
time.sleep(10)
