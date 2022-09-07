from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time
import modul


class CommentPage:
    
    def Comment(self, driver):

        modul.findsurvey(driver)
        modul.comment(driver)

        Alert(driver).accept()
        time.sleep(1)

        self.message = driver.find_element(
            By.XPATH, "/html/body/div/div/div[4]/div[3]/div[2]/p"
        ).text

        if self.message == "Don't have an account?":
            print(
                "Yorum alanına bir şey yazılmadan Comment butonuna tıklandığında gerekli uyarı mesajı verildi."
            )
            print(
                "Giriş yapılmadan yorum yapmak istendiğinde login sayfasına yönlendirme durumu başarılı."
            )
        else:
            print("HATA: İşlem başarılı değil!")

        driver.quit()


