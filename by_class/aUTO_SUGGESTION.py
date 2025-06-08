from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

class auto_suggestion:
    def auto_suggestion_check(self):
        driver = webdriver.Chrome()
        driver.get("https://www.yatra.com/")
        time.sleep(2)
        driver.maximize_window()

        try:
            element = driver.find_element(By.CSS_SELECTOR,"#__next > div > div.MuiBox-root.css-1h9nmm8 > div.MuiBox-root.css-1jea2if > div.MuiBox-root.css-n9rhs2 > div.MuiBox-root.css-1xaekgw > div.MuiBox-root.css-1az9q6q > div.MuiBox-root.css-cp8bg9 > div > button").click()
            print(element)

            driver.find_element(By.XPATH,"/html/body/section[1]/section/div/div/form/ul[2]/li[2]/div/input").click()
            driver.find_element(By.ID,"origin_0").send_keys("New Dehli")
            driver.find_element(By.XPATH,"/html/body/section[1]/section/div/div/form/ul[2]/li[2]/div/input").send_keys(Keys.ENTER)
            time.sleep(5)

        except NoSuchElementException:
            print("Exception is occur")

        finally:
            driver.quit()

k=auto_suggestion()
k.auto_suggestion_check()


