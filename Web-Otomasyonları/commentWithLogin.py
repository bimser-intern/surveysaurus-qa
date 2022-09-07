from selenium.webdriver.common.by import By
import modul


class CommentWithLoginPage:
    def __int__(self, email, password, message, driver):
        self.email = email
        self.password = password
        self.message = message
        self.driver = driver

    def CommentWithLogin(self, driver):

        modul.login(driver,"luigop@hizliemail.net","Luigop.123")
        modul.findsurvey(driver)
        modul.comment(driver)

        self.message = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div[2]/div/h1").text

        if self.message == "Comments":
            print("Yorum yapma işlemi başarılı.")
        else:
            print("HATA: Yorum yapma işlemi başarısız!")

        driver.quit()
