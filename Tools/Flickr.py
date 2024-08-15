import time
import colorama
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import os
class Flickr(object):
    def __init__(self):
        self.user = input(" Enter your Flickr username: ")
        self.user = self.user.replace(" " , "")
        self.url = f'https://www.flickr.com/photos/{self.user}/'
        self.information_list = list()
        if os.name == "nt":
            self.options = webdriver.ChromeOptions()
            self.options.add_argument("--window-size=1920,1080")
            self.options.add_argument("--disable-extensions")
            self.options.add_argument("--proxy-server='direct://'")
            self.options.add_argument("--proxy-bypass-list=*")
            self.options.add_argument("--start-maximized")
            self.options.add_argument('--headless')
            self.options.add_argument('--disable-gpu')
            self.options.add_argument('--disable-dev-shm-usage')
            self.options.add_argument('--no-sandbox')
            self.options.add_argument('--ignore-certificate-errors')
            self.options.add_argument("--disable-popup-blocking")
            self.driver = webdriver.Chrome(options=self.options)
        elif os.name == "posix":
            self.options = webdriver.FirefoxOptions()
            self.options.add_argument("--window-size=1920,1080")
            self.options.add_argument("--disable-extensions")
            self.options.add_argument("--proxy-server='direct://'")
            self.options.add_argument("--proxy-bypass-list=*")
            self.options.add_argument("--start-maximized")
            self.options.add_argument('--headless')
            self.options.add_argument('--disable-gpu')
            self.options.add_argument('--disable-dev-shm-usage')
            self.options.add_argument('--no-sandbox')
            self.options.add_argument('--ignore-certificate-errors')
            self.options.add_argument("--disable-popup-blocking")
            self.driver = webdriver.Firefox(options=self.options)
    def Get(self):
        self.driver.get(self.url)
        response = requests.get(self.url)
        try:
            if response.status_code == 200:
                bs = BeautifulSoup(response.text, 'html.parser')
                name = bs.find('h1', attrs={"class" : "truncate"}).text
                print(colorama.Fore.RED + " Name: " + colorama.Fore.BLUE + name.strip())
                print(colorama.Fore.RED + " Details;" + colorama.Fore.BLUE)
                followers = bs.find('p', attrs={"class" : "followers"}).text
                fo = followers.split("•")
                for i in fo:
                    print(" " + i)
                photo = bs.find("p" , attrs={"class" : "metadata-item photo-count"})
                print(" " + photo.text.strip())
                self.driver.quit()
            else:
                print(colorama.Fore.RED + " There is no such user!!!")
                self.driver.quit()
        except:
                print(colorama.Fore.RED+" There is an unknown error!!! Please contact us.")
        self.driver.quit()
class Flickr_Write(object):
    def __init__(self,user):
        self.user = user
        self.user = self.user.replace(" " , "")
        self.url = f'https://www.flickr.com/photos/{self.user}/'
        self.information_list = list()
        if os.name == "nt":
            self.options = webdriver.ChromeOptions()
            self.options.add_argument("--window-size=1920,1080")
            self.options.add_argument("--disable-extensions")
            self.options.add_argument("--proxy-server='direct://'")
            self.options.add_argument("--proxy-bypass-list=*")
            self.options.add_argument("--start-maximized")
            self.options.add_argument('--headless')
            self.options.add_argument('--disable-gpu')
            self.options.add_argument('--disable-dev-shm-usage')
            self.options.add_argument('--no-sandbox')
            self.options.add_argument('--ignore-certificate-errors')
            self.options.add_argument("--disable-popup-blocking")
            self.driver = webdriver.Chrome(options=self.options)
        elif os.name == "posix":
            self.options = webdriver.FirefoxOptions()
            self.options.add_argument("--window-size=1920,1080")
            self.options.add_argument("--disable-extensions")
            self.options.add_argument("--proxy-server='direct://'")
            self.options.add_argument("--proxy-bypass-list=*")
            self.options.add_argument("--start-maximized")
            self.options.add_argument('--headless')
            self.options.add_argument('--disable-gpu')
            self.options.add_argument('--disable-dev-shm-usage')
            self.options.add_argument('--no-sandbox')
            self.options.add_argument('--ignore-certificate-errors')
            self.options.add_argument("--disable-popup-blocking")
            self.driver = webdriver.Firefox(options=self.options)
    def Get(self):
        self.driver.get(self.url)
        response = requests.get(self.url)
        with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
            f.write(f"{15 * '*'} Flickr {15 * '*'}\n")
            try:
                if response.status_code == 200:
                    bs = BeautifulSoup(response.text, 'html.parser')
                    name = bs.find('h1', attrs={"class" : "truncate"}).text
                    f.write(f" Name:{name.strip()} \n")
                    f.write(" Details;\n")
                    followers = bs.find('p', attrs={"class" : "followers"}).text
                    fo = followers.split("•")
                    for i in fo:
                        f.write(" " + i+ "\n")
                    photo = bs.find("p" , attrs={"class" : "metadata-item photo-count"})
                    f.write(" " + photo.text.strip()+"\n")
                    self.driver.quit()
                else:
                    f.write(" None \n")
                    self.driver.quit()
            except:
                f.write(" None \n")
            self.driver.quit()



