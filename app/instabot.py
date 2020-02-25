from selenium import webdriver
import bot_engine

chromedriver_path = '/home/paulemberg/projects/chromedriver_linux64/chromedriver' 
webdriver = webdriver.Chrome(executable_path=chromedriver_path)

bot_engine.init(webdriver)
bot_engine.update(webdriver)

webdriver.close()