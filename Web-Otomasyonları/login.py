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

class LoginPage():
        def Login(self):

                self.login = driver.find_element(By.XPATH, "//*[@id='#menu']/ul/li[2]/a")
                self.login.click()
                time.sleep(1)

                self.Mail = driver.find_element(By.XPATH, '//*[@id="exampleInputEmail1"]')
                self.Mail.send_keys("ali@gmail.com")
                time.sleep(2)

                self.Password = driver.find_element(By.XPATH, '//*[@id="exampleInputPassword1"]')
                self.Password.send_keys("Ae123456")
                time.sleep(2)

                self.loginButton1 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[4]/div[3]/form/div[4]/button")
                self.loginButton1.click()
                time.sleep(2)

                self.message = driver.find_element(By.XPATH, "//*[@id='root']/div/div[4]/div[3]/form/div[3]/p").text
                if "Incorrect email or password" == self.message:
                        print("Şifre hatalı girildiğinde doğru uyarı verilmiştir.")
                else:
                        print("HATA: Şifre hatalı girilmesine rağmen uyarı verilmemiştir.")

                driver.get("http://40.113.137.113/login")
                time.sleep(1.5)

                self.Mail = driver.find_element(By.XPATH, '//*[@id="exampleInputEmail1"]')
                self.Mail.send_keys("al@gmail.com")
                time.sleep(2)

                self.Password = driver.find_element(By.XPATH, '//*[@id="exampleInputPassword1"]')
                self.Password.send_keys("Abc.123456")
                time.sleep(2)

                self.loginButton2 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[4]/div[3]/form/div[4]/button")
                self.loginButton2.click()
                time.sleep(2)

                self.message = driver.find_element(By.XPATH, "//*[@id='root']/div/div[4]/div[3]/form/div[3]/p").text
                if "Incorrect email or password" == self.message:
                        print("Kullanıcı adı hatalı girildiğinde doğru uyarı verilmiştir.")
                else:
                        print("HATA: Kullanıcı adı yanlış girilmesine rağmen uyarı verilmemiştir.")

                driver.get("http://40.113.137.113/login")
                time.sleep(1.5)

                self.Mail = driver.find_element(By.XPATH, '//*[@id="exampleInputEmail1"]')
                self.Mail.send_keys("ali@gmail.com")
                time.sleep(2)

                self.Password = driver.find_element(By.XPATH, '//*[@id="exampleInputPassword1"]')
                self.Password.send_keys("Abc.123456")
                time.sleep(2)

                self.loginButton3 = driver.find_element(By.XPATH, "//*[@id='root']/div/div[4]/div[3]/form/div[4]/button")
                self.loginButton3.click()
                time.sleep(2)

                self.message = driver.find_element(By.XPATH,"/html/body/div/div/div[1]/ul/li[2]/a/p").text
                if self.message == "mamo":
                        print("Kullanıcı adı ve şifre doğru girildiğinde başarılı bir şekilde giriş yapılmıştır.")
                else:
                        print("HATA: Kullanıcı adı ve şifre doğru girildiğinde başarılı bir şekilde giriş yapılamamıştır.")

                driver.quit()

login = LoginPage()
login.Login()