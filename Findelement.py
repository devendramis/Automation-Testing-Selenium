from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FindElement:
    def locate_by_id_demo(self):
        # Set up the Chrome WebDriver
        driver = webdriver.Chrome()  # Ensure chromedriver is in PATH

        try:
            # Navigate to the webpage
            driver.get("https://www.dictionary.com/")

            # Use WebDriverWait to wait until the desired element is present
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "list"))
            )
            
            # Check if the element was successfully found
            if element:
                print("Element found:", element)
            else:
                print("Element not found.")

        except Exception as e:
            print("Error occurred:", e)

        finally:
            # Close the driver after the actions
            driver.quit()

# Instantiate and call the method
finder = FindElement()
finder.locate_by_id_demo()