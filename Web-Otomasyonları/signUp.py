from msilib.schema import Class
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random
import itertools
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert
import sys

#service = Service(".\chromedriver.exe")
#driver = webdriver.Chrome(service=service)

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


driver.get("http://40.113.137.113/")
driver.maximize_window()
time.sleep(3)

class SignUpPage():
    def __int__(self, Name, Mail, Gender, Country, City, Password, Password2, email, message):
        self.Name = Name
        self.Mail = Mail
        self.Gender = Gender
        self.Country = Country
        self.City = City
        self.Password = Password
        self.Password2 = Password2
        self.email = email

    def SignUp(self):


        self.signup = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/ul/li[1]/a/p")
        self.signup.click()
        time.sleep(2)

        self.scroll = driver.execute_script("window.scrollBy(0,200)", "")
        time.sleep(2)


        letterss = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                  "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]

        all_combos1 = list(itertools.combinations(letterss, 7))  # make all 7 letter combinations
        all_combos1 = [''.join(combo) for combo in all_combos1]  # make them strings
        self.username = random.sample(all_combos1, 1)[0]
        username = ''
        for _ in range(7):
            letter1 = random.sample(letterss, 1)[0]
            username += letter1


        name = driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[3]/form/div[1]/input")
        name.send_keys(username)
        time.sleep(1)

        letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
                   "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]

        all_combos = list(itertools.combinations(letters, 7))  # make all 7 letter combinations
        all_combos = [''.join(combo) for combo in all_combos]  # make them strings
        self.email = random.sample(all_combos, 1)[0] + '@gmail.com'  # grab a random one, add @gmail.com
        email = ''
        for _ in range(7):
            letter = random.sample(letters, 1)[0]
            email += letter

        email += '@gmail.com'

        self.Mail = driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[3]/form/div[2]/input")
        self.Mail.send_keys(email)
        time.sleep(1)

        Select(driver.find_element(By.XPATH,"/html/body/div/div/div[4]/div[3]/form/div[3]/select")).select_by_visible_text("Male")
        time.sleep(1)

        Select(driver.find_element(By.XPATH,"/html/body/div/div/div[4]/div[3]/form/div[4]/select")).select_by_visible_text("Turkey")
        time.sleep(1)

        Select(driver.find_element(By.XPATH,"/html/body/div/div/div[4]/div[3]/form/div[5]/select")).select_by_visible_text("Kocaeli")
        time.sleep(1)

        self.Password = driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[3]/form/div[6]/input")
        self.Password.click()
        self.Password.send_keys("Abc.123456")
        time.sleep(1)

        self.Password2 = driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[3]/form/div[7]/input")
        self.Password2.click()
        self.Password2.send_keys("Abc.123456")
        time.sleep(1)

        button = driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[3]/form/div[9]/button")
        button.click()
        button.click()
        time.sleep(3)

        Alert(driver).accept()
        time.sleep(3)

        message = driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[3]/div[2]/p").text

        if message == "Don't have an account?":
            print("Üye olma işlemi başarılı.")
        else:
            print("HATA: Üye olma işlemi başarılı değil!")

        driver.quit()

signup = SignUpPage()
signup.SignUp()

