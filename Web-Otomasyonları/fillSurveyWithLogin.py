from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import sys

#service = Service(".\chromedriver.exe")
#driver = webdriver.Chrome(service = service)

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

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

class FillWithLogin():

    def __int__(self,email, password, message):
        self.email = email
        self.password = password
        self.message = message

    def FillSurveyWithLogin(self):

        self.login = driver.find_element(By.XPATH,"//*[@id='#menu']/ul/li[2]/a")
        self.login.click()
        time.sleep(1)

        email = driver.find_element(By.XPATH,"/html/body/div/div/div[4]/div[3]/form/div[1]/input")
        email.send_keys("luigop@hizliemail.net")
        time.sleep(1)

        password = driver.find_element(By.XPATH,"/html/body/div/div/div[4]/div[3]/form/div[2]/input")
        password.send_keys("Luigop.123")
        time.sleep(1)

        self.loginButton = driver.find_element(By.XPATH,"/html/body/div/div/div[4]/div[3]/form/div[4]/button")
        self.loginButton.click()
        time.sleep(1)

        self.home = driver.find_element(By.XPATH,"/html/body/div/div/div[1]/nav/ul/li[1]/a")
        self.home.click()
        time.sleep(1)

        self.scroll = driver.execute_script("window.scrollBy(0,2100)","")
        time.sleep(1)

        self.scrollToRight = driver.find_element(By.XPATH,"/html/body/div/div/div/div[5]/div/div[2]/div/button[2]")
        self.scrollToRight.click()
        time.sleep(1)

        self.survey = driver.find_element(By.XPATH,"/html/body/div/div/div/div[5]/div/div[2]/div/div/div/div[7]/div/div/div/div")
        self.survey.click()
        time.sleep(2)

        self.option = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[2]/div/div[1]/img")
        self.option.click()
        time.sleep(2)

        self.option2 = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[2]/div/div[2]/img")
        self.option2.click()
        time.sleep(2)

        self.button = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[1]/div[3]/button[2]")
        self.button.click()
        time.sleep(2)

        message = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[2]/div/label").text

        if message == "Rates":
             print("Anket Doldurma işlemi başarılı.")
        else:
             print("HATA: Anket doldurma işlemi başarılı değil!")

        driver.quit()

fillSurvey = FillWithLogin()
fillSurvey.FillSurveyWithLogin()

