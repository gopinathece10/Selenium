from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'C:\Users\Gopinath\PycharmProjects\Selenium\Crome\chromedriver.exe')
driver.get('https://mail.jasmin-infotech.com/')

driver.maximize_window()
print(driver.current_url)
print(driver.title)

e = driver.find_element_by_name('username')

e.send_keys("gopinath.m@jasmin-infotech.com")

e1 = driver.find_element_by_name("password")

e1.send_keys("navyanavjith")

e2 = driver.find_element_by_xpath("//input[@type='submit']")
e2.click()

print(driver.current_url)

#driver.set_page_load_timeout("10")
e3 = driver.find_element_by_id("DWT36_dropdown")
e3.click()

#driver.set_page_load_timeout("10")

#e4 = driver.find_element_by_id("logOff")
#e4.click()

e5 = driver.find_element_by_id("zb__App__Calendar_title")
e5.click()