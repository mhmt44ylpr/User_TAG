from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
import colorama
import os
class Facebook():
    def __init__(self):
        self.ad_list = set()
        self.urs = input(" Facebook User Name : ")
        self.urs = self.urs.replace(" " , "")
        self.url = f'https://facebook.com/public/{self.urs}'
        if os.name == "nt":
            self.options = webdriver.ChromeOptions()
            self.options.add_argument('--headless')
            self.options.add_argument("disable-popup-blocking")
            self.driver = webdriver.Chrome(options=self.options)
            self.driver.get(self.url)
            self.Links()
            self.driver.quit()
        elif os.name == "posix":
            self.options = webdriver.FirefoxOptions()
            self.options.add_argument('--headless')
            self.options.add_argument("disable-popup-blocking")
            self.driver = webdriver.Firefox(options=self.options)
            self.driver.get(self.url)
            self.Links()
            self.driver.quit()

    def Links(self):
        num = 0
        response = requests.get(self.url)
        print("\n"*2)
        if response.status_code == 200:
            try:
                while True:
                    time.sleep(2)
                    users = self.driver.find_elements(By.XPATH ,'//*[@id="BrowseResultsContainer"]/div/div/div/div/div[2]/div/div[1]/div[1]/div/div/div/div/a')
                    for user in users:
                        num += 1
                        print(colorama.Fore.WHITE + f" {num})" + colorama.Fore.RED + user.text + colorama.Fore.BLUE + user.get_attribute("href"))
                        self.ad_list.add(user.get_attribute('href'))
                    if num >= 7:
                        break
                    self.driver.quit()
            except:
                print(colorama.Fore.RED+"  There is no such users!!!")
                self.driver.quit()
        else:
            print(colorama.Fore.RED+" There is no such users!!!")
            self.driver.quit()
class Facebook_writer():
    def __init__(self,user):
        self.ad_list = set()
        self.user = user
        self.url = f'https://facebook.com/public/{self.user}'
        if os.name == "nt":
            self.options = webdriver.ChromeOptions()
            self.options.add_argument('--headless')
            self.options.add_argument("disable-popup-blocking")
            self.driver = webdriver.Chrome(options=self.options)
            self.driver.get(self.url)
            self.Links()
            self.driver.quit()
        elif os.name == "posix":
            self.options = webdriver.FirefoxOptions()
            self.options.add_argument('--headless')
            self.options.add_argument("disable-popup-blocking")
            self.driver = webdriver.Firefox(options=self.options)
            self.driver.get(self.url)
            self.Links()
            self.driver.quit()
    def Links(self):
        num = 0
        response = requests.get(self.url)
        with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
            f.write(f"{15*'*'} Facebook {15*'*'}\n")
        if response.status_code == 200:
            try:
                while True:
                    time.sleep(2)
                    users = self.driver.find_elements(By.XPATH ,'//*[@id="BrowseResultsContainer"]/div/div/div/div/div[2]/div/div[1]/div[1]/div/div/div/div/a')
                    with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                        for user in users:
                            num += 1
                            f.write(f" {num}){user.text}: {user.get_attribute("href")}\n")
                            self.ad_list.add(user.get_attribute('href'))
                    if num >= 7:
                        break
                    self.driver.quit()
            except:
                print("None\n")
                self.driver.quit()
        else:
            print("None\n")
            self.driver.quit()


