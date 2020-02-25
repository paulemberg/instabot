import time
import json

from selenium import webdriver


with open('../config/configuration.json') as config_file:
    data = json.load(config_file)

driver = webdriver.Chrome('/home/paulemberg/projects/chromedriver_linux64/chromedriver')  # Optional argument, if not specified will search path.
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('username')
search_box.send_keys(data["Username"])
search_box = driver.find_element_by_name('password')
search_box.send_keys(data["Password"])

search_box.submit()
time.sleep(5) # Let the user actually see something!
#driver.quit()