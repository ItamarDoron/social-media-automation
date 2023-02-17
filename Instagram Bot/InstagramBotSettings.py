# Paths for all buttons and input fields required for the "Instagram Bot"
URL = "https://www.instagram.com/accounts/login/"

# home
home_button_xpath = '//*[@aria-label="Home"]'

# user look up
search_button_xpath = '//*[@aria-label="Search"]'
search_text_box_xpath = '//input[@placeholder="Search"]'

# follow
follow_button_xpath = '//div[text()="Follow"]'

# messages
message_button_xpath = '//div[text()="Message"]'
message_textbox_xpath = '//textarea[@placeholder="Message..."]'
send_button_xpath = '//button[text()="Send"]'
message_wait_time = 5

# user log-in
username_path = 'username'
password_path = 'password'
log_in_button_xpath = '//div[text()="Log in"]'
turn_on_notifications_pop_up_xpath = '//button[text()="Not Now"]'

# user log-out
more_options_button_xpath = '//*[@aria-label="Settings"]'
log_out_button_xpath = '//div[text()="Log out"]'

# password length
minimum_password_length = 6;

# user list input message
USER_LIST_INPUT_MESSAGE = "Enter a comma-separated list of usernames: "

# message input from user
MESSAGE_INPUT = "What is the message?\n"
