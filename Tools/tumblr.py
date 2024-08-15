import colorama
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import os
class Tumblr(object):
    def __init__(self):
        self.user = input(" Enter your Tumblr username: ")
        self.user = self.user.replace(" " , "")
        self.url = f'https://www.tumblr.com/{self.user}'
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
                soup = BeautifulSoup(response.text, 'html.parser')
                name = soup.find('h1', class_='vfPi2')
                print( colorama.Fore.RED +" Name"+":"+ colorama.Fore.BLUE +name.text)
                bio = soup.find('div', class_='a15fm')
                bio = bio.text
                num = 0
                nu = 1
                print(colorama.Fore.RED + " Bio;")
                new_str = " "
                while True:
                    new_str = colorama.Fore.BLUE + new_str + bio[num]
                    num = num + 1
                    nu = nu + 1
                    if nu == 55:
                        new_str = new_str + "\n "
                        nu = 0
                    if num == len(bio):
                        break
                print(new_str)
                self.driver.quit()
            else:
                print(colorama.Fore.RED + " There is no such user!!!")
                self.driver.quit()
        except:
                print(colorama.Fore.RED+" There is no such user!!!")
        self.driver.quit()
class Tumblr_Write(object):
    def __init__(self,user):
        self.user = user
        self.url = f'https://www.tumblr.com/{user}'
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
            f.write(f"{15*'*'} Tumblr {15*'*'}\n")
        try:
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                name = soup.find('h1', class_='vfPi2')
                with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                    f.write(f" Name:{name.text}\n")
                bio = soup.find('div', class_='a15fm')
                bio = bio.text
                num = 0
                nu = 1
                new_str = " "
                while True:
                    new_str = colorama.Fore.WHITE + new_str + bio[num]
                    num = num + 1
                    nu = nu + 1
                    if nu == 55:
                        new_str = new_str + "\n "
                        nu = 0
                    if num == len(bio):
                        break
                with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                    f.write(f" Bio:{new_str}\n")
                    self.driver.quit()

            else:
                with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                    f.write("none\n")
                    self.driver.quit()
        except:
            with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                f.write("none\n")
        self.driver.quit()




