from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramBot():
    #Bot and browser initial
    def __init__(self, email, password):
        self.browser = webdriver.Chrome('/Users/home/PycharmProjects/InstaBot/chromedriver')
        self.email = email
        self.password = password
    # Sign in Page, fills in details
    def signIn(self):
        self.browser.get('http://www.instagram.com/accounts/login')

        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]
        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)
    # there's a "Turn on Notification" popup, the method turns it off
    def turnOff(self):
        button = self.browser.find_element_by_xpath('//button[text() = "Not Now"]')
        button.click()

    # follows user
    def followWUserName(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(3)
        followButton = self.browser.find_element_by_css_selector('button')
        if ( followButton.text != 'Following'):
            followButton.click()
            time.sleep(3)
        else:
            print("Already Following This User")

    # unfollows user
    def unFollowWUsername(self, username):
        self.browser.get('https://www.instagram.com/' + username + '/')
        time.sleep(3)
        followButton = self.browser.find_element_by_css_selector('button')
        if (followButton.text == 'Following'):
            followButton.click()
            time.sleep(3)
            confirmButton = self.browser.find_element_by_xpath('//button[text() = "Unfollow"]')
            confirmButton.click()
        else:
            print("You are not following the user")


useremail = ''
userpassword = ''
bot = InstagramBot(useremail, userpassword)

bot.signIn()
bot.turnOff()
#bot.followWUserName('landrover')

