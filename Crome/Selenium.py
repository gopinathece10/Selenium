#from selenium import webdriver
from Crome.Loginpage import Login_page
from Crome.Test_base import TestBase

t = TestBase()
t.browser_launch()
t.load_url('https://adactin.com/HotelApp/Register.php')  #login
t.maximize()
p = Login_page(t.driver)
t.insert(p.get_txt_username(),t.get_data(1,2))
t.insert(p.get_txt_password(),t.get_data(2,2))
t.insert(p.get_txt_confirmpass(),t.get_data(3,2))
t.insert(p.get_txt_full_name(),t.get_data(4,2))
t.insert(p.get_txt_email(),t.get_data(5,2))
t.insert(p.get_txt_cap(),t.get_data(6,2))
t.click(p.clk_T_C_box())
t.click(p.get_bt_reg())
