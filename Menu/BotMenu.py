from Main_Bot_Menu import Bot_Factory, Browser_Config
from SettingFiles import Factory_Settings, MainBotSettings, MenuSettings


class BotMenu:

    @staticmethod
    def menu():
        running = True
        while running:
            # ask the user for the browser type and platform in order to create an instance of the bot
            bot = BotMenu.user_bot_setup()
            print("Bot Created")
            BotMenu.action_menu(bot)

    @staticmethod
    def user_bot_setup():
        browser = BotMenu.pick_browser()
        platform = BotMenu.pick_platform()
        bot = Bot_Factory.Bot_Maker.create_bot(platform, browser)
        return bot

    @staticmethod
    def action_menu(bot):
        # Loop continuously until the user chooses to quit
        while True:
            # Get the user's selected action
            action = bot.pick_action()

            # Check if the user chose to quit
            if action == MainBotSettings.quit_option:
                # If so, break out of the loop and end the function
                break

            # Execute the selected action
            bot.take_action(action)

    @staticmethod
    def display_browsers():
        for i, key in enumerate(Browser_Config.browsers):
            print(f"{i} - {key}")

    """""
    @staticmethod
    def display_browsers():
        count = 0
        for key in Browser_Config.browsers.keys():
            print(str(count) + " - " + key)
            count += 1
    """""

    @staticmethod
    def pick_browser():
        BotMenu.display_browsers()
        num_browsers = len(Browser_Config.browsers)
        browser_index = BotMenu.get_valid_index(MenuSettings.PICK_BROWSER_MESSAGE, num_browsers)
        return list(Browser_Config.browsers)[browser_index]

    @staticmethod
    def display_platforms():
        for i, platform in enumerate(Factory_Settings.bot_list):
            print(f"{i} - {platform}")

    @staticmethod
    def pick_platform():
        BotMenu.display_platforms()
        num_platforms = len(Factory_Settings.bot_list)
        platform_index = BotMenu.get_valid_index(MenuSettings.PICK_PLATFORM_MESSAGE, num_platforms)
        return Factory_Settings.bot_list[platform_index]

    @staticmethod
    def get_valid_index(prompt, num_items):
        while True:
            index = input(prompt)
            if index.isdigit() and 0 <= int(index) < num_items:
                return int(index)
            print(MenuSettings.INVALID_ANSWER.format(0, num_items - 1))



