import colorama
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import os
class VK(object):
    def __init__(self):
        self.user = input(" Enter VK username: ")
        self.user = self.user.replace(" " , "")
        self.url = f'https://vk.com/{self.user}'
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
                name = self.driver.find_element(By.XPATH , '//*[@id="owner_page_name"]')
                print(colorama.Fore.RED + " Name: " + colorama.Fore.BLUE + name.text)
                try:
                    city = self.driver.find_element(By.XPATH ,'//*[@id="profile_redesigned"]/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/span[1]/span/span[2]')
                    print(colorama.Fore.RED + " City: " + colorama.Fore.BLUE + city.text)
                except:
                    print(colorama.Fore.RED + " City None")
                try:
                    work = self.driver.find_element(By.XPATH , '//*[@id="profile_redesigned"]/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/span[3]/span/span[2]')
                    print(colorama.Fore.RED + " Work: " + colorama.Fore.BLUE + work.text)
                    self.driver.quit()
                except:
                    print(colorama.Fore.RED + " Work None")
                    self.driver.quit()
            else:
                print(colorama.Fore.RED + " There is no such user!!!")
                self.driver.quit()
        except:
                print(colorama.Fore.RED+" There is an unknown error!!! Please contact us.")
        self.driver.quit()
class VK_writer(object):
    def __init__(self,user):
        self.user = user
        self.user = self.user.replace(" " , "")
        self.url = f'https://vk.com/{self.user}'
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
            f.write(f"{15*'*'} VK {15*'*'}\n")
            try:
                if response.status_code == 200:
                    name = self.driver.find_element(By.XPATH , '//*[@id="owner_page_name"]')
                    f.write(f" Name: {name.text}\n")
                    try:
                        city = self.driver.find_element(By.XPATH ,'//*[@id="profile_redesigned"]/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/span[1]/span/span[2]')
                        f.write(f" City: {city.text} \n"  )
                    except:
                        f.write(" City None")
                    try:
                        work = self.driver.find_element(By.XPATH , '//*[@id="profile_redesigned"]/div/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/span[3]/span/span[2]')
                        f.write(f" Work: {work.text}\n")
                    except:
                        f.write(" Work None\n")
                        self.driver.quit()
                else:
                    f.write(" None\n")
                    self.driver.quit()
            except:
                    f.write(" None\n")
            self.driver.quit()
