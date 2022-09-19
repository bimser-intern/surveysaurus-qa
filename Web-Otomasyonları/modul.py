from selenium.webdriver.common.by import By
import time
import sys
from selenium import webdriver
import random
import itertools

options = webdriver.ChromeOptions()

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

driver = webdriver.Chrome(options=options)
link = "http://20.4.45.170"

def login(driver, username, password):

    driver.get(link)
    driver.find_element(By.CLASS_NAME, "loginButton").click()
    driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[3]/form/div[1]/input").send_keys(username)
    driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[3]/form/div[2]/input").send_keys(password)
    driver.find_element(By.XPATH, "/html/body/div/div/div[4]/div[3]/form/div[4]/button").click()
    time.sleep(3)

def logout(driver):
    driver.find_element(By.CLASS_NAME, "UserIcon").click()
    driver.find_element(By.CLASS_NAME, "logOutContainer").click()

def findsurvey(driver):
    
    driver.get(link)
    time.sleep(1)
    driver.scroll = driver.execute_script("window.scrollBy(0,2100)", "")
    time.sleep(1)

    driver.scrollToRight = driver.find_element(
        By.XPATH, "/html/body/div/div/div/div[5]/div/div[2]/div/button[2]"
    )
    driver.scrollToRight.click()
    time.sleep(1)

    driver.survey = driver.find_element(By.XPATH, "/html/body/div/div/div/div[5]/div/div[2]/div/div/div/div[7]/div/div/div/div")
    driver.survey.click()
    time.sleep(1)


def fillsurvey(driver):

    driver.option = driver.find_element(
        By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div/div[1]/img"
    )
    driver.option.click()
    time.sleep(1)

    driver.option2 = driver.find_element(
        By.XPATH, "/html/body/div/div/div[2]/div[1]/div[2]/div/div[2]/img"
    )
    driver.option2.click()
    time.sleep(1)

    driver.button = driver.find_element(
        By.XPATH, "//*[@id='root']/div/div[2]/div[1]/div[3]/button[2]"
    )
    driver.button.click()


def comment(driver):
    
    time.sleep(3)
    driver.addComment = driver.find_element(By.CLASS_NAME, "addButton")
    driver.addComment.click()
    time.sleep(1)

    driver.commentArea = driver.find_element(
        By.XPATH, "/html/body/div/div/div[2]/div/div/textarea"
    )
    driver.commentArea.click()
    time.sleep(1)
    driver.commentArea.send_keys("Merhaba, çok iyi bir anket. Kesinlikle çok güzel.")
    time.sleep(1)

    driver.commentButton2 = driver.find_element(
        By.XPATH, "/html/body/div/div/div[2]/div/div/div/div"
    )
    driver.commentButton2.click()
    time.sleep(1)


def surveyfilltext(driver):

    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/form/div[1]/input").send_keys("Mevsimler 5")

    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/form/div[2]/input").send_keys("En sevdiğiniz mevsim hangisidir?")

    driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/form/div[3]/div[1]/div[3]/input").send_keys("Kış")

    driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/form/div[3]/div[2]/div[3]/input").send_keys("Yaz")

    driver.find_element(By.CLASS_NAME, "addOption").click()    
    driver.find_element(By.CLASS_NAME, "addOption").click()

    driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/form/div[3]/div[3]/div[3]/input").send_keys("İlkbahar")

    driver.find_element( By.XPATH,"/html/body/div/div/div[2]/div/div/div/form/div[3]/div[4]/div[3]/input").send_keys("Sonbahar")

    driver.find_element(By.CLASS_NAME, "addOption").click()

    driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div/div/div/form/div[3]/div[5]/div[3]/input").send_keys("Silinecek seçenek")

    driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div/div/form/div[3]/div[5]/div[2]/img").click()

    driver.execute_script("window.scrollBy(0,350)", "")

    driver.find_element(By.CLASS_NAME, "createButton").click()

    time.sleep(3)


def email(driver):

   letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]   
   all_combos = list(itertools.combinations(letters, 7))  # make all 7 letter combinations
   all_combos = [''.join(combo) for combo in all_combos]  # make them strings
   email = random.sample(all_combos, 1)[0] + '@gmail.com'  # grab a random one, add @gmail.com
   email = ''
   for _ in range(7):
       letter = random.sample(letters, 1)[0]
       email += letter

   email += '@gmail.com'

   return email