from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.request
import time
import pandas as pd
import csv
from csv import writer


driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.pakwheels.com/used-cars/search/-/")
time.sleep(2)

detail = driver.find_elements_by_xpath("//div[@class ='search-title']/a")
for i in detail:
    print(i.get_attribute('href'))

flag = True

while flag:
    try:
        btn = driver.find_element_by_xpath("//a[@rel='next']")
        btn.click()
        time.sleep(5)
        detail = driver.find_elements_by_xpath("//div[@class ='search-title']/a")
        for i in detail:
            print(i.get_attribute('href'))

    except:
        flag = False


# btn = driver.find_element_by_xpath("//button[@class = 'align-right primary slidedown-button']")
# btn.click()
# driver.implicitly_wait(10)




#     with open('decided.csv', 'a', newline='') as f_object:
#         writer_object = writer(f_object)
#         writer_object.writerow([i.get_attribute('href')])
#         f_object.close()
# # # Pagination Links
# #     # Pagination Links
# button = driver.find_element_by_xpath("//button[@class = 'close']")
# flag = True
#
# while flag:
#     try:
#         button = driver.find_element_by_xpath("//a[@rel = 'next']")
#         button.click()
#
#         driver.implicitly_wait(10)
#
#         for i in detail:
#             print(i.get_attribute('href'))
#             # with open('decided.csv', 'a', newline='') as f_object:
#             #     writer_object = writer(f_object)
#             #     writer_object.writerow([i.get_attribute('href')])
#             #     f_object.close()
#
#
#     except:
#         flag = False
#         pass