import colorama
from selenium import webdriver
import requests
import  os
class Instagran(object):
    def __init__(self):
        self.user = input(" Enter Instagram username: ")
        self.user = self.user.replace(" " , "")
        self.url = f'https://www.instagram.com/{self.user}/'
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
        if response.status_code == 200:
            print( "\n"+ colorama.Fore.RED  +  " Instagram url : " + colorama.Fore.BLUE  +  self.url)
            self.driver.quit()
        else:
            print("\n" + colorama.Fore.RED + " Instagram url : None")
            self.driver.quit()
class Instagran_Writer(object):
    def __init__(self,user):
        self.user = user
        self.user = self.user.replace(" " , "")
        self.url = f'https://www.instagram.com/{self.user}/'
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
            f.write(f"{15*'*'} Instagram {15*'*'}\n")
            if response.status_code == 200:
                f.write(f" Instagram url : {self.url}\n")
                self.driver.quit()
            else:
                f.write( " Instagram url : None\n")
                self.driver.quit()




