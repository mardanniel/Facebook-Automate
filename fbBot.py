

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from hatdog import myUsers, myPasswords

class fbBot():
    
    def __init__(self): # STABLE

        """
        Initialize Facebook through Google Chrome.
        
        """
        fS = webdriver.ChromeOptions()
        
        fS.add_argument("--start-maximized")

        print("Start Google Chrome maximized...")

        fS.add_argument("--disable-infobars")

        print("Disabling Infobars...")

        fS.add_argument("--disable-notifications")

        print("Disabling Notifications...")

        print("Initializing Google Chrome...")

        self.driver = webdriver.Chrome(chrome_options=fS)

        self.action = ActionChains(self.driver)

        sleep(2)

        print("Opening Facebook...")

        self.driver.get('https://facebook.com')

        print("Waiting for page to load...")
        
        self.driver.implicitly_wait(10)

    def refreshTL(self): #STABLE

        """
        Refreshes the timeline.

        """

        sleep(8)

        self.driver.refresh()

    def fbLogin(self): # STABLE

        """
        Login user to his/her Facebook account.
        
        """
        try: 
            
            print("Entering Email/Username and Password...")

            fbEmail = self.driver.find_element_by_xpath('//*[@id="email"]')

            fbEmail.click()

            fbEmail.send_keys(myUsers[0])

            fbPass = self.driver.find_element_by_xpath('//*[@id="pass"]')

            fbPass.click()

            fbPass.send_keys(myPasswords[0])

            fbLogin = self.driver.find_element_by_xpath('//*[@id="loginbutton"]')

            fbLogin.click()

            print("Logging In to User Account...")

            self.driver.implicitly_wait(10)

        except:

            print("Provided Email / Username and Password Incorrect!")

    def fbPost(self, message):  # STABLE

        """
        Automatically post a message to the user timeline.
        
        """
        print("Posting to Main Timeline...")

        try:    # For First Post

            getWOYM = self.driver.find_element_by_name('xhpc_message')

            getWOYM.click()

            sleep(2)

            fbWOYM = self.driver.find_element_by_class_name('_1mf._1mj')

            fbWOYM.click()

            sleep(2)

            fbWOYM.send_keys(message)

            postWOYM = self.driver.find_element_by_class_name('_1mf7._4r1q._4jy0._4jy3._4jy1._51sy.selected._42ft')

            postWOYM.click()

        except:

            try: # After First Post / For Consecutive Posting

                fbWOYM = self.driver.find_element_by_class_name('_1mf._1mj')

                fbWOYM.click()

                sleep(2)

                fbWOYM.send_keys(message)

                postWOYM = self.driver.find_element_by_class_name('_1mf7._4r1q._4jy0._4jy3._4jy1._51sy.selected._42ft')

                postWOYM.click()

                sleep(2)

                # If duplicate post

                closeMod = self.driver.find_element_by_xpath('//*[@id="facebook"]/body/div[22]/div[2]/div/div/div/div/div[3]/div/div/div[2]/div/a') 

                closeMod.click()

                sleep(2)

            except: 

                pass

    def findPageDepth(self):
        """
        Scrolls down through timeline until it reaches the maximum height of the page.
        
        """
        SCROLL_PAUSE_TIME = 5

        max_height = self.driver.execute_script("return document.body.scrollHeight")

        scheight = .1

        while True:

            print("Scanning full timeline... | Current Depth:",max_height)

            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)

            scheight = scheight + .01

            sleep(SCROLL_PAUSE_TIME)

            new_height = self.driver.execute_script("return document.body.scrollHeight")

            if new_height == max_height:

                print("Max Depth:",max_height)

                break

            max_height = new_height

        sleep(10)

        self.driver.execute_script("window.scrollTo(0, 0);")

    def autoLike(self): # STABLE

        """
        Automatically likes all unliked post.
        
        """
        try:

            self.findPageDepth()

            while True:

                isUnliked = self.driver.find_element_by_xpath('//form[@class="commentable_item"]/div/div[2]/div/div/div/span[1]/div/div/a[@aria-pressed="false"]')

                print(isUnliked.location)

                isUnliked.click()

                sleep(5)

        except:

            print("No unliked buttons found!\nRefreshing...")

            self.refreshTL()

    def autoHaha(self):
        """
        Automatically reacts a post.
        
        """

        try:

            self.findPageDepth()

            while True:

                print("Finding Like button...")

                isUnhaha = self.driver.find_element_by_xpath('//*[@class="commentable_item"]/div/div[2]/div/div/div/span[1]/div/div/a[@aria-pressed="false"]')

                print("Location:",isUnhaha.location)

                print("Hovering to Like button...")
                                                            
                self.action.move_to_element(isUnhaha).perform()

                sleep(2)

                print("Dehovering to Like button...")

                randElem = self.driver.find_element_by_xpath('//*[@class="commentable_item"]/div/div[2]/div/div[2]/div/span[2]/a')

                self.action.move_to_element(randElem).perform()

                sleep(2)
                
                print("Finding Haha Reaction...")

                findHaha = self.driver.find_element_by_xpath("//*[@class='commentable_item']/div/div[2]/div/div/div/span[1]/div/div/div/div/div/div/div[1]/span[contains(@aria-pressed, 'false') and contains(@aria-label, 'Haha')]")

                self.action.move_to_element(isUnhaha).perform()

                print("Clicking Haha Reaction...")
                                                                                            
                findHaha.click()

                sleep(3)

        except Exception as ex:

            print(ex)

            print("No unreacted buttons found!\nRefreshing...")

            # self.refreshTL()

    def spamChat(self):

        try: 

            fbChat = self.driver.find_element_by_xpath('//*[@id="chatsearch"]/div/span/label/input')

            fbChat.click()

        except:
            pass

bot = fbBot()
bot.fbLogin()
bot.autoLike()

