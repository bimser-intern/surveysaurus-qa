from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import modul

#service = Service(".\chromedriver.exe")
#driver = webdriver.Chrome(service = service)

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

modul.devops(driver)

driver.maximize_window()
time.sleep(3)

class FillWithLogin():

    def FillSurveyWithLogin(self):

        modul.login(driver,"luigop@hizliemail.net","Luigop.123")
        modul.findsurvey(driver)
        modul.fillsurvey(driver)
        time.sleep(2)

        message = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[2]/div/label").text

        if message == "Rates":
             print("Anket Doldurma işlemi başarılı.")
        else:
             print("HATA: Anket doldurma işlemi başarılı değil!")

        driver.quit()

fillSurvey = FillWithLogin()
fillSurvey.FillSurveyWithLogin()

