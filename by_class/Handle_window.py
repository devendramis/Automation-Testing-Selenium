from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class HandleWindow:
    def multiple_windows(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        driver.maximize_window()

        try:
            parent_handle = driver.current_window_handle
            print("Parent Window Handle:", parent_handle)

            # Click the element to open new window (Use a better XPath or CSS selector)
            time.sleep(3)
            img_element = driver.find_element(By.XPATH, "//img[contains(@src, 'special-offer')]")  # Example fix
            img_element.click()

            # Wait for new window to open
            WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)

            # Get all window handles
            all_handles = driver.window_handles
            for handle in all_handles:
                if handle != parent_handle:
                    driver.switch_to.window(handle)
                    print("Switched to child window:", handle)
                    break

            # Example interaction in new window (adjust XPath as needed)
            try:
                promo_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), 'View All Offers')]"))
                )
                promo_element.click()
                print("Clicked on View All Offers")
            except NoSuchElementException:
                print("Promo element not found in new window.")

        except NoSuchElementException as e:
            print("Element not found:", e)

        finally:
            time.sleep(3)
            driver.quit()

# Run
k = HandleWindow()
k.multiple_windows()
