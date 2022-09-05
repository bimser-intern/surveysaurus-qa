from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import modul
import time

options = modul.devops()
driver = webdriver.Chrome(options=options)

driver.maximize_window()
time.sleep(3)


class CommentWithLoginPage:
    def __int__(self, email, password, message):
        self.email = email
        self.password = password
        self.message = message

    def CommentWithLogin(self):

        modul.login(driver,"luigop@hizliemail.net","Luigop.123")

        time.sleep(1)
        self.scroll = driver.execute_script("window.scrollBy(0,2100)", "")
        time.sleep(1)

        self.scrollToRight = driver.find_element(
            By.XPATH, "/html/body/div/div/div/div[5]/div/div[2]/div/button[2]"
        )
        self.scrollToRight.click()
        time.sleep(1)

        self.survey = driver.find_element(
            By.XPATH,
            "/html/body/div/div/div/div[5]/div/div[2]/div/div/div/div[7]/div/div/div/div",
        )
        self.survey.click()
        time.sleep(2)

        self.addComment = driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[2]/div/div/p"
        )
        self.addComment.click()
        time.sleep(1)

        self.commentButton1 = driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div/div/div/div"
        )
        self.commentButton1.click()
        time.sleep(1)

        Alert(driver).accept()
        time.sleep(1)

        self.commentArea = driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div/div/textarea"
        )
        self.commentArea.click()
        time.sleep(1)
        self.commentArea.send_keys("Merhaba, çok iyi bir anket. Kesinlikle çok güzel.")
        time.sleep(1)

        self.commentButton2 = driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div/div/div/div"
        )
        self.commentButton2.click()
        time.sleep(1)

        self.message = driver.find_element(
            By.XPATH, "/html/body/div/div/div[2]/div[2]/div/h1"
        ).text

        if self.message == "Comments":
            print("Yorum yapma işlemi başarılı.")
        else:
            print("HATA: Yorum yapma işlemi başarısız!")

        driver.quit()


commentpage = CommentWithLoginPage()
commentpage.CommentWithLogin()
