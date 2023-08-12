#source/bin activate

import time
import pandas as pd
import csv
import random
from csv import writer
from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def start(url):
    browser.get(url)
    sleep()
    #clickOnLeague("""Eredivisie""")
    #sleep()
    #previously li1
    #clickOnResults("li2")
    #sleep()
    clickOnMoreButton()
    sleep()
    results = getResults("event__match")
    expandResult(results)
    

def clickOnLeague(elementName):
    l = browser.find_element(By.PARTIAL_LINK_TEXT, elementName)
    l.click()

def clickOnResults(elementID):
    l = browser.find_element(By.ID, elementID)
    l.click()

def clickOnMoreButton():
    while True:
        try:
            if browser.find_element(By.CLASS_NAME, "event__more").is_enabled():
                l = browser.find_element(By.CLASS_NAME, "event__more")
                browser.execute_script("arguments[0].click();", l)
                sleep()
        except NoSuchElementException:
            break
        
def getResults(element):
    return browser.find_elements(By.CLASS_NAME, element)

def expandResult(results):
    count = 1
    for result in results:
        count += 1
        # increase number where it stuck
        if count > 62:
            sleep()
            window_before = browser.window_handles[0]
            browser.execute_script("arguments[0].click();", result)
            sleep()
            window_after = browser.window_handles[1]
            browser.switch_to.window(window_after)
            sleep()
            getHalfScores("smv__incidentsHeader")
            #clickStats("tabs__group","tabs__tab")
            clickStats("filter__group","filter__filter")
            #click1stHalf("tabs__detail--sub","subTabs__tab")
            click1stHalf("detail__subFilter","subFilter__filter")
            saveData()
            browser.switch_to.window(window_before)


def clickStats(group,tab):
    tabs = []
    tabNav = browser.find_element(By.CLASS_NAME, "detail__filter")
    tabBar = tabNav.find_element(By.CLASS_NAME, group)
    tabs = tabBar.find_elements(By.CLASS_NAME, tab)
    browser.execute_script("arguments[0].click();", tabs[1])
    sleep()
    
def click1stHalf(group,tab):
    tabs = []
    tabBar = browser.find_element(By.CLASS_NAME, group)
    tabs = tabBar.find_elements(By.CLASS_NAME, tab)
    browser.execute_script("arguments[0].click();", tabs[1])    
    sleep()
    collect1stHalfData()
    
def getHalfScores(elementName):
    halfBar = []
    halfBar = browser.find_elements(By.CLASS_NAME, elementName)
    data[16] = halfBar[0].text[9:10]
    data[17] = halfBar[0].text[13:14]
    data[18] = halfBar[1].text[9:10]
    data[19] = halfBar[1].text[13:14]
    
def collect1stHalfData():
    rows = []
    rows = browser.find_elements(By.CLASS_NAME, "stat__row")
    homeArray = []
    awayArray = []
    for row in rows:
        category = row.find_element(By.CLASS_NAME, "stat__category")
        if category.find_element(By.CLASS_NAME, "stat__categoryName").text in titles[:8]:
            homeArray.append(category.find_element(By.CLASS_NAME, "stat__homeValue").text)
            awayArray.append(category.find_element(By.CLASS_NAME, "stat__awayValue").text)
    data[:8] = homeArray
    data[8:16] = awayArray
    data[0] = data[0][:-1]
    data[8] = data[8][:-1]
    browser.close()

def saveData():
    with open('super-lig-22-23.csv', 'a') as f_object:
        global data
        missingElement = False
        for element in data:
            if str(element).isnumeric and str(element) != '':
                continue
            else:
                missingElement = True
                break
            
        if missingElement == False and len(data) == 20:
            writer_object = writer(f_object)
            writer_object.writerow(data)
            
    data = [0] * 20    
    f_object.close()
    
def sleep():
    time.sleep(random.randint(2,5))
    
if __name__ == '__main__':
    
    driverPath = '/usr/local/Caskroom/chromedriver/89.0.4389.23/chromedriver'
    binaryPath = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
    options = webdriver.ChromeOptions()
    options.binary_location = binaryPath
    browser = webdriver.Chrome(executable_path=driverPath, options=options)

    #check stat titles
    titles = ["Ball Possession", "Goal Attempts", "Shots on Goal", "Shots off Goal", "Corner Kicks", "Total Passes", "Attacks", "Dangerous Attacks", "Home Goals", "Away Goals"]

    halfTitles = [ "1st Half Home Ball Possession", "1st Half Home Goal Attempts", "1st Half Home Shots on Goal", "1st Half Home Shots off Goal", "1st Half Home Corner Kicks", "1st Half Home Total Passes", "1st Half Home Attacks", "1st Half Home Dangerous Attacks", "1st Half Away Ball Possession", "1st Half Away Goal Attempts", "1st Half Away Shots on Goal", "1st Half Away Shots off Goal", "1st Half Away Corner Kicks", "1st Half Away Total Passes", "1st Half Away Attacks", "1st Half Away Dangerous Attacks", "1st Half Home Goals", "1st Half Away Goals", "2nd Half Home Goals", "2nd Half Away Goals"]
    data = [0] * len(halfTitles)
    
    start("https://www.flashscore.com/football/turkey/super-lig-2022-2023/results/")
    
