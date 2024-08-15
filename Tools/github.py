import colorama
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
import time
import os
class Github():
    def __init__(self):
        """
        Communication was established via the website
        """
        self.user = input(" Enter your github username: ")
        self.user = self.user.replace(" " , "")
        self.url = f"https://github.com/{self.user}"
        if os.name == "nt":
            self.options = webdriver.ChromeOptions()
            self.options.add_argument('--headless')
            self.driver = webdriver.Chrome(options=self.options)
            self.driver.get(self.url)
        elif os.name == "posix":
            self.options = webdriver.FirefoxOptions()
            self.options.add_argument('--headless')
            self.driver = webdriver.Firefox(options=self.options)
            self.driver.get(self.url)
    def Get_Github(self):
        response = requests.get(self.url)
        """
        I allowed it to pull data based on the status code value.
        """
        if response.status_code == 200:
            print("\n" * 2)
            try:
                """
                Here, I filtered the codes I put in the try except block because 
                some users do not have all the codes.
                """
                url_list = list()
                try:
                    name = self.driver.find_element(By.XPATH , '/html/body/div[1]/div[4]/main/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/h1/span[1]').text
                    if name == "":
                        name = "null"
                except:
                    name = "null"
                username = self.driver.find_element(By.XPATH , '/html/body/div[1]/div[4]/main/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/h1/span[2]').text
                try:
                    about = self.driver.find_element(By.XPATH , '/html/body/div[1]/div[4]/main/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div').text
                except:
                    about = "null"
                following = self.driver.find_element(By.XPATH , '/html/body/div[1]/div[4]/main/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/a[1]/span').text
                followers = self.driver.find_element(By.XPATH , '/html/body/div[1]/div[4]/main/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/a[1]/span').text
                try:
                    """
                    I printed some of the data that I wanted to be printed according to the conditions
                    """
                    urls = self.driver.find_elements(By.XPATH , '/html/body/div[1]/div[4]/main/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/ul/li/a')
                    for url in urls:
                        url_list.append(url.text)
                    print(colorama.Fore.CYAN + f" Name: {name}\n Username: {username}\n About: {about}\n Followers: {following}\n Followers: {followers}")
                    if len(url_list) > 0:
                        print(f"Url List: {url_list[0]}")
                        for i in range(1, len(url_list)):
                            print(url_list[i])
                except:
                    print(colorama.Fore.CYAN +
                        f" Name: {name}\n Username:{username}\n About: {about}\n Followers: {following}\n Followers: {followers}")
                    print("-" * 30)
                    self.driver.quit()

            except:
                print(colorama.Fore.RED+" There is no such user!!")
                self.driver.quit()
        else:
            print(colorama.Fore.RED+" There is no such user!!!")
            self.driver.quit()
    def Repostry_Github(self):
        """
            Repositories with more than one number run in the try block.
        """
        try:
            new_url = self.driver.get(self.url + "?tab=repositories")
            response = requests.get(self.driver.current_url)
            num = 1
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            button = self.driver.find_element(By.XPATH, '//*[@id="user-repositories-list"]/div/div/a').click()
            print(colorama.Fore.RED+"Repositories;")
            while True:
                bs = BeautifulSoup(response.text, "html.parser")
                rep_url = bs.find_all("a" , attrs={"itemprop":"name codeRepository"})

                for url in rep_url:
                    print(colorama.Fore.RED + f"{num})" + colorama.Fore.BLUE + url.text[6:])
                    num += 1
                time.sleep(1)
                time.sleep(1)
                try:
                    button = self.driver.find_element(By.XPATH, '//*[@id="user-repositories-list"]/div/div/a[2]')
                except:
                    break
                if button.get_attribute("disabled"):
                    break
                else:
                    button.click()
                    response = requests.get(self.driver.current_url)
        except:
            """
            In the Except block, I equipped it for those that
             have no repositories or only one page.
            """
            new_url = self.driver.get(self.url + "?tab=repositories")
            response = requests.get(self.driver.current_url)
            num = 1
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            bs = BeautifulSoup(response.text, "html.parser")
            rep_url = bs.find_all("a", attrs={"itemprop": "name codeRepository"})
            if len(rep_url) == 0:
                print(colorama.Fore.RED+" Repositories:None")
            else:
                print(colorama.Fore.RED + " Repositories;")
                for url in rep_url:
                    print(colorama.Fore.BLUE + f" {num})" + url.text[6:])
                    num += 1
class Git_Write(object):
    def __init__(self,user):
        self.user = user
        self.url = f"https://github.com/{self.user}"
        if os.name == "nt":
            self.options = webdriver.ChromeOptions()
            self.options.add_argument('--headless')
            self.driver = webdriver.Chrome(options=self.options)
            self.driver.get(self.url)
        elif os.name == "posix":
            self.options = webdriver.FirefoxOptions()
            self.options.add_argument('--headless')
            self.driver = webdriver.Firefox(options=self.options)
            self.driver.get(self.url)
        with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
            f.write(f"{15*'*'} GitHub {15*'*'}\n")
    def Get_Github(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            try:
                url_list = list()
                try:
                    name = self.driver.find_element(By.XPATH , '/html/body/div[1]/div[4]/main/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/h1/span[1]').text
                    if name == "":
                        name = "null"
                except:
                    name = "null"
                username = self.driver.find_element(By.XPATH , '/html/body/div[1]/div[4]/main/div[2]/div/div[1]/div/div[2]/div[1]/div[2]/h1/span[2]').text
                try:
                    about = self.driver.find_element(By.XPATH , '/html/body/div[1]/div[4]/main/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/div').text
                except:
                    about = "null"
                following = self.driver.find_element(By.XPATH , '/html/body/div[1]/div[4]/main/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/a[1]/span').text
                followers = self.driver.find_element(By.XPATH , '/html/body/div[1]/div[4]/main/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[2]/div/a[1]/span').text
                try:
                    urls = self.driver.find_elements(By.XPATH , '/html/body/div[1]/div[4]/main/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/ul/li/a')
                    for url in urls:
                        url_list.append(url.text)
                    with open(f"{self.user}.txt", "a" , encoding="utf-8") as f:
                        f.write(f" Name: {name}\n Username: {username}\n About: {about}\n Followers: {following}\n Followers: {followers}\n")
                    if len(url_list) > 0:
                        with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                            for i in range(0, len(url_list)-1):
                                f.write(url_list[i])
                except:
                    with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                        f.write(f" Name: {name}\n Username:{username}\n About: {about}\n Followers: {following}\n Followers: {followers}")
            except:
                with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                    f.write("none\n")
        else:
            with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                f.write("none\n")
    def Repostry_Github(self):
        try:
            new_url = self.driver.get(self.url + "?tab=repositories")
            response = requests.get(self.driver.current_url)
            num = 1
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            button = self.driver.find_element(By.XPATH, '//*[@id="user-repositories-list"]/div/div/a').click()
            with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                f.write("Repositories;")
            while True:
                bs = BeautifulSoup(response.text, "html.parser")
                rep_url = bs.find_all("a" , attrs={"itemprop":"name codeRepository"})
                with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                    for url in rep_url:
                        f.write(f"{num})" + url.text[6:])
                        num += 1
                time.sleep(1)
                time.sleep(1)
                try:
                    button = self.driver.find_element(By.XPATH, '//*[@id="user-repositories-list"]/div/div/a[2]')
                except:
                    break
                if button.get_attribute("disabled"):
                    break
                else:
                    button.click()
                    response = requests.get(self.driver.current_url)
        except:
            new_url = self.driver.get(self.url + "?tab=repositories")
            response = requests.get(self.driver.current_url)
            num = 1
            time.sleep(1)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            bs = BeautifulSoup(response.text, "html.parser")
            rep_url = bs.find_all("a", attrs={"itemprop": "name codeRepository"})

            if len(rep_url) == 0:
                with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                    f.write(" Repositories:None")
            else:
                with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                    f.write(" Repositories;")
                    for url in rep_url:
                        f.write(f" {num})" + url.text[6:] )
                        num += 1














