import colorama
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
class About_me(object):
    def __init__(self):
        self.user = input(" Enter your About.me username: ")
        self.user = self.user.replace(" " , "")
        self.url = f'https://about.me/{self.user}'
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
            self.information_list = list()
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
            self.information_list = list()

    def Get(self):
        self.driver.get(self.url)
        response = requests.get(self.url)
        try:
            if response.status_code == 200:
                name = self.driver.find_element(By.XPATH , '/html/body/div[1]/div/div/main/div/div/div/div[1]/div[2]/section[1]/h1')
                print(colorama.Fore.RED + " Name: " + colorama.Fore.BLUE + name.text)
                try:
                    about = self.driver.find_element(By.XPATH , '/html/body/div[1]/div/div/main/div/div/div/div[1]/div[2]/section[2]/h2')
                    print(colorama.Fore.RED + " About: " + colorama.Fore.BLUE + about.text)
                except:
                    pass
                try:
                    detail = self.driver.find_element(By.XPATH , '/html/body/div[1]/div/div/main/div/div/div/div[2]/div/section[2]/div')
                    print(colorama.Fore.RED + " Details:" + colorama.Fore.BLUE + detail.text)
                except:
                    pass

                links = self.driver.find_elements(By.XPATH , '/html/body/div[1]/div/div/main/div/div/div/div[2]/div/section[3]/ul/li/a')
                for link in links:
                    if "www" in link.get_attribute("href"):
                        print(" " + colorama.Fore.RED + link.get_attribute("href").split(".")[1].capitalize() + ": " + colorama.Fore.BLUE + link.get_attribute("href"))
                    else:
                        print(" " + colorama.Fore.RED + link.get_attribute("href").split(".")[0].capitalize() + ": " + colorama.Fore.BLUE + link.get_attribute("href"))
                self.driver.quit()
            else:
                print(colorama.Fore.RED+" There is no such user!!!")
                self.driver.quit()
        except:
            print(colorama.Fore.RED + " There is an unknown error!!! Please contact us.")
            self.driver.quit()
        self.driver.quit()
class About_me_writer(object):
    def __init__(self,user):
        self.user = user
        self.user = self.user.replace(" ", "")
        self.url = f'https://about.me/{self.user}'
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
            self.information_list = list()
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
            self.information_list = list()

    def Get(self):
        with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
            f.write(f"{15*'*'} About.me {15*'*'}\n")
            self.driver.get(self.url)
            response = requests.get(self.url)
            if response.status_code == 200:
                name = self.driver.find_element(By.XPATH , '/html/body/div[1]/div/div/main/div/div/div/div[1]/div[2]/section[1]/h1')
                f.write(f" Name: {name.text}\n")
                about = self.driver.find_element(By.XPATH , '/html/body/div[1]/div/div/main/div/div/div/div[1]/div[2]/section[2]/h2')
                f.write(f" About: {about.text}\n")
                try:
                    detail = self.driver.find_element(By.XPATH , '/html/body/div[1]/div/div/main/div/div/div/div[2]/div/section[2]/div')
                    f.write(f" Details:{detail.text}\n")
                except:
                    f.write("No Details")
                links = self.driver.find_elements(By.XPATH , '/html/body/div[1]/div/div/main/div/div/div/div[2]/div/section[3]/ul/li/a')
                for link in links:
                    if "www" in link.get_attribute("href"):
                        f.write(f' {link.get_attribute("href").split(".")[1].capitalize()}: {link.get_attribute("href")}\n')
                    else:
                        f.write(f' {link.get_attribute("href").split(".")[0].capitalize()}: {link.get_attribute("href")}\n')
            else:
                with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                    f.write(" None\n")
            self.driver.quit()

