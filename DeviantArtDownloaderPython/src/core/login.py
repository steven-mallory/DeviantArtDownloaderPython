from src import config
from selenium import webdriver #base
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import json

LOGIN_URL = "https://www.deviantart.com/users/login"
COOKIES_FILE = "cookies.json"

#creates the driver that our code talks to

#for google
try:
    options = webdriver.firefox.options.Options()
    #options.add_argument('--headless=new')
    driver = webdriver.Firefox(options=options)
    
    driver.get(LOGIN_URL)
    time.sleep(2)
    #login

    #dump cookies
    cookies = driver.get_cookies()
    with open(COOKIES_FILE, 'w') as f:
        json.dump(cookies, f)
    print("Downloaded cookies\n")
finally:
    driver.quit()
