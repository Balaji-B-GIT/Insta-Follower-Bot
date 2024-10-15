from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException,ElementNotInteractableException
from dotenv import load_dotenv
load_dotenv("C:/Python/Environmental variables/.env")
import os
import time

insta_mail = os.getenv("insta_email")
insta_password = os.getenv("insta_password")


class InstaFollower:
    def __init__(self):
        self.insta_url = "https://www.instagram.com/"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.maximize_window()
    def login(self):
        self.driver.get(self.insta_url)
        time.sleep(3)
        username_field = self.driver.find_element(By.NAME,value="username")
        password_field = self.driver.find_element(By.NAME,value="password")
        sign_in = self.driver.find_element(By.XPATH,value='//*[@id="loginForm"]/div/div[3]/button')
        username_field.send_keys(insta_mail)
        time.sleep(2)
        password_field.send_keys(insta_password)
        time.sleep(2)
        sign_in.click()
        time.sleep(3)
        search_icon = self.driver.find_element(By.XPATH,value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[2]')
        search_icon.click()
        time.sleep(2)
        search_input = self.driver.find_element(By.XPATH,value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input')
        search_input.send_keys("balaji_raina_")
        time.sleep(2)
        profile = self.driver.find_element(By.XPATH,value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]/div[1]')
        profile.click()
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME,value="_acan._acap._acas._aj1-._ap30").click()



in_fo = InstaFollower()
in_fo.login()