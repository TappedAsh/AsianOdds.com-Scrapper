import matchScrapper
import excelexporter
import requests  
import xlsxwriter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException, ElementNotInteractableException, NoSuchElementException,NoSuchAttributeException, TimeoutException, WebDriverException 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import argparse
import xlwt

row  = 4

ap = argparse.ArgumentParser()
ap.add_argument("-f","--filename", required = True , help = "Write the output filename")
ap.add_argument("-u","--username", required = True , help = "Write login email")
ap.add_argument("-p","--password", required = True , help = "Write password")
args = vars(ap.parse_args())
filename = args["filename"]
user = args["username"]
passwd = args["password"]
input_date = args["date"]
link = "https://asianodds.com"

excelexporter.create_workbook(filename)
workbook = excelexporter.open_workbook(filename)
worksheet = excelexporter.write_worksheet(workbook)


#options = Options()
#options.headless = True
driver = webdriver.Chrome()
driver = webdriver.Chrome(executable_path="/seleniumDrivers/chromedriver")

print(driver.get_cookies())

timeout = 10
url = link
driver.get(url + "/en/profile/login")
try:
    WebDriverWait(driver , timeout).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='page-content']")))
    email = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div/div[1]/div/div[2]/form/div[2]/input")
    password = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div/div[1]/div/div[2]/form/div[3]/input")

    email.send_keys(user)
    password.send_keys(passwd)
    submit = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div/div[1]/div/div[2]/form/div[4]/div/div[1]/div/button')
    submit.click()

    navbar = driver.find_element_by_xpath("/html/body/div[4]/div[1]")
    navbar.click()

    past_games = driver.find_element_by_xpath('/html/body/div[5]/div/ul[1]/li[4]/a')
    past_games.click()
    sleep(5)


    
    
   
    
      
except TimeoutException:
    print("Timeout filling login form")

pageIndex = 2

try:
    driver.set_window_size(1552, 840)
    WebDriverWait(driver , timeout).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='page-content']")))
    sleep(4)
    next = True
    while next  : 
        
        WebDriverWait(driver , timeout).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='page-content']")))
     
        #_table = driver.find_element_by_xpath('//*[@id="event_data"]/div[1]/div/table')
        _tbodies = matchScrapper.get_events(driver) 

        
        i = 1
        for e in _tbodies:
            print("[INFO][Scrapper] : Extracting event number : ",i)    
            #Scrapping events Data
            try:

                summary = matchScrapper.extract_summary(e)
                print("[INFO][Scrapper][MATCH]: Home : ",summary["HOME"]," AWAY : ",summary["AWAY"])
                print("[INFO][Scrapper][LEAGUE] : ",summary["LEAGUE"])
                scores = matchScrapper.extract_scores(e)
                current_odds = matchScrapper.current_odds(e)
                open_odds = matchScrapper.open_odds(e)
                total = matchScrapper.total(e)
                over_under = matchScrapper.over_under(e)
                money_line = matchScrapper.moneyline(e)
                    #Writing into excel 
              
                excelexporter.write_summary(worksheet , summary , row)
                excelexporter.write_scores(worksheet , scores , row)
                excelexporter.write_current(worksheet , current_odds , row)
                excelexporter.write_open_odds(worksheet , open_odds , row)
                excelexporter.write_total(worksheet , total , row)
                excelexporter.write_overunder(worksheet , over_under , row)
                excelexporter.write_moneyline(worksheet , money_line , row)
                
            except StaleElementReferenceException:
                sleep(1)
                pass
            row+=1
            i+=1
           
        try:
            #pg_nav = driver.find_element_by_xpath("/html/body/div[6]/div/div/div[1]/div/div/div[2]/div/div[2]/div/nav/ul")
            driver.execute_script("window.scrollTo(0,1411.199951171875)")
            sleep(0.5)

            #Click on next page
            driver.find_element(By.LINK_TEXT, "›").click()
            
            print("Next Page...")
            sleep(1)
            
            

        except ElementNotInteractableException:  
            print("Couldn't press next button")
            next = False 
            pass
        except ElementClickInterceptedException:
            print("Couldn't press next button")

            next = False 
            pass
        except NoSuchElementException:
            print("Couldn't press next button")
            next = False
            pass
        
except TimeoutException:
    print("Timeout Loading page")
    driver.quit()
driver.quit()
workbook.close()