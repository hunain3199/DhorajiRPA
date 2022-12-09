import csv
from _csv import writer


from selenium.webdriver import ActionChains
from selenium.webdriver.chrome import options
from selenium.webdriver.common import actions

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions
import time


options = webdriver.ChromeOptions()

options.add_argument("--enable-javascript")

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
def target_html():
    try:
        zip = driver.find_element(By.CLASS_NAME, "niche__grade niche__grade--a-minus").text
    except:
        zip = " "
        pass
    try:
        city_name = driver.find_element_by_xpath("//div[@class='postcard__parent']/a").text
    except:
        city_name = " "
        pass
    try:
        overall = driver.find_element(By.CLASS_NAME, "niche__grade niche__grade--a-minus").text
    except:
        overall = " "
        pass
    # try:
    #     public_school = chrome.find_element_by_xpath(
    #         "(//li[@class='ordered__list__bucket__item']//div/div/@class)[2]").text
    # except:
    #     public_school = " "
    #     pass
    # try:
    #     night_life = chrome.find_element_by_xpath(
    #         "(//li[@class='ordered__list__bucket__item']//div/div/@class)[6]").text
    # except:
    #     night_life = " "
    # try:
    #     diversity = chrome.find_element_by_xpath(
    #         "(//li[@class='ordered__list__bucket__item']//div/div/@class)[10]").text
    # except:
    #     diversity = " "
    # try:
    #     weather = chrome.find_element_by_xpath("(//li[@class='ordered__list__bucket__item']//div/div/@class)[14]").text
    # except:
    #     weather = " "
    # try:
    #     health = chrome.find_element_by_xpath("(//li[@class='ordered__list__bucket__item']//div/div/@class)[18]").text
    # except:
    #     health = " "
    # try:
    #     commute = chrome.find_element_by_xpath("(//li[@class='ordered__list__bucket__item']//div/div/@class)[22]").text
    # except:
    #     commute = " "
    # try:
    #     housing = chrome.find_element_by_xpath("(//li[@class='ordered__list__bucket__item']//div/div/@class)[4]").text
    # except:
    #     housing = " "
    # try:
    #     familes = chrome.find_element_by_xpath("(//li[@class='ordered__list__bucket__item']//div/div/@class)[8]").text
    # except:
    #     familes = " "
    # try:
    #     job = chrome.find_element_by_xpath("(//li[@class='ordered__list__bucket__item']//div/div/@class)[12]").text
    # except:
    #     job = " "
    # try:
    #     col = chrome.find_element_by_xpath("(//li[@class='ordered__list__bucket__item']//div/div/@class)[16]").text
    # except:
    #     col = " "
    # try:
    #     outdoor = chrome.find_element_by_xpath("(//li[@class='ordered__list__bucket__item']//div/div/@class)[20]").text
    # except:
    #     outdoor = " "
    with open('niche.csv', 'a', encoding='utf-8', newline='') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(
            [zip])
        f_object.close()

# APIKEY = "0762f811549cc97ddd1046d791fd6f59"
with open('niche_links.csv', 'r') as file:
    reader = csv.reader(file)
    for count, row in enumerate(reader):
        for i in row:
            try:
                try:

                    driver.get(i)
                    time.sleep(1)
                    element = driver.find_element(By.ID, 'px-captcha')
                    action = ActionChains(driver)
                    action.click_and_hold(element)
                    action.perform()
                    time.sleep(10)
                    action.release(element)
                    action.perform()
                    time.sleep(0.2)
                    action.release(element)
                    time.sleep(3)
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                    button = driver.find_element_by_xpath("//button[@class='report-card__toggle']")
                    button.click()
                except:

                    # element = driver.find_element(By.ID,'px-captcha')
                    # action = ActionChains(driver)
                    # action.click_and_hold(element)
                    # action.perform()
                    # time.sleep(10)
                    # action.release(element)
                    # action.perform()
                    # time.sleep(0.2)
                    # action.release(element)
                    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    # time.sleep(3)
                    # button = driver.find_element_by_xpath("//button[@class='report-card__toggle']")
                    # button.click()
                    continue

            except Exception as e:
                print(e)



            # target_html()



            #
            #
            # except Exception as e:
            # print(e)
            # with open('issues.csv', 'a', encoding='utf-8', newline='') as f_object:
            #     writer_object = writer(f_object)
            #     writer_object.writerow([driver.current_url])
            #     f_object.close()
            # try:
            #







































