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

            time.sleep(2)
            try:
                summary = driver.find_element_by_xpath("//a[@id = 'subtab_summary']").get_attribute("href")
                print(summary)
                df = pd.read_html(summary)
                df[0].to_csv("summary.csv" , mode='a',header =  index = False)

            except Exception as e:
                print(e)
                pass
            # try:
            #     contacts = driver.find_element_by_xpath("//a[@id = 'subtab_contacts']").click()
            #     pd.read_html("https://pa1.swindon.gov.uk" + "")
            # except:
            #     pass
            # try:
            #     dates = driver.find_element_by_xpath("//a[@id = 'subtab_dates']").click()
            #     pd.read_html("https://pa1.swindon.gov.uk"+)
            # except:
            #     pass
            #
            # try:
            #     constraints = driver.find_element_by_xpath("//a[@id = 'tab_constraints']").click()
            #     pd.read_html("https://pa1.swindon.gov.uk"+)
            # except:
            #     pass
            # try:
            #     documents = driver.find_element_by_xpath("//a[@id = 'tab_documents']").click()
            #
            # except:
            #     pass









            driver.close()