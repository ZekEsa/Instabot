from time import sleep
from selenium import webdriver
from secrets import password
from random import randint

class Bot():

    links = []

    #Chooses one of these comments randomly
    comments = [
        'Great post!', 'cool lol', 'artificial intelligence is the future!', 'wowza'
    ]

    def __init__(self):
        #can change these
        hashtag = 'aiart'
        username = 'robotZek'

        # set the driver
        self.driver = webdriver.Firefox()

        self.login(username, password)
        #self.get_first_post('artificalintelligenceart')
        #self.like_pic()
        #self.get_post()
        self.like_comment_by_hashtag(hashtag)
        #self.download_image()

    
    def login(self, username, password):
        """
            1) open instagram
            3) begin login sequence
        """
        # load up instagram
        self.driver.get('https://instagram.com')
        sleep(5)

        # type in username and password
        username_input = self.driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input')
        username_input.send_keys(username)
        sleep(1)

        password_input = self.driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input')
        password_input.send_keys(password)
        sleep(1)

        #click login!
        self.driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div').click()
        sleep(5)
        
        # get rid of popups ie. click 'Not now' buttons
        self.driver.find_element('xpath', "//button[contains(text(), 'Not Now')]").click()
        sleep(3)
        self.driver.find_element('xpath', "//button[contains(text(), 'Not Now')]").click()
        sleep(3)


    def like_comment_by_hashtag(self, hashtag):
        # search hashtag
        self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
        sleep(5)

        # get links/posts from this page
        links = self.driver.find_elements('tag name', 'a')

        def condition(link):
            return '.com/p/' in link.get_attribute('href')
        valid_links = list(filter(condition, links))
        # search hashtag
        self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
        sleep(5)

        # get links/posts from this page
        links = self.driver.find_elements('tag name', 'a')

        def condition(link):
            return '.com/p/' in link.get_attribute('href')
        valid_links = list(filter(condition, links))
        
        # Like and Comment!
        for i in range(5):
            link = valid_links[i].get_attribute('href')
            if link not in self.links:
                self.links.append(link)
        
        for link in self.links:
            self.driver.get(link)
            sleep(3)

            # like
            self.driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[1]/span[1]/button/div[2]').click()
            sleep(5)

            # comment
            self.driver.find_element('xpath', '/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea').click()
            sleep(1)
            #comment.send_keys(self.comments[randint(0, 3)])
            self.driver.find_element('xpath', "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea").send_keys(self.comments[randint(0, 3)])
            sleep(1)
            self.driver.find_element('xpath', "/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/div[2]/div").click() 

# make runable 
def main():
    while True:
        my_bot = Bot()
        sleep(60*60*24) # do this *once a day*


if __name__ == '__main__':
    main()
