from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InstaFollower():
    def __init__(self):
        self.driver=self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    


    def login(self,USERNAME,PASSWORD):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        login=self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input')
        login.send_keys(USERNAME)
        login=self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input')
        login.send_keys(PASSWORD)
        login=self.driver.find_element(By.CSS_SELECTOR,'button>.xjbqb8w ');
        login.click()
        time.sleep(10)






    def find_followers(self):
        self.driver.get("https://www.instagram.com/chefsteps/")
        time.sleep(10)
        find=self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a")
        find.click()
        time.sleep(5)
        
        scr1 = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
    
    def follow(self):
        try:
    # Wait for all "Follow" buttons to be present on the page
            wait = WebDriverWait(self.driver, 10)
            follow_buttons = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[contains(., 'Follow')]")))

            # Click each "Follow" button
            for button in follow_buttons[1:]:
                button.click()
                time.sleep(1)

            print("All 'Follow' buttons clicked successfully!")
        except Exception as e:
            print(f"Error occurred while clicking 'Follow' buttons: {str(e)}")
        time.sleep(10)
        scr1 = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]')
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)