from time import sleep
from selenium.webdriver.common.by import By

class SearchPIM:

    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(5)

        self.empName = (By.XPATH, "//label[text()='Employee Name']/parent::div/following-sibling::div/div/div/input")
        self.empId = (By.XPATH,"//label[text()='Employee Id']/parent::div/following-sibling::div/input")
        self.empStatus = (By.XPATH, "//label[text()='Employment Status']/parent::div/following-sibling::div/div/div")
        self.include = (By.XPATH,"//label[text()='Include']/parent::div/following-sibling::div/div/div")
        self.supervisorName = (By.XPATH,"//label[text()='Supervisor Name']/parent::div/following-sibling::div/div/div/input")
        self.jobTitle = (By.XPATH,"//label[text()='Job Title']/parent::div/following-sibling::div/div/div")
        self.subUnit= (By.XPATH,"//label[text()='Sub Unit']/parent::div/following-sibling::div/div/div")
        self.reset = (By.XPATH, "//button[text()=' Reset ']")
        self.search = (By.XPATH,"//button[text()=' Search ']")
        self.tblSearchResult = (By.XPATH, "//div[@class='oxd-table-body']")
        self.tblRow = (By.XPATH, "//div[@class='oxd-table-card']")
        self.nextPage = (By.XPATH,"//i[@class='oxd-icon bi-chevron-right']")


    def setName(self,name):
        self.driver.find_element(*self.empName).send_keys(name)   # * is to unpack the tuple

    def setId(self,id):
        self.driver.find_element(*self.empId).send_keys(id)

    def clickSearch(self):
        self.driver.find_element(*self.search).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(*self.tblRow))

    def clickReset(self):
        self.driver.find_element(*self.reset).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements(*self.tblRow))

    def searchEmpByName(self, name):
        flag = False
        for i in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element(*self.tblSearchResult)
            eFName = table.find_element(By.XPATH,"//div[@role='cell'][3]/div").text
            eLName = table.find_element(By.XPATH,"//div[@role='cell'][4]/div").text
            eName = (eFName +' '+ eLName).lower()

            if eName == name.lower():
                flag = True
                break
        return flag

    def searchEmpById(self, id):
        flag = False
        for i in range(1,self.getNoOfRows()+1):
            table = self.driver.find_element(*self.tblSearchResult)
            eId = table.find_element(By.XPATH,"//div[@role='cell'][2]/div").text

            if eId == id:
                flag = True
                break
        return flag


    def clickNextPg(self):
        next_button = self.driver.find_element(*self.nextPage)
        if next_button.is_enabled():
            next_button.click()

    def getTableRowTexts(self):
        rows = self.driver.find_elements(*self.tblRow)
        texts = []
        for row in rows:
            texts.append(row.text)
        return texts