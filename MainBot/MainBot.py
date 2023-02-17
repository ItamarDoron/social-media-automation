from random import randint
from time import sleep
from SettingFiles import MainBotSettings


class MainBot:

    def __init__(self, driver, URL):
        self.driver = driver
        self.URL = URL

    def start(self):
        self.driver.get(self.URL)

    # random sleep generated time (in seconds) for long actions that need loading
    @staticmethod
    def _long_action_time():
        return randint(MainBotSettings.start_long_random_time, MainBotSettings.end_long_random_time)

    # random sleep generated time (in seconds) for short actions that do not need loading
    @staticmethod
    def _short_action_time():
        return randint(MainBotSettings.start_short_random_time, MainBotSettings.end_short_random_time)

    def click_action(self, button, sleep_time=_short_action_time()):
        button.click()
        sleep(sleep_time)

    def write_action(self, text, input_box, sleep_time=_long_action_time()):
        self.click_action(input_box, MainBot._long_action_time())
        input_box.send_keys(text)
        sleep(sleep_time)

    @staticmethod
    def wait_long():
        sleep(MainBot._long_action_time())

    @staticmethod
    def wait_short():
        sleep(MainBot._short_action_time())
