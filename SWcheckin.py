import time
import sys
import os
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.add_argument("--headless")
opts.add_argument("--window-size=1920x1080")
opts.add_argument("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")
driver = webdriver.Chrome(chrome_options=opts)
if len(sys.argv) is not 4:
    print "Error... Please supply confirmation number, first name, and last name"
    sys.exit()
else:
    confirmationNumber = str(sys.argv[1])
    passengerFirstName = str(sys.argv[2])
    passengerLastName = str(sys.argv[3])
    date = time.strftime("%Y%m%d-%I%M")
try:
    driver.get('https://www.southwest.com/air/check-in/review.html?confirmationNumber='+confirmationNumber+'&passengerFirstName='+passengerFirstName+'&passengerLastName='+passengerLastName)
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[2]/div/div[2]/div/section/div/div/div[3]/button').click()
    if ("You're checked in!" in driver.page_source):
        driver.get_screenshot_as_file(date+'.png')
        print "You're checked in!"
except:
    print "There was an error checking in. Please check in manually..."