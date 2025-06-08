from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

class Calendar:
    def calendar_check(self):
        driver = webdriver.Chrome()
        driver.get("https://www.oyorooms.com/deals/oyo/?id=5864&utm_source=google&utm_medium=cpc&utm_device=c&utm_campaign=India_SEM_Brand_generic&utm_campaignid=1701551904&utm_adgroup=71982097371&utm_content=538023998106&utm_keyword=oyo&gad_source=1&gad_campaignid=1701551904&gbraid=0AAAAADj-OgQSnkjGCK2qZSLIRNXNkIcwl&gclid=CjwKCAjwz_bABhAGEiwAm-P8YZumVYHCzSG-xMhV4Y5tiWWKNySo7hvRGRXjqYlAg_9bXRHnJQTl4hoCZ38QAvD_BwE")
        time.sleep(3)
        driver.maximize_window()

        try:
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div/div/div[2]/div[1]/div/section[2]/div/div/div/div[3]/div/div[1]/div/div/div/input").click()
            element1 = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div[1]/div/section[2]/div/div/div/div[3]/div/div[1]/div/span/div/div[3]/div/div[1]/div[1]/input")
            element1.send_keys("Kanpur")
            element1.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div[1]/div/section[2]/div/div/div/div[3]/div/div[1]/div/span/div/div[3]/div/div[2]/div/ul/li").click()
            time.sleep(2)
            driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div[1]/div/section[2]/div/div/div/div[3]/div/div[2]/div/div").click()
            time.sleep(2)
            driver.find_element(By.CLASS_NAME,"DateRangePicker__DateLabel").click()
            time.sleep(2)
            driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div/div/div[2]/div[1]/div/section[2]/div/div/div/div[3]/div/div[2]/div/span/div/div/div[2]/table/tbody/tr[5]/td[2]/span").click()
            time.sleep(2)
            element = driver.find_element(By.CSS_SELECTOR,"#root > div > div.c-r9c3xt > div > div > div.layout.dealPage > div.layout__content.layout__content--isDealPage > div > section.dealPage__container > div > div > div > div:nth-child(5) > div > div.oyo-cell.oyo-cell--2-col.oyo-cell--8-col-tablet.oyo-cell--4-col-phone.homeSearchWidget__gutter.homeSearchWidget__search.homeSearchWidget__search--deal > button")
            element.send_keys(Keys.ENTER)
            time.sleep(5)

        except NoSuchElementException:
            print("There is a Exception is occurs")

        finally:
            driver.quit()

k=Calendar()
k.calendar_check()
 