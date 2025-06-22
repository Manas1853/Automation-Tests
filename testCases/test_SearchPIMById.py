from pageObjects.LoginPage import LoginPage
from pageObjects.AddPIMPage import AddPIM
from pageObjects.PIM_search import SearchPIM
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_0005_PIM_search:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()    #logger

    def test_searchEmpById(self,setup):
        self.logger.info('******************** searchEmpByName_0005 ********************')
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

        self.logger.info('********************* Starting Search PIM by ID Test ************************')

        self.sp = SearchPIM(self.driver)
        self.sp.setId('0379')
        self.sp.clickSearch()

        status= self.sp.searchEmpById('0379')
        assert True == status
        self.logger.info('****************************** searchEmpById_0005 Finished ******************************* ')


