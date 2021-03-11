This is a small scrapping script i built based on selenium to extract pastgames odds soccer data from asianodds.com using login and puts them into an excel output file using chrome driver

Requirements installation : 


1- create a directory on root folder named "seleniumDrivers"

2- download chrome driver associated with chrome browser version from the following link : https://sites.google.com/a/chromium.org/chromedriver/downloads

3- execute the following commands to install required libraries :

      pip install xlwrt
      pip install xlsxwriter
      pip install argparse 
      pip install selenium
      pip install requests 



Usage : 


    python main.py -f outputfile.xlsx -u email@email.com -p password 

    or 

    python main.py --filename outputfile.xlsx --username email@mail.com --password pass

PS: don't scroll the browser window opened by the script becaus it will affect the scrapping behaviour .
