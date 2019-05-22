from selenium import webdriver
import os
import time

class InstagramBot:

    
    def __init__(self,username,password):
        self.username=username
        self.password=password
        
        self.ig_url='https://www.instagram.com'
        
        self.bot_followed=[]

        self.driver=webdriver.Chrome('./chromedriver.exe')
        self.login()


    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')

        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        self.driver.find_elements_by_xpath("//div[contains(text(),'Log In')]")[0].click()


    def navigate(self,user):
        self.driver.get('{}/{}'.format(self.ig_url,user))


    def follow(self,user):
        self.navigate(user)
        follow_button=self.driver.find_elements_by_xpath("//button[contains(text(),'Follow')]")[0].click()
        self.bot_followed.append(user)

        
    def unfollow(self,user):
        self.navigate(user)
        followed=self.driver.find_elements_by_xpath("//button[contains(text(),'Following')]")[0]
        if followed:
            followed.click()
            unfollow_button=self.driver.find_elements_by_xpath("//button[contains(text(),'Unfollow')]")[0].click()
            self.bot_followed.remove(user)


if __name__ == '__main__':
    user=input("\nEnter username: ")
    passwd=input("\nEnter password: ")
    follow_user=input('\nEnter the other user: ')
    print()
    ig_bot=InstagramBot(user,passwd)
    time.sleep(2)
    #ig_bot.navigate('aumkar0803')
    ig_bot.follow(follow_user)
    time.sleep(10)
    ig_bot.unfollow(ig_bot.bot_followed[0])
