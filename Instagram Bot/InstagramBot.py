import MainBot.MainBot
from SettingFiles import InstagramBotSettings, MainBotSettings
import selenium
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class InstagramBot(MainBot.MainBot.MainBot):

    # TODO: Add hadle to both notifications and to login pop ups

    def __init__(self, driver):
        super().__init__(driver, InstagramBotSettings.URL)
        self.setup_login()
        # Dictionary of actions a user can execute
        self.action_list = {
            "Follow user list": self.follow_user_list,
            "Message user list": self.message_user_list
        }

    def start(self):
        super(InstagramBot, self).start()

        # log in to the account

    def setup_login(self):
        # get credentials
        username, password = self.getCredentials()
        self.start()
        self.wait_long()
        # create the buttons
        log_in_button = self.driver.find_element(By.XPATH, InstagramBotSettings.log_in_button_xpath)
        username_field = self.driver.find_element(By.NAME, InstagramBotSettings.username_path)
        password_field = self.driver.find_element(By.NAME, InstagramBotSettings.password_path)
        # preform the login
        self.login(username, password, password_field, username_field, log_in_button)

    def login(self, username, password, password_field, username_field, login_button):
        self.write_action(username, username_field)
        self.write_action(password, password_field)
        self.click_action(login_button)
        self.wait_long()
        self.handle_notifications_window()
        self.handle_notifications_window()

    def pick_action(self):
        self.show_actions()
        last_sequence = len(self.action_list) - 1
        try:
            input_str = input("Enter value ({}-{}): ".format(0, last_sequence))
            if input_str.lower() == 'q':
                return MainBotSettings.quit_option
            action = int(input_str)
            if action not in range(len(self.action_list)):
                raise ValueError("Action value out of range.")
            return list(self.action_list.keys())[action]
        except (ValueError, IndexError):
            print("Invalid input. Please try again.")
            return self.pick_action()

    def show_actions(self):
        for i, (key, value) in enumerate(self.action_list.items()):
            print("{} - {}".format(i, key))
        print("Enter " + MainBotSettings.quit_option + " to quit")

    def take_action(self, key):
        self.action_list[key]()

    def handle_notifications_window(self):
        # If notifications are off, instagram will ask to turn them on
        try:
            turn_on_notifications_pop_up = self.driver.find_element(By.XPATH, InstagramBotSettings.turn_on_notifications_pop_up_xpath)
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
        home_button = self.driver.find_element(By.XPATH, InstagramBotSettings.home_button_xpath)
        self.click_action(home_button)

    # follow a certain user
    def follow(self, username):
        # go to the user we want to follow
        self.user_look_up(username)
        # create the button
        follow_button = self.driver.find_element(By.XPATH, InstagramBotSettings.follow_button_xpath)
        # action
        self.click_action(follow_button)

    # go to a user's profile
    def user_look_up(self, username):
        # navigating to starting point (home page)
        self.home()
        # button making
        search_button = self.driver.find_element(By.XPATH, InstagramBotSettings.search_button_xpath)
        # actions
        self.click_action(search_button)
        search_text_box = self.driver.find_element(By.XPATH, InstagramBotSettings.search_text_box_xpath)
        self.write_action(username, search_text_box)
        # 2x enter for sending the search request
        self.write_action(Keys.ENTER, search_text_box, self._short_action_time())
        self.write_action(Keys.ENTER, search_text_box,  self._short_action_time())

    # message a certain user
    def message_user(self, username, text):
        # go to the user we want to message
        self.user_look_up(username)
        # go to message inbox
        message_button = self.driver.find_element(By.XPATH, InstagramBotSettings.message_button_xpath)
        self.click_action(message_button, InstagramBotSettings.message_wait_time)
        # enter message
        message_textbox = self.driver.find_element(By.XPATH, InstagramBotSettings.message_textbox_xpath)
        self.write_action(text, message_textbox)
        # send message
        send_button = self.driver.find_element(By.XPATH, InstagramBotSettings.send_button_xpath)
        self.click_action(send_button)

    # mass message a user list a certain message
    def message_user_list(self):
        message_list = InstagramBot.get_user_list()
        text = input(InstagramBotSettings.MESSAGE_INPUT)
        for username in message_list:
            self.message_user(username, text)

    # mass follow a user list
    def follow_user_list(self):
        follow_list = InstagramBot.get_user_list()
        for username in follow_list:
            self.follow(username)

    @staticmethod
    def get_user_list():
        user_list = []
        user_input = input(InstagramBotSettings.USER_LIST_INPUT_MESSAGE)
        if user_input:
            user_list = user_input.split(",")
            user_list = [username.strip() for username in user_list]
        return user_list
