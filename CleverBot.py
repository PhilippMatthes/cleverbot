from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from os import system

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class CleverBot(object):
    def __init__(self):
        self.URL = "http://www.cleverbot.com/"
        self.alice = webdriver.PhantomJS()
        self.bob = webdriver.PhantomJS()
        self.message = " Hallo! Was machst du gerade?"
        self.alice.get(self.URL)
        self.bob.get(self.URL)

    def talk(self):
        while True:
            for i in range(20):
                sleep(len(self.message)/20)
                print(bcolors.BOLD + self.message + bcolors.ENDC)
                self.send_message(self.message, self.alice)
                if self.message:
                    system("say -v tom "+self.message)
                self.receive_message(self.alice)
                self.message = " "+self.message
                sleep(len(self.message)/20)
                print(bcolors.FAIL + self.message + bcolors.ENDC)
                self.send_message(self.message, self.bob)
                if self.message:
                    system("say -v ava "+self.message)
                self.receive_message(self.bob)
                self.message = " "+self.message
            self.alice.refresh()
            self.bob.refresh()

    def send_message(self, message, browser):
        textfield = browser.find_element_by_class_name("stimulus")
        textfield.send_keys(self.message)
        textfield.send_keys(Keys.RETURN)

    def receive_message(self, browser):
        message_size = 0
        previous_size = -1
        try:
            while message_size != previous_size:
                previous_size = message_size;
                sleep(1)
                chat = browser.find_elements_by_xpath("//span[contains(@class,'bot')]")
                if chat:
                    nosymbols = chat[len(chat)-1].text
                    self.message = nosymbols.replace("´","").replace("'","").replace('"',"").replace(";","").replace(")","").replace("(","")
                    message_size = len(self.message)
                else:
                    self.message = ""
        except:
            self.message = ""
