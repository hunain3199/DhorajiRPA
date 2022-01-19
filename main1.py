from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='chromedriver.exe')
#open webpage on chrome driver
driver.get('https://www.olx.com.pk/')

time.sleep(5)

#close webpage on chrome driver
# driver.close()

