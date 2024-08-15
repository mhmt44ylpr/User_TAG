import colorama
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
class Twitter(object):
    def __init__(self):
        self.user = input(" Enter your Tumblr username: ")
        self.user = self.user.replace(" " , "")
        self.url = f'https://x.com/{self.user}'
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
                name = self.driver.find_element(By.XPATH , '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/span/span[1]')
                print(colorama.Fore.RED + " Name: " + colorama.Fore.BLUE + name.text)
                try:
                    bio = self.driver.find_element(By.XPATH , '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[3]/div/div/span')
                    print(colorama.Fore.RED + " Bio: " + colorama.Fore.BLUE + bio.text)
                except:
                    print(colorama.Fore.RED + " Bio: None")
                print(colorama.Fore.RED + " Details;")
                try:
                    details = self.driver.find_elements(By.XPATH , '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div/span')
                    for detail in details:
                        print( colorama.Fore.BLUE + " " + detail.text)
                except:
                    print(colorama.Fore.RED + " Details: None")
                    self.driver.quit()
            else:
                print(colorama.Fore.RED + " There is no such user!!!")
                self.driver.quit()
        except:
                print(colorama.Fore.RED+" There is an unknown error!!! Please contact us.")
        self.driver.quit()
class Twitter_Writer(object):
    def __init__(self,user):
        self.user = user
        self.user = self.user.replace(" " , "")
        self.url = f'https://x.com/{self.user}'
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
            f.write(f"{15*'*'} Twitter {15*'*'}\n")
            try:
                if response.status_code == 200:
                    name = self.driver.find_element(By.XPATH , '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div/div[1]/div/div[1]/div/div/span/span[1]')
                    f.write(f" Name:{name.text} \n")
                    try:
                        bio = self.driver.find_element(By.XPATH , '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[3]/div/div/span')
                        f.write(f" Bio:{bio.text} \n")
                    except:
                        f.write(" Bio: None\n")
                    f.write(" Details;\n")
                    try:
                        details = self.driver.find_elements(By.XPATH , '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[4]/div/span')
                        for detail in details:
                            f.write( " " + detail.text + "\n")
                    except:
                        f.write(" Details: None\n")
                        self.driver.quit()
                else:
                    f.write(colorama.Fore.RED + " None\n")
                    self.driver.quit()
            except:
                    f.write("None\n")
            self.driver.quit()
