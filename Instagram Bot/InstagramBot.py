from MainBot.MainBot import MainBot
import InstagramBotSettings
import selenium
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from MainBot import MainBotSettings

class InstagramBot(MainBot):

    def __init__(self, browser):  # user needs to input the web driver
        super().__init__(browser, InstagramBotSettings.URL)
        self.setup_login()
        self.action_list = {
            ("Follow user list", self.follow_user_list),
            ("Message user list", self.message_user_list),
            ("Follow user list", self.follow_user_list)
        }

    def show_actions(self):
        for action in self.action_list.items():
            print("{} - {}".format(action[0], action[1][0]))

    def pick_action(self):
        action = input("Enter value ({}-{}):".format(0, (len(self.action_list) - 1)))
        return action

    def get_valid_action(self):
        action = self.pick_action()
        while not self.is_valid_action(action):
            action = self.pick_action()
        return action

    def is_valid_action(self, action):
        if action == MainBotSettings.quit_option:
            return MainBotSettings.quit_option
        if not action.isnumeric():
            return False
        action = int(action)
        if action > len(self.action_list) - 1 or action < 0:
            return False
        return True

    def take_action(self, action):
        self.action_list[action][1]()

    # log in to the account
    def setup_login(self):
        # get credentials
        username, password = self.getCredentials()
        # create the buttons
        log_in_button = self.browser.find_element(By.XPATH,
                                                  InstagramBotSettings.log_in_button_xpath)  # maybe we put this in the settings?
        username_field = self.browser.find_element(By.NAME, InstagramBotSettings.username_path)
        password_field = self.browser.find_element(By.NAME, InstagramBotSettings.password_path)
        self.login(username, password, password_field, username_field, log_in_button)

    def login(self, username, password, password_field, username_field, login_button):
        self.write_action(username, username_field)
        self.write_action(password, password_field)
        self.click_action(login_button)
        self.handle_notifications_window()

    def handle_notifications_window(self):
        # If notifications are off, instagram will ask to turn them on
        turn_on_notifications_pop_up = self.browser.find_element(By.XPATH,
                                                                 InstagramBotSettings.turn_on_notifications_pop_up_xpath)
        try:
            self.click_action(turn_on_notifications_pop_up)
        except selenium.common.exceptions.NoSuchWindowException:
            pass

    def getCredentials(self):
        username = (input("Enter username: "))  # TODO settings
        password = (input("Enter password: "))
        while len(password) < InstagramBotSettings.minimum_password_length:
            print("Password too short, must be " + InstagramBotSettings.minimum_password_length)
            password = (input("Enter password: "))
        return username, password

    # navigate to the home page
    def home(self):
        home_button = self.browser.find_element(By.XPATH, InstagramBotSettings.home_button_xpath)
        MainBot.click_action(home_button)

    # follow a certain user
    def follow(self, username):
        # go to the user we want to follow
        self.userlookup(username)
        # create the button
        follow_button = self.browser.find_element(By.XPATH, InstagramBotSettings.follow_button_xpath)
        # action
        MainBot.click_action(follow_button)

    # go to a user's profile
    def user_look_up(self, username):
        # navigating to starting point (home page)
        self.home()
        # button making
        search_button = self.browser.find_element(By.XPATH, InstagramBotSettings.search_button_xpath)
        search_text_box = self.browser.find_element(By.XPATH, InstagramBotSettings.search_button_xpath)
        # actions
        MainBot.click_action(search_button)
        MainBot.write_action(username, search_text_box)
        # 2x enter for sending the search request
        MainBot.write_action(Keys.ENTER, MainBot._short_action_time())
        MainBot.write_action(Keys.ENTER, MainBot._short_action_time())

    # message a certain user
    def message_user(self, username, text):
        # go to the user we want to message
        self.userlookup(username)
        # create the buttons
        message_button = self.browser.find_element(By.XPATH, InstagramBotSettings.message_button_xpath)
        message_textbox = self.browser.find_element(By.XPATH, InstagramBotSettings.message_textbox_xpath)
        send_button = self.browser.find_element(By.XPATH, InstagramBotSettings.send_button_xpath)
        # actions
        self.click_action(message_button, InstagramBotSettings.message_wait_time)
        self.write_action(text, message_textbox)
        self.click_action(send_button)

    # mass message a user list a certain message
    def message_user_list(self, user_list, text):
        for username in user_list:
            self.message_user(username, text)

    # mass follow a user list
    def follow_user_list(self, user_list):
        for username in user_list:
            self.follow(username)
