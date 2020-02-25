import AccountAgent
import DBUsers
import Constants
import datetime


def init(webdriver):
    Constants.init()
    AccountAgent.login(webdriver)
    return


def update(webdriver):
    return