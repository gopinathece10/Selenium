import openpyxl
from selenium import webdriver
from Crome import Locators
l =Locators
class TestBase:
    def browser_launch(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Gopinath\PycharmProjects\Selenium\Crome\chromedriver.exe')

    def load_url(self,url):
        self.driver.get(url)

    def maximize(self):
        self.driver.maximize_window()

    def insert(self,element,value):
        element.send_keys(value)

    def click(self):
        self.driver = l.clk_T_C_box_id

    def get_data(self,row,column):
        excel_path =r"C:\Users\Gopinath\PycharmProjects\Selenium\Crome\test.xlsx"
        workbook = openpyxl.load_workbook(excel_path)
        sheet = workbook.active
        cell = sheet.cell(row,column)
        return cell.value
