from time import sleep
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By

class AddPIM:
    # textbox_username = "//input[@name='username']"
    # textbox_password = "//input[@name='password']"
    # button_login_xpath='//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    # class_to_logout = "oxd-userdropdown-tab"
    # link_to_logout='Logout'

    class_pim_tab = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    btn_add_xpath = "//button[text()=' Add ']"
    tx_emp_name_xpath="//input[@placeholder='Type for hints...']"
    tx_emp_id_xpath= "//label[contains(text(),'Employee Id')]/parent::div/following-sibling::div/input"
    emp_sts_xpath = "//div[text()='-- Select --']"
    include_xpath = "//label[contains(text(),'Include')]/parent::div/following-sibling::div/div/div"
    superviser_name_xpath = "//label[contains(text(),'Supervisor Name')]/parent::div/following-sibling::div/div/div"
    job_title_xpath = "//label[contains(text(),'Job Title')]/parent::div/following-sibling::div/div/div"
    sub_unit_xpath = "//div[text()='OrangeHRM']"
    btn_reset_xpath = "//button[@type='reset']"

    btn_save_xpath = "//button[text()=' Save ']"
    tx_firstname = "firstName"
    tx_lastname = 'lastName'
    tx_midname = 'middleName'
    btn_emplist_xpath = "//a[text()='Employee List']"
    nicknm_xpath = "//label[contains(text(),'Nickname')]/parent::div/following-sibling::div/input"
    male_checkbox_xpath = "//label[text()='Male']"
    female_checkbox_xpath = "//label[text()='Female']"
    otherid_xpath = "//label[contains(text(),'Other Id')]/parent::div/following-sibling::div/input"
    driver_lncs_xpath = '''//label[contains(text(),"Driver's License Number")]/parent::div/following-sibling::div/input'''
    # lncs_expdate_xpath = "//input[@placeholder='yyyy-mm-dd']"
    lncs_expdate_xpath = "//label[contains(text(),'License Expiry Date')]/parent::div/following-sibling::div/div/div/input"
    nationality_xpath = "//label[text()='Nationality']/following::div[1]"
    nationality_ddw= "//div[@role='listbox']//span[text()='Afghan']"
    marital_sts_xpath = "//label[text()='Marital Status']/following::div[1]"
    marital_sts_ddw = "//div[@role='listbox']//span[text()='Single']"
    dob_xpath= "//label[contains(text(),'Date of Birth')]/parent::div/following-sibling::div/div/div/input"
    # save2_xpath = "//button[text()=' Save ']"





    def __init__(self,driver):
        self.driver = driver

    def clickonPIM(self):
        self.driver.find_element(By.XPATH,self.class_pim_tab).click()

    def addEmp(self):
        self.driver.find_element(By.XPATH,self.btn_add_xpath).click()

    def setFName(self, fname):
        self.driver.find_element(By.NAME,self.tx_firstname).send_keys(fname)

    def setLName(self, lname):
        self.driver.find_element(By.NAME,self.tx_lastname).send_keys(lname)

    def setMName(self, mname):
        self.driver.find_element(By.NAME,self.tx_midname).send_keys(mname)

    def setSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element(By.XPATH,self.male_checkbox_xpath).click()
        elif gender == 'Female':
            self.driver.find_element(By.XPATH, self.female_checkbox_xpath).click()

    def setOtherId(self, otherid):
        self.driver.find_element(By.XPATH, self.otherid_xpath).send_keys(otherid)

    def setDriverLncs(self, lcns_no):
        self.driver.find_element(By.XPATH,self.driver_lncs_xpath).send_keys(lcns_no)

    def setLcnsExpDate(self, expDate):
        self.driver.find_element(By.XPATH, self.lncs_expdate_xpath).send_keys(expDate)

    def setNationality(self, nationality):
        # self.driver.find_element(By.XPATH, self.nationality_class).click()
        # drop = Select(self.driver.find_element(By.XPATH, self.nationality_class))
        # drop.select_by_visible_text(nationality)
        self.driver.find_element(By.XPATH, self.nationality_xpath ).click()
        sleep(1)
        self.driver.find_element(By.XPATH, self.nationality_ddw).click()

    def setMaritalSts(self, status):
        # self.driver.find_element(By.XPATH, self.marital_sts_xpath).click()
        # drop = Select(self.driver.find_element(By.XPATH, self.marital_sts_xpath))
        # drop.select_by_visible_text(status)
        self.driver.find_element(By.XPATH, self.marital_sts_xpath).click()
        sleep(1)
        self.driver.find_element(By.XPATH, self.marital_sts_ddw).click()

    def setDob(self, dob):
        self.driver.find_element(By.XPATH, self.dob_xpath).send_keys(dob)

    def setSave2(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()

    def emplist(self):
        self.driver.find_element(By.XPATH,self.btn_emplist_xpath).click()

