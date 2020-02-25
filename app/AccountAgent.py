from time import sleep
import datetime
import DBUsers, Constants
import traceback
import random

def login(webdriver):
    #Open the instagram login page
    webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
    #sleep for 3 seconds to prevent issues with the server
    sleep(3)
    #Find username and password fields and set their input using our constants
    username = webdriver.find_element_by_name('username')
    username.send_keys(Constants.INST_USER)
    password = webdriver.find_element_by_name('password')
    password.send_keys(Constants.INST_PASS)
    # #Get the login button
    # try:
    #     button_login = webdriver.find_element_by_xpath(
    #         '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')
    #         #'//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button'
            
    # except:
    #     button_login = webdriver.find_element_by_xpath(
    #          '//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]')
            
    #sleep again
    sleep(2)
    #click login
    password.submit()
    sleep(3)
    #In case you get a popup after logging in, press not now.
    #If not, then just return
    try:
        notnow = webdriver.find_element_by_css_selector(
            'body > div.RnEpo.Yx5HN > div > div > div.mt3GC > button.aOOlW.HoLwm')
        notnow.click()
    except:
        return