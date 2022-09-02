from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
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

class Fill():

    def FillSurvey(self):
        time.sleep(1)
        self.scroll = driver.execute_script("window.scrollBy(0,2100)","")
        time.sleep(1)

        self.scrollToRight = driver.find_element(By.XPATH,"/html/body/div/div/div/div[5]/div/div[2]/div/button[2]")
        self.scrollToRight.click()
        time.sleep(1)

        self.survey = driver.find_element(By.XPATH,"/html/body/div/div/div/div[5]/div/div[2]/div/div/div/div[7]/div/div/div/div")
        self.survey.click()
        time.sleep(1)

        self.option = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[2]/div/div[1]/img")
        self.option.click()
        time.sleep(1)

        self.option2 = driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[2]/div/div[2]/img")
        self.option2.click()
        time.sleep(1)

        self.button = driver.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[1]/div[3]/button[2]")
        self.button.click()
        time.sleep(1)

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