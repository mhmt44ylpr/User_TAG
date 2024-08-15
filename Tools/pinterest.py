import colorama
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
class Pinterest(object):
    def __init__(self):
        self.user = input(" Enter your Pinterest username: ")
        self.user = self.user.replace(" " , "")
        self.url = f'https://pinterest.com/{self.user}/'
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
                name = self.driver.find_element(By.XPATH ,'//*[@id="mweb-unauth-container"]/div/div[1]/div[1]/div/div[2]/div/h1/div')
                print(colorama.Fore.RED + " Name:" + colorama.Fore.BLUE + name.text)
                followers = self.driver.find_element(By.XPATH , '//*[@id="mweb-unauth-container"]/div/div[1]/div[1]/div/div[6]/div[1]/div/div/div')
                print(colorama.Fore.RED + " Followers:" + colorama.Fore.BLUE + followers.text)
                following = self.driver.find_element(By.XPATH , '//*[@id="mweb-unauth-container"]/div/div[1]/div[1]/div/div[6]/div[3]/div/div/div')
                print(colorama.Fore.RED + " Following:" + colorama.Fore.BLUE + following.text)
                try:
                    bio = self.driver.find_element(By.XPATH , '//*[@id="mweb-unauth-container"]/div/div[1]/div[1]/div/div[4]/div/div/div/span')
                    print(colorama.Fore.RED + " Bio:" + colorama.Fore.BLUE + bio.text)
                except:
                    pass
            else:
                print(colorama.Fore.RED + " There is no such user!!!")
                self.driver.quit()
        except:
            print(colorama.Fore.RED+" There is no such user!!")
        self.driver.quit()
class Pinterest_writer(object):
    def __init__(self,user):
        self.user = user
        self.user = self.user.replace(" " , "")
        self.url = f'https://pinterest.com/{self.user}/'
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
            f.write(f"{15*'*'} Pinterest {15*'*'}\n")
        try:
            if response.status_code == 200:
                with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                    name = self.driver.find_element(By.XPATH ,'//*[@id="mweb-unauth-container"]/div/div[1]/div[1]/div/div[2]/div/h1/div')
                    followers = self.driver.find_element(By.XPATH , '//*[@id="mweb-unauth-container"]/div/div[1]/div[1]/div/div[6]/div[1]/div/div/div')
                    following = self.driver.find_element(By.XPATH , '//*[@id="mweb-unauth-container"]/div/div[1]/div[1]/div/div[6]/div[3]/div/div/div')
                    f.write(f" Name:{name.text}\n Followers:{followers.text}\n Following:{following.text}")
                    try:
                        bio = self.driver.find_element(By.XPATH , '//*[@id="mweb-unauth-container"]/div/div[1]/div[1]/div/div[4]/div/div/div/span')
                        f.write(f" Bio:{bio.text}\n")
                    except:
                        pass
            else:
                with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                    f.write(" None\n")
                    self.driver.quit()
        except:
            with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                f.write(" None\n")
        self.driver.quit()

