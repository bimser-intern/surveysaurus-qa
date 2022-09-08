from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import modul


class CreateSurveywithLogin():
    
     def Survey(self, driver):
        
        # giriş sign up otomasyonunun sonunda yapıldı.

        # ana sayfadan create survey sayfasına izlenen yol

        profil_ikonu = driver.find_element(By.CLASS_NAME, "UserIcon")
        profil_ikonu.click()

        my_surveys = driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/ul[2]/li[3]/div/div/div/div[2]")
        my_surveys.click()

        create_survey = driver.find_element(By.ID, "pluscreatesurvey")
        create_survey.click()

        # anket oluşturma modulü

        modul.surveyfilltext(driver)  
 
        # anket oluşturdaktan sonra çıkan uyarının kontrolü

        mesaj =  Alert(driver).text

        if "The survey creation process was successful." in mesaj:
           print("Anket oluştulduğunda başarılı bir şekilde oluşturulduğuna dair uyarı gelmiştir.")
        else:
           print("HATA: Anket oluştulduğunda başarılı bir şekilde oluşturulduğuna dair uyarı gelmemiştir.")

        Alert(driver).accept()
        time.sleep(1)
        
        # anket oluşturduktan sonra My Surveys sayfasına yönlendirme işleminin kontrolü

        link = driver.current_url()

        if "http://40.113.137.113/userPage" == link:
           print("Anket oluşturma işlemi tamamlandığında My Surveys sayfasına yönlendirme işlemi başarılıdır.")
        else:
           print("HATA: Anket oluşturma işlemi tamamlandığında My Surveys sayfasına yönlendirme işlemi başarısız olmuştur.")

       # anketin oluşturulduktan sonra My Surveys sayfasında görüntülenebilmesinin kontrolü

        survey_card_title = driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div/div[1]/div/h3").text
        
        if "Mevsimler 5" in survey_card_title:
           print("Anket oluşturma işlemi tamamlandığında anket My Surveys sayfasında gözükmektedir.")
        else:
           print("HATA: Anket oluşturma işlemi tamamlandığında anket My Surveys sayfasında gözükmemektedir.")
        
        # hesaptan çıkış yapmak için kullanılan modül
        modul.logout(driver)
