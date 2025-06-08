from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time 

class demopop:
    def check_popul(self):
        driver = webdriver.Chrome()
        driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_prompt1")
        driver.maximize_window()
        time.sleep(2)

        try:
            driver.switch_to.frame("iframeResult")
            #Accept alart

            # driver.find_element(By.XPATH,"/html/body/button").click()
            # time.sleep(3)
            # driver.switch_to.alert.accept()
            # time.sleep(5)
            
            #Dismise alart

            # driver.find_element(By.XPATH,"/html/body/button").click()
            # time.sleep(3)
            # driver.switch_to.alert.dismiss()
            # time.sleep(5)
        
            #Send text in alert

            driver.find_element(By.XPATH,"/html/body/button").click()
            time.sleep(3)
            alert = driver.switch_to.alert
            alert.send_keys("Sprite")
            time.sleep(3)
            alert.accept()
            time.sleep(5)

        except NoSuchElementException:
            print("Exception is occer in page")

        finally:
            driver.quit()

demo = demopop()
demo.check_popul()
