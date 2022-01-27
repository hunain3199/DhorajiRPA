from selenium import webdriver
import time
import pandas as pd

import csv
with open('CSVFILE.csv', 'r') as file:
    reader = csv.reader(file)
    for count, row in enumerate(reader):
        for i in row:
            driver = webdriver.Chrome(executable_path='chromedriver.exe')
            driver.get(i)
            
            # time.sleep(2)





            driver.close()