from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

class LoginPage:
    # textbox_username_id="Email"
    textbox_username = "//input[@name='username']"
    # textbox_password_id="Password"
    textbox_password = "//input[@name='password']"
    # button_login_xpath="//button[@class='button-1 login-button']"
    button_login_xpath='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    link_to_linktext_1='Logout'
    link_to_linktext="oxd-userdropdown-tab"

#it will capture the driver from the test case and we'll pass this driver from the test case later and that driver will initiate into the class variable
    def __init__(self,driver):    # this constructor will invoke at the time of object creation
        self.driver = driver

    def setUserName(self, username):
        # self.driver.find_element(By.ID, self.textbox_username_id).clear()
        # self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)
        self.driver.find_element(By.XPATH, self.textbox_username).clear()
        self.driver.find_element(By.XPATH, self.textbox_username).send_keys(username)

    def setPassword(self,password):
        # self.driver.find_element(By.ID,self.textbox_password_id).clear()
        # self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
        self.driver.find_element(By.XPATH, self.textbox_password).clear()
        self.driver.find_element(By.XPATH, self.textbox_password).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.button_login_xpath).click()
        sleep(1)

    def clickLogout(self):
        self.driver.find_element(By.CLASS_NAME, self.link_to_linktext).click()
        sleep(2)
        self.driver.find_element(By.LINK_TEXT,self.link_to_linktext_1).click()
        sleep(2)