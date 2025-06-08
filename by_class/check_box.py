from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

class check_boxe:
    def check_boxe_is_working(slef):
        driver = webdriver.Chrome()
        driver.get("https://www.zoho.com/forms/index1.html?campaignid=22356223675&adgroup=177605580378&keyword=form%20maker&matchtype=e&device=c&network=g&adposition=&placement=&gad_source=1&gbraid=0AAAAACg12Ats-GWHXUECRku7VVTCmVPnc&gclid=Cj0KCQjwt8zABhDKARIsAHXuD7Z74Vg2PqI-wf2Xc1eShRFhBXnZDJClWI-Mf8bgqOHC-CrkyZuZfgkaAn0cEALw_wcB")
        driver.maximize_window()
        time.sleep(3)

        try:
            name = "/html/body/main/div/div[1]/div[1]/div/div/div[2]/div/div/div/form/div/div[1]/div/input"
            email = "/html/body/main/div/div[1]/div[1]/div/div/div[2]/div/div/div/form/div/div[2]/div/input"
            password = "/html/body/main/div/div[1]/div[1]/div/div/div[2]/div/div/div/form/div/div[3]/div/input"
            phone_number = "/html/body/main/div/div[1]/div[1]/div/div/div[2]/div/div/div/form/div/div[4]/div/div/input[2]"
            agree = "signup-termservice"
            driver.find_element(By.XPATH,name).send_keys("Devendra Mishra")
            time.sleep(2)
            driver.find_element(By.XPATH,email).send_keys("harshitmishra3307@gmail.com")
            time.sleep(2)
            driver.find_element(By.XPATH,password).send_keys("Babashiv@12345")
            time.sleep(2)
            driver.find_element(By.XPATH,phone_number).send_keys("6393873957")
            time.sleep(2)

            element = driver.find_element(By.ID,agree).click()
            print("Agree Botton is working" , element)
            
            var1 = driver.find_element(By.ID,agree).is_selected()
            print(var1)
            
            

        except NoSuchElementException:
            print("No Error in this code")

        finally:
            driver.quit()

k = check_boxe()
k.check_boxe_is_working()