from selenium.webdriver.common.by import By

from Crome import Locators  as l


class Login_page():
    def __init__(self,driver):
        self.txt_user_name = driver.find_element(By.ID,l.txt_user_name_id)
        self.txt_Pass = driver.find_element(By.ID,l.txt_Pass_id)
        self.txt_Confirm_pass = driver.find_element(By.ID,l.txt_Confirm_pass_id)
        self.txt_full_name = driver.find_element(By.ID, l.txt_full_name_id)
        self.txt_email_add = driver.find_element(By.ID,l.txt_email_add_id)
        self.txt_cap_txt = driver.find_element(By.ID,l.txt_cap_txt_id)
        self.clk_T_C_box = driver.find_element(By.ID,l.clk_T_C_box_id)
        self.bt_register = driver.find_element(By.ID,l.bt_register_id)

    def get_txt_username(self):
        return self.txt_user_name
    def get_txt_password(self):
        return self.txt_Pass
    def get_txt_confirmpass(self):
        return self.txt_Confirm_pass
    def get_txt_full_name(self):
        return self.txt_full_name
    def get_txt_email(self):
        return self.txt_email_add
    def get_txt_cap(self):
        return self.txt_cap_txt
    def clk_tcbox(self):
        return self.clk_T_C_box
    def get_bt_reg(self):
        return self.bt_register

