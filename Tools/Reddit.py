from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import colorama
import os
class Reddit(object):
    def __init__(self):
        self.user = input(" Enter username: ")
        self.user = self.user.replace(" " , "")
        self.url = f'https://www.reddit.com/user/{self.user}'
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
            self.driver = webdriver.Firefox(options=self.options)
    def Get(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.driver.get(self.url)
                bs = BeautifulSoup(response.text, 'html.parser')
                name = bs.find('h1', attrs={"class":'text-24'}).text[20:]
                name = name.replace("\n" , "")
                print(colorama.Fore.RED +" Name:" + colorama.Fore.BLUE +  name)
                inf_num_list = list()
                inf_num = bs.find_all('p', attrs={"class":'m-0 text-neutral-content-strong text-14 font-semibold whitespace-nowrap'})
                for i in  inf_num:
                    i = i.text
                    i = i.replace('\n', '')
                    i = i.replace(' ', '')
                    inf_num_list.append(i)
                inf_tit_list = list()
                inf_tit = bs.find_all("p" , attrs={"class":'m-0 text-neutral-content-weak text-12 whitespace-nowrap truncate'})
                for i in inf_tit:
                    i = i.text
                    i = i.replace('\n', '')
                    inf_tit_list.append(i)
                for i in range(0,3):
                    print(" "+colorama.Fore.RED + inf_tit_list[i] + ":" + colorama.Fore.BLUE + inf_num_list[i])
            else:
                print(colorama.Fore.RED+" There is no such user!!!")
        except:
            print(colorama.Fore.RED + " There is no such user!!")
        self.driver.quit()
class Reddit_writer(object):
    def __init__(self,user):
        self.user = user
        self.url = f'https://www.reddit.com/user/{self.user}'
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
            self.driver = webdriver.Firefox(options=self.options)
    def Get(self):
        with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
            f.write(f"{15*'*'} Reddit {15*'*'}\n")
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                self.driver.get(self.url)
                bs = BeautifulSoup(response.text, 'html.parser')
                name = bs.find('h1', attrs={"class":'text-24'}).text[20:]
                name = name.replace("\n" , "")
                with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                    f.write(f" Name:{name}\n")
                inf_num_list = list()
                inf_num = bs.find_all('p', attrs={"class":'m-0 text-neutral-content-strong text-14 font-semibold whitespace-nowrap'})
                for i in  inf_num:
                    i = i.text
                    i = i.replace('\n', '')
                    i = i.replace(' ', '')
                    inf_num_list.append(i)
                inf_tit_list = list()
                inf_tit = bs.find_all("p" , attrs={"class":'m-0 text-neutral-content-weak text-12 whitespace-nowrap truncate'})
                for i in inf_tit:
                    i = i.text
                    i = i.replace('\n', '')
                    inf_tit_list.append(i)
                with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                    for i in range(0,3):
                        f.write(f" {inf_tit_list[i]}:{inf_num_list[i]}\n")
                self.driver.quit()
            else:
                with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                    f.write(" None\n")
                    self.driver.quit()
        except:
            with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                f.write(colorama.Fore.RED + " None\n")
        self.driver.quit()
