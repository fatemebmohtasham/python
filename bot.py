#------------------
# INSTAGRAM Bot    |
#------------------
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from instabot import bot
import time

class Instabot:

    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.driver=webdriver.Chrome()

    def close_browser(self):
        self.driver.close()    
 
    def login(self):
        self.driver.get('https://www.instagram.com')
        time.sleep(3)
        username=self.driver.find_element(By.NAME,'username')
        username.send_keys(self.username)
        time.sleep(3)
        password=self.driver.find_element(By.NAME,'password')
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)
        time.sleep(3)
        nextbotton=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//button[text() = "Not Now"]')))
        nextbotton.click()
        time.sleep(4)
        self.driver.find_element(By.XPATH,"//button[contains(text(), 'Not Now')]").click()
	

    def follow_with_username(self,username):# FOLLOW WITH USERNAME FUNCTION --------
        self.driver.get('https://www.instagram.com/'+username+'/')
        time.sleep(3)
        followbutton=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH,'//*[text() = "Follow"]'))) 
        followbutton.click()
    
     
    def direct(self,username):# Direct WITH USERNAME FUNCTION --------
        self.driver.get('https://www.instagram.com/'+username+'/')
        time.sleep(2)
        directbutton=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.TAG_NAME,'button')))
        directbutton.click()
        time.sleep(2)
        directbutton=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.TAG_NAME,"textarea")))
        directbutton.send_keys()# WRITE MESSAGE IN DIRECT-----------
        directbutton.send_keys(Keys.ENTER)
    
    
    
    def unfollow_with_username(self,username):# UNFOLLOW WITH USERNAME FUNCTION --------
        self.driver.get('https://www.instagram.com/'+username+'/')
        time.sleep(3)
        unfollowbutton=WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.TAG_NAME,'svg')))
        unfollowbutton.click()
        time.sleep(2)
        unfollowbotton2=WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH,'//*[text() = "Unfollow"]')))
        unfollowbotton2.click()  


person=Instabot()# <- INSERT YOUR INSTAGRAM USERNAME AND PASSWORD HERE --------------------
person.login()
person.follow_with_username()# <- INSERT  USERNAME FOR FOLLOW------------
person.direct()# <- INSERT  USERNAME FOR DIRECT------------
person.unfollow_with_username()# <- INSERT  USERNAME FOR UNFOLLOW------------
