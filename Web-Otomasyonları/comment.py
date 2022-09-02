from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time
import sys

#service = Service(".\chromedriver.exe")
#driver = webdriver.Chrome(service = service)

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(20)

if len(sys.argv) == 1:
    sys.exit()

if sys.argv[1] == "production":

    options.add_argument("headless")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--remote-debugging-port=9222")
    options.add_argument("--window-size=1920,1080")


if sys.argv[1] == "development":
    # for development
    pass


driver.get("http://40.113.137.113")
driver.maximize_window()
time.sleep(3)

class CommentPage():

    def Comment(self):
        time.sleep(1)
        self.scroll = driver.execute_script("window.scrollBy(0,2100)","")
        time.sleep(1)

        self.scrollToRight = driver.find_element(By.XPATH,"/html/body/div/div/div/div[5]/div/div[2]/div/button[2]")
        self.scrollToRight.click()
        time.sleep(1)

        self.survey = driver.find_element(By.XPATH,"/html/body/div/div/div/div[5]/div/div[2]/div/div/div/div[7]/div/div/div/div")
        self.survey.click()
        time.sleep(1)

        self.addComment = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div/div/p")
        self.addComment.click()
        time.sleep(1)

        self.commentButton1 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div")
        self.commentButton1.click()
        time.sleep(1)

        Alert(driver).accept()
        time.sleep(1)

        self.commentArea = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/textarea")
        self.commentArea.click()
        time.sleep(1)
        self.commentArea.send_keys("Merhaba, çok iyi bir anket. Kesinlikle çok güzel.")
        time.sleep(1)

        self.commentButton2 = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div")
        self.commentButton2.click()
        time.sleep(1)

        Alert(driver).accept()
        time.sleep(1)

        self.message = driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[3]/div[2]/p").text

        if self.message == "Don't have an account?":
            print("Yorum alanına bir şey yazılmadan Comment butonuna tıklandığında gerekli uyarı mesajı verildi.")
            print("Giriş yapılmadan yorum yapmak istendiğinde login sayfasına yönlendirme durumu başarılı.")
        else:
            print("HATA: İşlem başarılı değil!")

        driver.quit()

comment = CommentPage()
comment.Comment()


