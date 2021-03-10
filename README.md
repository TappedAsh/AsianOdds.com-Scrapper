# AsianOdds.com-Scrapper
This is python scrapper i build that scrappes data from asianodds.com past games and uses your login account 



Requirements installation : 


1- download chromedriver associated with your chrome browser version for selenium from the following link : https://sites.google.com/a/chromium.org/chromedriver/downloads


2- create a directory named seleniumDrivers on root directory and put the driver on this directory 


3- execute the following commands to install required libraries : 
    pip install xlsxwriter 
    pip install xlwt
    pip install selenium
    pip install requests
    pip install argparse
    
   
Usage : 

python main.py -f name-of-output-file.xlsx -u email@email.com -p password

or 

python main.py --filename name-of-output-file.xlsx --username --pasword password
