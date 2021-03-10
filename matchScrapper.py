import requests  
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException,StaleElementReferenceException ,ElementNotInteractableException, NoSuchElementException,NoSuchAttributeException, TimeoutException, WebDriverException 

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


def events_number(driver):    
    ev_number = None
    _nb_pages = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[1]/div/div/div[2]/div/div[3]')
    ev_number = _nb_pages.text.split()[3]

    print("[INFO] Number of existing events : " ,ev_number)    
def get_events(driver):
  
    _tbodies = None 
    
    try:
        _table = driver.find_element_by_id("event_data")
    except StaleElementReferenceException:
        _table = driver.find_element_by_css_selector("#event_data")
    try:    
        _tbodies = _table.find_elements_by_tag_name('tbody') 
    except StaleElementReferenceException:
        _tbodies = _table.find_elements_by_tag_name('tbody') 

    return _tbodies

def extract_summary(event):
   
    
    _body = event
    

    DATE = ""
    TIME = "" 
    LEAGUE = "" 
    ROWS = ""
    HOME = "" 
    AWAY = ""
    attempts = 0
    while(attempts < 2 ):
        try : 
            _trs = _body.find_elements_by_tag_name('tr')
        except StaleElementReferenceException:
            _trs = _body.find_elements_by_tag_name('tr')
            
        ROWS = len(_trs)
        try:
            _tr_summary = _trs[0]
            td6 = _tr_summary.find_elements_by_tag_name('td')[6]
            date = _tr_summary.find_elements_by_tag_name('td')[0].text
            LEAGUE = _tr_summary.find_elements_by_tag_name('td')[4].text
            DATE = date.split()[0] + " " + date.split()[1] + " " +  date.split()[2]
        except StaleElementReferenceException:
            _tr_summary = _trs[0]
            td6 = _tr_summary.find_elements_by_tag_name('td')[6]
            date = _tr_summary.find_elements_by_tag_name('td')[0].text
            LEAGUE = _tr_summary.find_elements_by_tag_name('td')[4].text
            DATE = date.split()[0] + " " + date.split()[1] + " " +  date.split()[2]
        attempts+=1
    try : 
        TIME = date.split()[3]
    except IndexError  :
        TIME = date.split()[2]
    HOME = td6.find_element_by_tag_name('span').text
    try :
        _tr_away = _trs[1]
        _away = _tr_away.find_elements_by_tag_name('td')[0]
        AWAY = _away.find_element_by_tag_name('span').text
    except StaleElementReferenceException:
        _tr_away = _trs[1]
        _away = _tr_away.find_elements_by_tag_name('td')[0]
        AWAY = _away.find_element_by_tag_name('span').text        
    
    return {"rows" : ROWS , "DATE" : DATE , "TIME" : TIME , "LEAGUE" : LEAGUE , "HOME" : HOME , "AWAY" : AWAY}

def extract_scores(event):
    size = extract_summary(event)["rows"]
    _body = event
    ft_score1 = "" 
    ft_score2 = ""
    ht_score1 = ""
    ht_score2 = ""
    
    attempts = 0
    while attempts < 2 :
        _tr_1 = _body.find_elements_by_tag_name('tr')[0]
        attempts+=1
    try:
        _td1 = _tr_1.find_elements_by_tag_name('td')[8]
        ft_score1 = _td1.text
    except NoSuchElementException:
        pass
    except StaleElementReferenceException : 
        _td1 = _tr_1.find_elements_by_tag_name('td')[8]
        ft_score1 = _td1.text
    try:    
        _tr_2 = _body.find_elements_by_tag_name('tr')[1]
        try:
            _td2 = _tr_2.find_elements_by_xpath('td')[1]
            ft_score2 = _td2.text
        except NoSuchElementException:
            pass
    except StaleElementReferenceException:
        _tr_2 = _body.find_elements_by_tag_name('tr')[1]
        try:
            _td2 = _tr_2.find_elements_by_xpath('td')[1]
            ft_score2 = _td2.text
        except NoSuchElementException:
            pass
    if size == 4 :
        try:
            _tr_3 = _body.find_elements_by_tag_name('tr')[2]
            _tr_4 = _body.find_elements_by_tag_name('tr')[3]
            try:
                _td3 = _tr_3.find_elements_by_tag_name('td')[2]
                ht_score1 = _td3.text        
            except NoSuchElementException:
                pass
            try:
                _td4 = _tr_4.find_elements_by_tag_name('td')[1]
                ht_score2 = _td4.text
            except NoSuchElementException:
                pass
        except StaleElementReferenceException:
            _tr_3 = _body.find_elements_by_tag_name('tr')[2]
            _tr_4 = _body.find_elements_by_tag_name('tr')[3]
            try:
                _td3 =  _tr_3.find_elements_by_tag_name('td')[2]
                ht_score1 = _td3.text        
            except NoSuchElementException:
                pass
            try:
                _td4 = _tr_4.find_elements_by_tag_name('td')[1]
                ht_score2 = _td4.text
            except NoSuchElementException:
                pass
    return  {"FT" : {"1" : ft_score1 , "2" : ft_score2} ,
     "HT" : {"1" : ht_score1 , "2" : ht_score2}
    }

def current_odds(event):
    ft_spread_1 = ""
    ft_spread_2 = ""  
   

    ft_odds_1 = "" 
    ft_odds_2 = ""  
    

    _body = event
    #FT
    #Spread
    attempts = 0
    while attempts < 2 :
    
        _tr_1 = _body.find_elements_by_tag_name('tr')[0]
        _tr_2 = _body.find_elements_by_tag_name('tr')[1]

        _td_1 = _tr_1.find_elements_by_tag_name('td')[9]
        attempts+=1
    try:
        _ft_spr1 = _td_1.find_element_by_tag_name('a')
        ft_spread_1 = _ft_spr1.text
    except NoSuchElementException:
        pass
    _td_2 = _tr_2.find_elements_by_tag_name('td')[2]
    try:
        _ft_spr2 = _td_2.find_element_by_tag_name('a')
        ft_spread_2 = _ft_spr2.text
    except NoSuchElementException:
        pass
    #Odds
    _td_3 = _tr_1.find_elements_by_tag_name('td')[10]
    try:
        _ft_odd1 = _td_3.find_element_by_tag_name('a')
        ft_odds_1 = _ft_odd1.text
    except NoSuchElementException:
        pass
    _td_4 = _tr_2.find_elements_by_tag_name('td')[3]
    try:
        _ft_odd2 = _td_4.find_element_by_tag_name('a')
        ft_odds_2  = _ft_odd2.text
    except NoSuchElementException:
        pass
    return {"SPREAD" : {"1" : ft_spread_1 , "2" : ft_spread_2},"ODDS" :  {"1" : ft_odds_1 , "2" : ft_odds_2} }

def open_odds(event):
    ft_spread_1 = ""
    ft_spread_2 = ""
 

    ft_odds_1 = "" 
    ft_odds_2 = ""  
    

    
    _body = event
    #FT
    #Spread
    attempts = 0
    while(attempts < 2 ) :

        _tr_1 = _body.find_elements_by_tag_name('tr')[0]
        _tr_2 = _body.find_elements_by_tag_name('tr')[1]

        _td1 = _tr_1.find_elements_by_tag_name('td')[11]
        attempts+=1
    try:
        _ft_spr1 = _td1.find_element_by_tag_name('a')
        ft_spread_1 = _ft_spr1.text
    except NoSuchElementException:
        pass
    _td2 = _tr_2.find_elements_by_tag_name('td')[4]
    try:
        _ft_spr2 = _td2.find_element_by_tag_name('a')
        ft_spread_2 = _ft_spr2.text
    except NoSuchElementException:
        pass
    #ODDS
    _td3 = _tr_1.find_elements_by_tag_name('td')[12]
    try:
        _ft_odd1 = _td3.find_element_by_tag_name('a')
        ft_odds_1 = _ft_odd1.text
    except NoSuchElementException:
        pass
    _td4 = _tr_2.find_elements_by_tag_name('td')[5]
    try:
        _ft_odd2 = _td4.find_element_by_tag_name('a')
        ft_odds_2 = _ft_odd2.text
    except NoSuchElementException:
        pass
    return {"SPREAD" :  {"1" : ft_spread_1 , "2" : ft_spread_2},"ODDS" : {"1" : ft_odds_1 , "2" : ft_odds_2} }
def total(event):
    total_current = ""
    total_open = ""
  
    _body = event

    attempts = 0
    while(attempts < 2 ) :
        _tr = _body.find_elements_by_tag_name('tr')[0]
    
        #Total --> Current
        _td1 = _tr.find_elements_by_tag_name('td')[16]
        attempts+=1
    try:
        _total_curr = _td1.find_element_by_tag_name('a')
        total_current = _total_curr.text
    except NoSuchElementException:
        pass
    #Total --> Open 
    _td2 = _tr.find_elements_by_tag_name('td')[17]
    try:
        _total_opn = _td2.find_element_by_tag_name('a')
        total_open = _total_opn.text
    except NoSuchElementException:
        pass
    return {"CURRENT" : total_current , "OPEN" : total_open}

def over_under(event):
    current_over = ""
    current_under = ""
    open_over = ""
    open_under = ""

    
    _body = event
    

    attempts = 0 
    while(attempts < 2 ) :
    
        _tr1 = _body.find_elements_by_tag_name('tr')[0] #over
        _tr2 = _body.find_elements_by_tag_name('tr')[1] #under
        attempts+=1
    #Current
    #Over
    _td1 = _tr1.find_elements_by_tag_name('td')[20]
    try:
        _curr_over = _td1.find_element_by_tag_name('a')
        current_over = _curr_over.text
    except NoSuchElementException:
        pass
    #Under
    _td2 = _tr2.find_elements_by_tag_name('td')[9]
    try:   
        _curr_under = _td2.find_element_by_tag_name('a')
        current_under = _curr_under.text
    except NoSuchElementException:
        pass
    #Open
    _td3 = _tr1.find_elements_by_tag_name('td')[21]
    try:
        _opn_over = _td3.find_element_by_tag_name('a')
        open_over = _opn_over.text
    except NoSuchElementException:
        pass
    _td4 = _tr2.find_elements_by_tag_name('td')[10]
    try:
        _opn_under = _td4.find_element_by_tag_name('a')
        open_under = _opn_under.text
    except NoSuchElementException:
        pass   
    return { "CURRENT" : {"OVER" : current_over , "UNDER" : current_under},
    "OPEN" : {"OVER" : open_over , "UNDER" : open_under}
    }
def moneyline(event):
    
    _body = event
    
    attempts = 0
    while(attempts < 2 ) :

        _tr = _body.find_elements_by_tag_name('tr')[0]
        _td = _tr.find_elements_by_tag_name('td')[24]
        _td2 = _tr.find_elements_by_tag_name('td')[25]
        attempts+=1

    curr_1 = ""
    curr_x = ""
    curr_2 = ""

    open_1 = ""
    open_x = ""
    open_2 = ""

    #Current
    try:
        _ahrefs = _td.find_elements_by_tag_name('span')
        _acurr1 = _ahrefs[0].find_element_by_tag_name('a')
        _acurrx = _ahrefs[1].find_element_by_tag_name('a')
        _acurr2 = _ahrefs[2].find_element_by_tag_name('a')
        curr_1 = _acurr1.text
        curr_x = _acurrx.text
        curr_2 = _acurr2.text
    except NoSuchElementException:
        pass
    
    try:
        #Open
        _ahrefs2 = _td2.find_elements_by_tag_name('span')
        _opn1 = _ahrefs2[0].find_element_by_tag_name('a')
        _opnx = _ahrefs2[1].find_element_by_tag_name('a')
        _opn2 = _ahrefs2[2].find_element_by_tag_name('a')

        open_1 = _opn1.text
        open_x = _opnx.text
        open_2 = _opn2.text

    except NoSuchElementException:
        pass
    

    
    return {"CURRENT" : { "1" : curr_1 , "X" : curr_x , "2" : curr_2}, 
        "OPEN" : {"1" : open_1 , "X" : open_x , "2" : open_2}
    }

