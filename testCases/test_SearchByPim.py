from pageObjects.LoginPage import LoginPage
from pageObjects.AddPIMPage import AddPIM
from pageObjects.PIM_search import SearchPIM
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from time import sleep
import pytest

class Test_004_PIM_Search:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.fixture(autouse=True)
    def setup_method(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("********************* Login Successful ************************")

        self.ap = AddPIM(self.driver)
        self.ap.clickonPIM()
        self.logger.info("********************* Navigated to PIM ************************")

    @pytest.mark.regression
    def test_searchEmpByName(self):
        self.logger.info('******************** Running: test_searchEmpByName ********************')

        self.emp_name = 'Raj Kumar'

        self.sp = SearchPIM(self.driver)
        self.sp.setName(self.emp_name)
        self.sp.clickSearch()

        status = self.sp.searchEmpByName(self.emp_name)
        assert True == status

        self.logger.info('******************** Finished: test_searchEmpByName ********************')

    @pytest.mark.regression
    def test_searchEmpById(self):
        self.logger.info('******************** Running: test_searchEmpById ********************')

        self.emp_id = '0474'

        self.sp = SearchPIM(self.driver)
        self.sp.setId(self.emp_id)
        self.sp.clickSearch()

        status = self.sp.searchEmpById(self.emp_id)
        assert True == status

        self.logger.info('******************** Finished: test_searchEmpById ********************')


    @pytest.mark.regression
    def test_resetSearchForm(self):
        self.logger.info('******************** Running: test_resetSearchForm ********************')

        self.sp = SearchPIM(self.driver)
        self.sp.setName('${firstName} JMeter ${lastName}')
        self.sp.setId('3065')

        self.sp.clickReset()

        name_value = self.driver.find_element(*self.sp.empName).get_attribute("value")
        id_value = self.driver.find_element(*self.sp.empId).get_attribute("value")

        assert name_value == ""
        assert id_value == ""

        self.logger.info('******************** Finished: test_resetSearchForm ********************')

    def test_combination_filters(self):
        self.logger.info('******************** Running: test_combination_filters ********************')
        self.sp = SearchPIM(self.driver)
        self.sp.setName("admin 1234")
        self.sp.setId("0416")
        self.sp.clickSearch()
        status = self.sp.searchEmpByName("admin 1234")
        assert status == True

        self.logger.info('******************** Finished: test_combination_filters ********************')


    def test_negative_search(self):
        self.logger.info('******************** Running: test_negative_search ********************')
        self.sp = SearchPIM(self.driver)
        self.sp.setName("!!invalid!!")
        self.sp.clickSearch()
        sleep(2)
        assert self.sp.getNoOfRows() == 0
        self.logger.info('******************** Finished: test_negative_search ********************')

    def test_pagination(self):
        self.logger.info('******************** Running: test_pagination ********************')
        self.sp = SearchPIM(self.driver)
        self.sp.clickSearch()
        rows_page1 = self.sp.getTableRowTexts()
        self.sp.clickNextPg()
        rows_page2 = self.sp.getTableRowTexts()
        assert rows_page1 != rows_page2
        self.logger.info('******************** Finished: test_pagination ********************')