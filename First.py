from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Gopinath\PycharmProjects\Selenium\Crome\chromedriver.exe')

driver.get('https://www.facebook.com/')

driver.maximize_window()
#print(driver.current_url)

txt_email = driver.find_element_by_id('email')
txt_email.send_keys('gopinath.m14@gmail.com')

txt_pass = driver.find_element_by_name('pass')
txt_pass.send_keys('gopinath14')

bt_login = driver.find_element_by_name('login')
bt_login.click()