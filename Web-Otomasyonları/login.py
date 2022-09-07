import modul
from selenium.webdriver.common.by import By
import time


class Login():

      def Loginsurvey(self, driver):
         
         modul.login(modul.driver,"123@gmail.com", "Ae123456")
         mesaj = driver.find_element(By.CLASS_NAME, "wrongLogIn").text
         if "Incorrect email or password" == mesaj:
            print("Şifre hatalı girildiğinde doğru uyarı verilmiştir.")
         else:
            print("HATA: Şifre hatalı girilmesine rağmen uyarı verilmemiştir.")

         modul.login(modul.driver,"12345@gmail.com", "Ae123456")
         mesaj = driver.find_element(By.CLASS_NAME, "wrongLogIn").text
         if "Incorrect email or password" == mesaj:
            print("Kullanıcı adı hatalı girildiğinde doğru uyarı verilmiştir.")
         else:
            print("HATA: Kullanıcı adı yanlış girilmesine rağmen uyarı verilmemiştir.")

         modul.login(modul.driver,"123@gmail.com", "Ue123456")
         time.sleep(2)
         kullanıcı_adi = driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/ul[2]/li[2]/a/p").text
         if kullanıcı_adi == "mobil ilk deneme":
           print("Kullanıcı adı ve şifre doğru yazıldığında başarılı bir şekilde giriş yapılmıştır. ")
         else:
           print("HATA: Kullanıcı adı ve şifre doğru yazıldığında başarılı bir şekilde giriş yapılamamıştır. ")

         modul.logout(driver)


