import InstagramBot.InstagramBot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

import MainBot.MainBot
from Main_Bot_Menu import Browser_Config


class Bot_Maker:

    @staticmethod
    def create_browser(browser_type):
        if browser_type.lower() == "chrome":
            driver = webdriver.Chrome(service=Service(Browser_Config.browsers[browser_type]))
            return driver

        # possible extension to more browsers
        print("Incorrect browser type")

    @staticmethod
    def create_bot(bot_type, browser_type):
        driver = Bot_Maker.create_browser(browser_type)
        return InstagramBot.InstagramBot.InstagramBot(driver)
