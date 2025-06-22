import pytest
from time import sleep

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.LoginPage import LoginPage
from pageObjects.AddPIMPage import AddPIM
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import string
import random

class Test_0003_AddPIM:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()    #logger


    def test_addPIM(self, setup):           # setup means it will return the browser driver here and we are using self keyword cause we can only access class level variable in that way
        self.logger.info('********************* Test_0003_AddPIM ************************')
        self.driver = setup
        self.driver.get(self.baseURL)

        sleep(2)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        sleep(2)
        self.lp.clickLogin()
        sleep(2)
        self.logger.info('********************* Login Successful ************************')

        self.logger.info('********************* Starting Add PIM Test ************************')

        self.aa = AddPIM(self.driver)
        self.aa.clickonPIM()
        sleep(4)
        self.aa.addEmp()
        sleep(4)

        self.logger.info('********************* Providing PIM Info ************************')

        self.aa.setFName('Dance')
        self.aa.setLName('Louis')
        self.aa.setSave()
        sleep(2)

        self.logger.info("***************** Add PIM validation_1 started *****************")

        # self.val1 = self.driver.find_element(By.XPATH,"//h6[text()='Add Employee']")
        #
        # if self.val1.is_displayed():
        #     # self.driver.save_screenshot(".\\Screenshots\\" +"test_addPIM.png")   # . here represent current directory
        #     self.logger.info('**************** Add PIM Test failed ****************')
        #     assert True == False
        #     self.driver.close()
        # else:
        #     assert True == True
        #     self.logger.info('**************** Add PIM Test passed ****************')

        try:
            self.msg = self.driver.find_element(By.TAG_NAME, "body").text
            assert 'Successfully Updated' in self.msg, f"Test Failed: Message 'Successfully Updated' not found. Full text: {self.msg}"   #If the test passes, this message never appears.
            self.logger.info('**************** Add PIM Test passed ****************')
        except AssertionError as e :                       #When an assert fails, Python raises an AssertionError
            # You can also take a screenshot here if needed to debug the failure
            # self.driver.save_screenshot(".\\Screenshots\\" + "test_addPIM_1.png")
            self.logger.info('**************** Add PIM Test failed ****************')
            assert e   # keeps the original error message


        sleep(5)
        self.aa.setOtherId('1122')
        sleep(2)
        self.aa.setDriverLncs('GJ01256S')
        sleep(2)
        self.aa.setLcnsExpDate('2030-02-25')
        sleep(2)
        self.aa.setNationality('Angolan')
        sleep(3)
        self.aa.setMaritalSts('Single')
        sleep(3)
        self.aa.setDob('2000-01-01')
        sleep(3)
        self.aa.setGender('Male')
        sleep(2)
        self.aa.setSave()
        sleep(1)

        self.logger.info('********************* Saving PIM Info ************************')

        self.logger.info("***************** Add PIM validation_2 started *****************")

        # self.msg = self.driver.find_element(By.TAG_NAME,"body").text
        #
        # if 'Successfully Updated' in self.msg:
        #     assert True == True
        #     self.logger.info('**************** Add PIM Test passed ****************')
        # else:
        #     # self.driver.save_screenshot(".\\Screenshots\\" + "test_addPIM_1.png")  # . here represent current directory
        #     self.logger.info('**************** Add PIM Test failed ****************')
        #     assert True == False


        # try:
        #     sucess = WebDriverWait(self.driver, 1).until(EC.presence_of_element_located((By.XPATH, "//*[text()='Successfully Updated']")))
        #     assert True == True
        #     self.logger.info('**************** Add PIM Test passed ****************')
        # except:
        #     # self.driver.save_screenshot(".\\Screenshots\\" + "test_addPIM_1.png")  # . here represent current directory
        #     self.logger.info('**************** Add PIM Test failed ****************')
        #     assert True == False

        try:
            self.msg = self.driver.find_element(By.TAG_NAME, "body").text
            assert 'Successfully Updated' in self.msg, f"Test Failed: Message 'Successfully Updated' not found. Full text: {self.msg}"   #If the test passes, this message never appears.
            self.logger.info('**************** Add PIM Test passed ****************')
        except AssertionError as e :                       #When an assert fails, Python raises an AssertionError
            # You can also take a screenshot here if needed to debug the failure
            # self.driver.save_screenshot(".\\Screenshots\\" + "test_addPIM_1.png")
            self.logger.info('**************** Add PIM Test failed ****************')
            assert e   # keeps the original error message


        self.driver.close()
        # self.driver.info("*************** Add PIM Test ****************")
# <p data-v-7b563373 data-v-35c8fe09 class="oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text">Successfully Updated</p>