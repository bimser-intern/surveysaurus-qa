from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import modul

#service = Service(".\chromedriver.exe")
#driver = webdriver.Chrome(service = service)

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

modul.devops(driver)

driver.maximize_window()
time.sleep(3)

class Fill():

    def FillSurvey(self):

        modul.findsurvey(driver)
        modul.fillsurvey(driver)

        Alert(driver).accept()
        time.sleep(1)

        self.message = driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[3]/div[2]/p").text

        if self.message == "Don't have an account?":
            print("Giriş yapılmadan anket doldurma işleminde login sayfasına yönlendirme durumu başarılı.")
        else:
            print("HATA: İşlem başarılı değil!")

        driver.quit()

fillsurvey = Fill()
fillsurvey.FillSurvey()
driver.quit()