from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException,ElementNotInteractableException
from dotenv import load_dotenv
load_dotenv("C:/Python/Environmental variables/.env")
import os
import time

insta_mail = os.getenv("insta_email")
insta_password = os.getenv("insta_password")


class InstaFollower:
    def __init__(self):
        self.followers = None
        self.insta_url = "https://www.instagram.com/"
        self.acc_url = "https://www.instagram.com/chefsteps/"
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
        time.sleep(7)

    def find_followers(self):
        self.driver.get(self.acc_url)
        time.sleep(3)
        # base_window = self.driver.current_window_handle
        self.followers = self.driver.find_element(By.XPATH,value='/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a')
        self.followers.click()
        time.sleep(3)
        # popup = self.driver.window_handles[1]
        # self.driver.switch_to.window(popup)

    # my bot account was detected by instagram, and they restricted my activities li follow or unfollow accounts
    # when i click follow, it shows "restricted these activities".So i have to click "Ok" and try to follow other accounts.
    def follow(self):
        # Here i set range 100,so it follows 100 accounts(99 actually)
        for i in range(1,100):
            acc = self.driver.find_element(By.XPATH,value = f"/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[{i}]")
            acc.find_element(By.TAG_NAME,value="button").click()
            time.sleep(5)
            self.driver.find_element(By.XPATH,
                                     value='/html/body/div[7]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/button[2]').click()
            # here i set a delay to scroll down,so it won't scroll down for every loop
            if i % 4 == 0:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", acc)
            time.sleep(3)

# For some reason, window_handles are not working.I tried to find solutions but cant find it.So i just used XPATH to access popup window.
# The exception handlers that I imported will come in handy when my bot account actually follows accounts.
# For example, if i try to follow already followed account,then it can be fixed using exception handlers.

in_fo = InstaFollower()
in_fo.login()
in_fo.find_followers()
in_fo.follow()