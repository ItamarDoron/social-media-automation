from random import random
from time import sleep
import selenium

import MainBotSettings
from selenium.webdriver.common.by import By

class MainBot():

    def __init__(self, browser, URL):
        self.URL = URL
        self.browser = browser

    def start(self):
        self.browser.get(self.URL)


    # random sleep generated time (in seconds) for long actions that need loading
    @staticmethod
    def _long_action_time():
        return random.randint(MainBotSettings.start_long_random_time, MainBotSettings.end_long_random_time)

    # random sleep generated time (in seconds) for short actions that do not need loading
    @staticmethod
    def _short_action_time():
        return random.randint(MainBotSettings.start_short_random_time, MainBotSettings.end_short_random_time)


    def click_action(self, button, sleep_time=_short_action_time()):  # TO DO: add generic default time
        x = MainBot.short_action_time()     ##  why do I need MainBot here and not in the header
        button.click()
        sleep(sleep_time)

    def write_action(self, text, input_box, sleep_time=_long_action_time()):  # TO DO: add generic default time
        self.click_action(input_box, MainBot.short_action_time())
        input_box.send_keys()
        sleep(sleep_time)


#############################
# notes
# security considerations -  hashing was an option for saving the password but decided to use an
# encryption like ROT13 for saving the password string in the variable and decryption when sending to the login page
