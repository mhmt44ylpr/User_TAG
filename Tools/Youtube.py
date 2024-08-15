import colorama
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time
import os
class Youtube():
    def __init__(self):
        self.user = input(" YouTube Channel Username: ")
        self.user = self.user.replace(" " , "")
        self.url = f"https://www.youtube.com/@{self.user}"
        self.dict = dict()
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
    def Get_Youtube(self):
        try:
            """
            Checked whether the channel exists
            """
            time.sleep(1)
            response = requests.get(self.url)
            if response.status_code == 200:
                print("\n" * 2)
                self.ChannelName()
                but = self.driver.find_element(By.XPATH,
                                               '//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-description-preview-view-model/truncated-text/button/span/span')
                but.click()
                self.result()
            else:
                print(colorama.Fore.RED + " There is no such user!!!")
                self.driver.quit()
        except:
            print(colorama.Fore.RED + " There is an unknown error!!! Please contact us.")
            self.driver.quit()
    def ChannelName(self):
        """
        channel name and video number received
        """
        cn = self.driver.find_element(By.XPATH , '//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-dynamic-text-view-model/h1/span')
        print(colorama.Fore.RED + f" Channel name :" + colorama.Fore.BLUE + cn.text)
        def videos():
            vv = self.driver.find_element(By.XPATH , '//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-content-metadata-view-model/div[2]/span[3]')
            print(colorama.Fore.RED +" Videos:"+ colorama.Fore.BLUE + vv.text)
        videos()
    def links(self):
        """
        Links shared on the channel were received
        """
        links = self.driver.find_elements(By.XPATH ,'//*[@id="link-list-container"]/yt-channel-external-link-view-model/div/span')
        links_li = list()
        for link in links:
            links_li.append(link.text)
        for i in range(0 , int(len(links_li)/2)):
            print(colorama.Fore.RED + " " + links_li[i*2] + ": " +colorama.Fore.BLUE+ links_li[i*2 + 1])
    def result(self):
        time.sleep(2)
        self.County()
        self.subs()
        self.links()
    def County(self):
        """
        country information received
        """
        ct = self.driver.find_element(By.XPATH ,'//*[@id="additional-info-container"]/table/tbody/tr[8]/td[2]')
        print(colorama.Fore.RED +f" Counrty:"+ colorama.Fore.BLUE + ct.text )
    def subs(self):
        """
        subs information received
        """
        sb = self.driver.find_element(By.XPATH , '//*[@id="additional-info-container"]/table/tbody/tr[4]/td[2]')
        print(colorama.Fore.RED + f" Number of subscribers:"+ colorama.Fore.BLUE +  sb.text[:-5])
class Yt_write():
    def __init__(self,user):
        self.user = user
        self.dict = dict()
        self.url = f"https://www.youtube.com/@{user}"
        if os.name == "nt":
            self.options = webdriver.ChromeOptions()
            self.options.add_argument('--headless')
            self.driver = webdriver.Chrome(options=self.options)
            self.information_list = list()
            self.driver.get(self.url)
        elif os.name == "posix":
            self.options = webdriver.FirefoxOptions()
            self.options.add_argument('--headless')
            self.driver = webdriver.Firefox(options=self.options)
            self.information_list = list()
            self.driver.get(self.url)

        self.Get_Youtube()
    def Get_Youtube(self):
        with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
            f.write(f"{15 * '*'} Youtube {15 * '*'}\n")
        try:
            time.sleep(1)
            response = requests.get(self.url)
            if response.status_code == 200:
                self.ChannelName()
                but = self.driver.find_element(By.XPATH,
                                               '//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-description-preview-view-model/truncated-text/button/span/span')
                but.click()
                self.result()
                with open(f"{self.user}.txt" ,"a" ,encoding="utf-8") as f:
                    for i in self.information_list:
                        f.write(f"{i}\n")
                self.driver.quit()
            else:
                with open(f"{self.user}.txt", "a" , encoding="utf-8") as f:
                    f.write("None\n")
                    self.driver.quit()
        except:
            with open(f"{self.user}.txt", "a", encoding="utf-8") as f:
                f.write("None\n")
                self.driver.quit()
    def ChannelName(self):
        cn = self.driver.find_element(By.XPATH,
                                      '//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-dynamic-text-view-model/h1/span')
        x = f" Channel name :{cn.text}"
        self.information_list.append(x)
        def videos():
            vv = self.driver.find_element(By.XPATH,
                                          '//*[@id="page-header"]/yt-page-header-renderer/yt-page-header-view-model/div/div[1]/div/yt-content-metadata-view-model/div[2]/span[3]')
            v = f" Videos:{vv.text}"
            self.information_list.append(v)
        videos()
    def links(self):
        links = self.driver.find_elements(By.XPATH,
                                          '//*[@id="link-list-container"]/yt-channel-external-link-view-model/div/span')
        links_li = list()
        for link in links:
            links_li.append(link.text)
        for i in range(0, int(len(links_li) / 2)):
            nn = f" {links_li[i * 2]}: {links_li[i * 2 + 1]}"
            self.information_list.append(nn)
    def result(self):
        time.sleep(2)
        self.County()
        self.subs()
        self.links()
    def County(self):
        ct = self.driver.find_element(By.XPATH, '//*[@id="additional-info-container"]/table/tbody/tr[8]/td[2]')
        c = f" Counrty: {ct.text}) "
        self.information_list.append(c)
    def subs(self):
        sb = self.driver.find_element(By.XPATH, '//*[@id="additional-info-container"]/table/tbody/tr[4]/td[2]')
        s = f" Number of subscribers: {sb.text[:-5]}"
        self.information_list.append(s)


