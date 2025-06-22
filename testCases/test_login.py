import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from time import sleep

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, setup):

        self.logger.info("***************** Test_001_Login ********************")   # first should always be to show the test case ID
        self.logger.info("***************** Verifying Home Page Title ********************")

        self.driver = setup
        self.driver.get(self.baseURL)
        sleep(2)
        act_title = self.driver.title
        self.driver.close()

        # if act_title == 'Your store. Login':
        # if act_title == 'nopCommerce demo store. Login':
        if act_title == 'OrangeHRM':
            assert True
            self.logger.info("***************** Home Page Title passed ********************")
            # self.driver.close()
        else:
            # self.driver.close()
            self.logger.error("***************** Home Page Title failed ********************")
            assert False

    def test_login(self,setup):

        self.logger.info("***************** Verifying Login Test ********************")

        self.driver = setup
        self.driver.get(self.baseURL)
        sleep(3)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        sleep(2)
        self.lp.clickLogin()
        sleep(5)
        act_title = self.driver.title
        print("helloooo",act_title)
        # if act_title == 'Dashboard / nopCommerce administration':
        if act_title == 'OrangeHRM':
            assert True
            self.logger.info("***************** Test Login passed ********************")
            # self.driver.close()
        else:
            # self.driver.save_screenshot(".\\Screenshots\\" +"test_login.png")   # . here represent current directory
            # self.driver.close()
            self.logger.error("***************** Test Login failed ********************")
            assert False

        # self.lp.clickLogout()

        # < input
        # type = "checkbox" >