from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import modul
service = Service(".\\chromedriver.exe")

driver = webdriver.Chrome(service = service)
driver.maximize_window()

modul.devops(driver)

class Createsurvey():
  
    @staticmethod

    def createsurvey():

       driver.get("http://40.113.137.113/")
       driver.execute_script("window.scrollBy(0,450)", "")
       time.sleep(3)
       driver.find_element(By.CLASS_NAME, "createButton").click()

       modul.surveyfilltext(driver)
       
       Alert(driver).accept()
       
       if "http://40.113.137.113/login" == driver.current_url:
           print("Giriş yapmadan anket oluşturulduğunda login sayfasına yönlendirme işlemi başarılıdır.")
       else:
           print("HATA: Giriş yapmadan anket oluşturulduğunda login sayfasına yönlendirme işlemi başarısız olmuştur.")

       driver.quit()

create = Createsurvey()
create.createsurvey()