import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r'C:\Users\Gopinath\PycharmProjects\Selenium\Crome\chromedriver.exe')
driver.get('https://www.flipkart.com/')  # login

driver.maximize_window()  # Maximize window
print(driver.current_url)
print(driver.title)

close_login = driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']")
close_login.click()
#home_fur1 = driver.find_element_by_class_name("RWB9Wm")

time.sleep(10)
home_Fur = driver.find_element_by_xpath("(//span[@class='_2I9KP_'])[6]")

action = ActionChains(driver)
action.move_to_element(home_Fur).perform()
home_Fur.click()

Bath = driver.find_element_by_xpath("(//a[@title='Bath Towels'])[1]")
Bath.click()