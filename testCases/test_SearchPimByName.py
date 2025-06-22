from pageObjects.LoginPage import LoginPage
from pageObjects.AddPIMPage import AddPIM
from pageObjects.PIM_search import SearchPIM
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_0004_PIM_search:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()    #logger

    def test_searchEmpByName(self,setup):
        self.logger.info('******************** searchEmpByName_0004 ********************')
        self.driver = setup
        self.driver.get(self.baseURL)

        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)

        self.lp.clickLogin()

        self.logger.info('********************* Login Successful ************************')

        self.ap = AddPIM(self.driver)
        self.ap.clickonPIM()

        self.logger.info('********************* Starting Search PIM by Name Test ************************')

        self.sp = SearchPIM(self.driver)
        self.sp.setName('123 123 123')
        self.sp.clickSearch()

        status= self.sp.searchEmpByName('123 123 123')
        assert True == status
        self.logger.info('****************************** searchEmpByName_0004 Finished ******************************* ')


