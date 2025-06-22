#LOGIN Data Driven Test CASE

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
from time import sleep

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = './/TestData/LoginData.xlsx'
    logger = LogGen.loggen()


    def test_login_ddt(self,setup):
        self.logger.info("***************** Test_002_DDT_Login **********************")
        self.logger.info("***************** Verifying Login Test ********************")

        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp=LoginPage(self.driver)
        sleep(3)

        self.rows = XLUtils.getRowCount(self.path,'Sheet1')
        print("number of rows: ",self.rows)

        lst_status=[]   #empty lsit variable to stroe the exp result

        for r in range(2,self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            print("username:",self.user)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            sleep(5)

            act_title = self.driver.title
            exp_title = "OrangeHRM"


            # IMP note: here our test case wont PASS cause the title of the page before login and after login is same so we wont be able to check whether we are logged in or not based on title


            # if act_title == exp_title:
            #     if self.exp=='Pass':
            #         self.logger.info('*****Passed*****')
            #         self.lp.clickLogout()
            #
            #         lst_status.append('Pass')
            #
            #     elif self.exp=='Fail':
            #         self.logger.info('*****Failed*****')
            #         # self.lp.clickLogout()
            #
            #         lst_status.append('Fail')
            #
            # elif act_title != exp_title:
            #     if self.exp=='Pass':
            #         self.logger.info('*****Failed*****')
            #         # self.lp.clickLogout()
            #
            #         lst_status.append('Fail')
            #
            #     elif self.exp=='Fail':
            #         self.logger.info('*****Passed*****')
            #         # self.lp.clickLogout()

            try:
                login_button = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button')
                if login_button.is_displayed():
                    if self.exp=='Pass':
                        self.logger.info('*****Failed*****')
                        self.lp.clickLogout()

                        lst_status.append('Fail')

                    elif self.exp=='Fail':
                        self.logger.info('*****Passed*****')

                        lst_status.append('Pass')

            except:
                if self.exp=='Pass':
                    self.logger.info('*****Passed*****')
                    self.lp.clickLogout()

                    lst_status.append('Pass')

                elif self.exp=='Fail':
                    self.logger.info('*****Failed*****')

                    lst_status.append('Fail')


            print('lst_status : ',lst_status)

        if 'Fail' not in lst_status:
            self.logger.info('************* Login DDT Test passed *************')
            self.driver.close()
            assert True
        else:
            self.logger.info('************* Login DDT Test failed *************')
            self.driver.close()
            assert False

        self.logger.info("**************** End of Login DDT Test ****************")
        self.logger.info('**************** Completed TC_loginDDT_002 ****************')


