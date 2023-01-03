import MenuSettings
import Bot_Factory
import Factory_Settings
import InstagramBot
from MainBot import MainBotSettings


class BotMenu:

    @staticmethod
    def menu():
        running = True
        while running:
            # ask the user for the browser type and platform in order to create an instance of the bot
            bot = BotMenu.user_bot_setup()
            BotMenu.action_menu(bot)

    @staticmethod
    def get_valid_answer(message, end, start=0):
        number = input(message)
        while not number.isnumeric() and (int(number) >= end or int(number) < start):
            print("Invalid answer, please enter a number in the range " + start + " - " + end)
            number = input(message)
        return int(number)

    @staticmethod
    def display_browsers():
        count = 0
        for key in MenuSettings.browsers.keys():
            print(count + " - " + key)
            count += 1

    @staticmethod
    def pick_browser():
        if len(MenuSettings.browsers) == 0:
            print("You must enter at least one browser in the config file in order to use")
            return None
        BotMenu.display_browsers()
        result = BotMenu.get_valid_answer((len(MenuSettings.browsers)))
        return MenuSettings.browsers.keys()[result]

    @staticmethod
    def display_platforms():
        count = 0
        for platform in Factory_Settings.bot_list:
            print(count + " - " + platform)
            count += 1

    @staticmethod
    def pick_platform():
        answer = BotMenu.get_valid_answer(len(Factory_Settings.bot_list))
        return Factory_Settings.bot_list[answer]

    @staticmethod
    def browser_menu_input():
        print("Welcome! Please pick your browser from your setup configurations file")
        BotMenu.display_browsers()
        choice = BotMenu.pick_browser()
        browser = Bot_Factory.create_browser(choice)
        return browser

    @staticmethod
    def platfrom_menu_input():
        print("Please pick the platform")
        BotMenu.display_platforms()
        platform = BotMenu.pick_platform()
        return platform

    @staticmethod
    def user_bot_setup():
        browser = BotMenu.browser_menu_input()
        platform = BotMenu.platfrom_menu_input()
        return Bot_Factory.Bot_Maker(platform, browser)

    @staticmethod
    def action_menu(bot):
        while True:
            # display actions
            bot.show_actions()
            action = bot.get_valid_action()
            if action == MainBotSettings.quit_option:
                break
            bot.take_action(action)
