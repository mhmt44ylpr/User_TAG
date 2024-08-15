import time
import colorama
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
class Medium_me(object):
    def __init__(self):
        self.user = input(" Enter Medium.me username: ")
        self.user = self.user.replace(" " , "")
        self.url = f'https://medium.com/@{self.user}'
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
                name = self.driver.find_element(By.XPATH , '//*[@id="root"]/div/div[3]/div[2]/div/main/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/span')
                print(colorama.Fore.RED + " Name: " + colorama.Fore.BLUE + name.text)
                try:
                    bio = self.driver.find_element(By.XPATH , '//*[@id="root"]/div/div[3]/div[2]/div/div/div/div/div/div[1]/div[1]/div[4]')
                    print(colorama.Fore.RED + " Bio: " + colorama.Fore.BLUE + bio.text)
                except:
                    print(colorama.Fore.RED + " Bio: None")
                followers = self.driver.find_element(By.XPATH , '//*[@id="root"]/div/div[3]/div[2]/div/div/div/div/div/div[1]/div[1]/div[3]/span/a')
                print(colorama.Fore.RED + " Followers: " + colorama.Fore.BLUE + followers.text[:-9])
                self.About()
                self.driver.quit()
            else:
                print(colorama.Fore.RED + " There is no such user!!!")
                self.driver.quit()
        except:
            print(colorama.Fore.RED+"  There is no such user!!!")
        self.driver.quit()
    def About(self):
        time.sleep(2)
        self.driver.get(self.url + "/about")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        print(colorama.Fore.RED + " About;" + colorama.Fore.BLUE)
        try:
            about = self.driver.find_element(By.XPATH , '//*[@id="root"]/div/div[3]/div[2]/div/main/div/div[2]')
            new_txt = ""
            n = 0
            b = 0
            while True:
                new_txt = new_txt + about.text[n]
                n = n + 1
                b = b + 1
                if b == 56:
                    new_txt = new_txt + "\n "
                    b = 0
                if len(about.text) == n + 1:
                    nl = list()
                    new_txt = new_txt.replace("Followers" , "")
                    new_txt = new_txt.replace("Followin" , "")
                    ne_l = new_txt.splitlines()
                    for i in ne_l:
                        nl.append(i)
                    for i in nl[:-4]:
                        print(i)
                        self.driver.quit()
                    break
        except:
            print(colorama.Fore.RED + " About: None")
            self.driver.quit()
class Medium_me_writer(object):
    def __init__(self,user):
        self.user = user
        self.user = self.user.replace(" " , "")
        self.url = f'https://medium.com/@{self.user}'
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
        elif os.name ==  "posix":
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
            f.write(f"{15*'*'} Medium.me {15*'*'}\n")
            try:
                if response.status_code == 200:
                    name = self.driver.find_element(By.XPATH , '//*[@id="root"]/div/div[3]/div[2]/div/main/div/div[1]/div/div/div/div/div[1]/div/div[2]/div[1]/span')
                    f.write(f" Name: {name.text}\n")
                    try:
                        bio = self.driver.find_element(By.XPATH , '//*[@id="root"]/div/div[3]/div[2]/div/div/div/div/div/div[1]/div[1]/div[4]')
                        f.write(f" Bio: {bio.text}\n")
                    except:
                        f.write(colorama.Fore.RED + " Bio: None")
                    followers = self.driver.find_element(By.XPATH , '//*[@id="root"]/div/div[3]/div[2]/div/div/div/div/div/div[1]/div[1]/div[3]/span/a')
                    f.write(f" Followers: {followers.text[:-9]}\n")

                else:
                    with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                        f.write("none\n")
                        self.driver.quit()
            except:
                with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                    f.write("none\n")
                    self.About()
            self.driver.quit()
    def About(self):
        time.sleep(2)
        self.driver.get(self.url + "/about")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
            f.write(" About;\n")
            try:
                about = self.driver.find_element(By.XPATH , '//*[@id="root"]/div/div[3]/div[2]/div/main/div/div[2]')
                new_txt = ""
                n = 0
                b = 0
                while True:
                    new_txt = new_txt + about.text[n]
                    n = n + 1
                    b = b + 1
                    if b == 56:
                        new_txt = new_txt + "\n "
                        b = 0
                    if len(about.text) == n + 1:
                        nl = list()
                        new_txt = new_txt.replace("Followers" , "")
                        new_txt = new_txt.replace("Followin" , "")
                        ne_l = new_txt.splitlines()
                        for i in ne_l:
                            nl.append(i)
                        for i in nl[:-4]:
                            f.write(i + "\n")
                            self.driver.quit()
                        break
            except:
                f.write(" About: None\n")
                self.driver.quit()




