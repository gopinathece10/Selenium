import time

from selenium import webdriver
#from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path=r'C:\Users\Gopinath\PycharmProjects\Selenium\Crome\chromedriver.exe')
driver.get('https://www.amazon.in/')  # login

driver.maximize_window()  # Maximize window
print(driver.current_url)
print(driver.title)

login1 = driver.find_element_by_class_name('nav-line-1-container')
login1.click()
#a = ActionChains
#time.sleep(10)

#login2 = driver.find_element_by_xpath("(//span[@class='nav-action-inner'])[1]")
#login2.click()
#time.sleep(10)

signin = driver.find_element_by_name('email')
signin.send_keys('gopinathece10@gmail.com')
Continue = driver.find_element_by_id('continue')
Continue.click()

password = driver.find_element_by_name('password')
password.send_keys('********')

login = driver.find_element_by_id('signInSubmit')
login.click()

