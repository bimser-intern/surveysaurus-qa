from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import modul


class Createsurvey:

    def createsurvey(self, driver):

        driver.get(modul.link)
        driver.execute_script("window.scrollBy(0,450)", "")
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "createButton").click()

        modul.surveyfilltext(driver)

        Alert(driver).accept()

        if driver.current_url == modul.link:
            print(
                "Giriş yapmadan anket oluşturulduğunda login sayfasına yönlendirme işlemi başarılıdır."
            )
        else:
            print(
                "HATA: Giriş yapmadan anket oluşturulduğunda login sayfasına yönlendirme işlemi başarısız olmuştur."
            )




