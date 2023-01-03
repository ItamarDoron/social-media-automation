import InstagramBot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import MenuSettings
import BotMenu


class Bot_Maker:

    @staticmethod
    def create_browser(browser_type):
        type = browser_type.lower
        if type == "chrome":
            s = Service(MenuSettings.browsers[browser_type])
            browser = webdriver.Chrome(service=s)
            return browser
        # possible extension to more browsers
        print("Incorrect browser type")

    @staticmethod
    def create_bot(bot_type, browser):
        bot_type = bot_type.lower
        if bot_type == "instagram":
            return InstagramBot(browser)
        # possible extension to more platforms
        print("Incorrect platform")

