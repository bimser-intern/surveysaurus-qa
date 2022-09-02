from selenium.webdriver.common.by import By
import time
import sys
from selenium.webdriver.common.alert import Alert

def devops(self):

    if len(sys.argv) == 1:
       sys.exit()

    if sys.argv[1] == "production":

       self.options.add_argument("headless")
       self.options.add_argument("--disable-infobars")
       self.options.add_argument("--disable-dev-shm-usage")
       self.options.add_argument("--no-sandbox")
       self.options.add_argument("--remote-debugging-port=9222")
       self.options.add_argument("--window-size=1920,1080")


    if sys.argv[1] == "development":
       # for development
       pass


def login(self, username, password):

    self.get("http://40.113.137.113")
    self.find_element(By.CLASS_NAME, "loginButton").click()
    self.find_element(By.XPATH, "/html/body/div/div/div[4]/div[3]/form/div[1]/input").send_keys(username)
    self.find_element(By.XPATH, "/html/body/div/div/div[4]/div[3]/form/div[2]/input").send_keys(password)
    self.find_element(By.XPATH, "/html/body/div/div/div[4]/div[3]/form/div[4]/button").click()
    time.sleep(3)

def findsurvey(self):

    self.get("http://40.113.137.113")
    time.sleep(1)
    self.scroll = self.execute_script("window.scrollBy(0,2100)","")
    time.sleep(1)

    self.scrollToRight = self.find_element(By.XPATH,"/html/body/div/div/div/div[5]/div/div[2]/div/button[2]")
    self.scrollToRight.click()
    time.sleep(1)

    self.survey = self.find_element(By.XPATH,"/html/body/div/div/div/div[5]/div/div[2]/div/div/div/div[7]/div/div/div/div")
    self.survey.click()
    time.sleep(1)


def fillsurvey(self):
    
    self.option = self.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[2]/div/div[1]/img")
    self.option.click()
    time.sleep(1)

    self.option2 = self.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div[2]/div/div[2]/img")
    self.option2.click()
    time.sleep(1)

    self.button = self.find_element(By.XPATH,"//*[@id='root']/div/div[2]/div[1]/div[3]/button[2]")
    self.button.click()

def comment(self):
    
        time.sleep(3)
        self.execute_script("window.scrollBy(0,350)","")
        self.addComment = self.find_element(By.CLASS_NAME,"addButton")
        self.addComment.click()
        time.sleep(1)

        self.commentArea = self.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/textarea")
        self.commentArea.click()
        time.sleep(1)
        self.commentArea.send_keys("Merhaba, çok iyi bir anket. Kesinlikle çok güzel.")
        time.sleep(1)

        self.commentButton2 = self.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/div")
        self.commentButton2.click()
        time.sleep(1)

def surveyfilltext(self):

    self.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/form/div[1]/input").send_keys("Mevsimler 5")
    self.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/form/div[3]/div[1]/div[3]/input").send_keys("Kış")
    self.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/form/div[2]/input").send_keys("En sevdiğiniz mevsim hangisidir?")
    self.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/form/div[3]/div[2]/div[3]/input").send_keys("Yaz")
    self.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/form/div[4]").click()
    self.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/form/div[4]").click()
    self.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/form/div[3]/div[3]/div[3]/input").send_keys("İlkbahar")
    self.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/form/div[3]/div[4]/div[3]/input").send_keys("Sonbahar")
    self.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/form/div[4]").click()
    self.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/form/div[3]/div[5]/div[3]/input").send_keys("Silinecek seçenek")
    self.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/form/div[3]/div[5]/div[2]/img").click()
    self.execute_script("window.scrollBy(0,350)", "")
    self.find_element(By.CLASS_NAME, "createButton").click()
    time.sleep(3)
