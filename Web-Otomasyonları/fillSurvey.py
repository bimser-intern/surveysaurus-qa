from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import modul

class Fill():

    def FillSurvey(self, driver):    

        modul.findsurvey(driver)
        modul.fillsurvey(driver)

        Alert(driver).accept()
        time.sleep(1)

        self.message = driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[3]/div[2]/p").text

        if self.message == "Don't have an account?":
            print("Giriş yapılmadan anket doldurma işleminde login sayfasına yönlendirme durumu başarılı.")
        else:
            print("HATA: İşlem başarılı değil!")


