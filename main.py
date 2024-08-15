import colorama
import pyfiglet
import requests
from Tools import github as gt
from Tools import Facebook as fb
from Tools import Youtube as yt
from Tools import writing
from Tools import Reddit
from Tools import tumblr
from Tools import pinterest
from Tools import about_me
from Tools import twitter
from Tools import Vk
from Tools import Flickr
from Tools import Vimeo
from Tools import Medium_me
from Tools import instagram
from Tools import linkedin
class Main_Frame():
    def __init__(self):
        self.App_list()
        self.res = input("\n" * 2 + " Select the action/scan you want to perform: ")
        self.Select()
    def Select(self):
        if self.res == "1":
            try:
                if __name__ == "__main__":
                    instagram.Instagran().Get()
            except:
                pass
        elif self.res == "2":
            try:
                if __name__ == "__main__":
                    fb.Facebook()
            except:
                pass
        elif self.res == "3":
            try:
                if __name__ == "__main__":
                    twitter.Twitter().Get()
            except:
                pass
        elif self.res == "4":
            try:
                if __name__=="__main__":
                    Reddit.Reddit().Get()
            except:
                pass
        elif self.res == "5":
            try:
                yt.Youtube().Get_Youtube()
            except:
                pass
        elif self.res == "6":
            try:
                if __name__ == "__main__":
                    pinterest.Pinterest().Get()
            except:
                pass
        elif self.res == "7":
            if __name__ == "__main__":
                try:
                    gts = gt.Github()
                    gts.Get_Github()
                    gts.Repostry_Github()
                except:
                    pass
        elif self.res == "8":
            try:
                if __name__ == "__main__":
                    linkedin.Linkedin().Get()
            except:
                pass
        elif self.res == "9":
            try:
                if __name__ == "__main__":
                    about_me.About_me().Get()
            except:
                pass
        elif self.res == "10":
            try:
                if __name__ == "__main__":
                    Medium_me.Medium_me().Get()
            except:
                pass
        elif self.res == "11":
            try:
                if __name__ == "__main__":
                    tumblr.Tumblr().Get()
            except:
                pass
        elif self.res == "12":
            try:
                if __name__ == "__main__":
                    Vimeo.Vimeo().Get()
            except:
                pass
        elif self.res == "13":
            try:
                if __name__ == "__main__":
                    Flickr.Flickr().Get()
            except:
                pass
        elif self.res == "14":
            try:
                if __name__ == "__main__":
                    Vk.VK().Get()
            except:
                pass
        elif self.res == "15":
            if __name__ == "__main__":
                print(colorama.Fore.WHITE + " Wait a moment while the printing process is in progress...")
                writing.Write_information().Get()
                print(colorama.Fore.WHITE + " Finished...")
        elif self.res == "16":
            class Links(object):
                def __init__(self):
                    self.user = input(colorama.Fore.RED + " Username: ")
                    self.link_list = ["https://www.instagram.com/","https://facebook.com/public","https://x.com/",
                                      "https://www.reddit.com/user/","https://www.youtube.com/@","https://pinterest.com/",
                                      "https://github.com/","https://tr.linkedin.com/","https://about.me/",
                                      "https://medium.com/@","https://www.tumblr.com/","https://vimeo.com/",
                                      "https://www.flickr.com/photos/","https://vk.com/"]
                    self.app_name_list = ["İnstagram" , "Facebook" , "Twitter" , "Reddit" , "YouTube" , "Pinterest",
                                          "Github" , "Linkedin" , "About.me" , "Medium.me" , "Tumblr" , "Vimeo",
                                          "Flickr" , "VK"]
                def result(self):
                    number = 0
                    for i in self.link_list:
                        new_url = i + self.user
                        response = requests.get(new_url)
                        if response.status_code == 200:
                            print(colorama.Fore.CYAN + "[" + colorama.Fore.LIGHTGREEN_EX + "ACTİVE" + colorama.Fore.CYAN + "]" + colorama.Fore.RED + self.app_name_list[number] + ":" + colorama.Fore.WHITE + new_url)
                            number += 1
                        else:
                            print(colorama.Fore.CYAN + "[" + colorama.Fore.LIGHTYELLOW_EX + "INACTIVE" + colorama.Fore.CYAN + "]" + colorama.Fore.RED + self.app_name_list[number] + ":" + colorama.Fore.WHITE + new_url)
                            number += 1
            Links().result()
        else:
            print(colorama.Fore.RED + "Please make a valid choice!!!")
    def App_list(self):
        """
        An interface that users can use has been prepared
        """
        nesne = pyfiglet.Figlet("slant")
        print("\n" * 2)
        print(colorama.Fore.RED + "   ───▄█▌─▄─▄─▐█▄             __  __               ________ _______________           ")
        print(colorama.Fore.RED + "   ───██▌▀▀▄▀▀▐██            / / / /_______  _____/__   __/ ___  /  ____  /           ")
        print(colorama.Fore.RED + "   ───██▌─▄▄▄─▐██           / / / / ___/ _/ / ___/  /  / / /  / /  /   / /            ")
        print(colorama.Fore.RED + "   ───▀██▌▐█▌▐██▀          / /_/ (__  )  __/ /     /  / / /__/ /  /___/ /             ")
        print(colorama.Fore.RED + "   ▄██████─▀─██████▄      |____/____//___/_/ /    /__/ /_____ /_____   /    V.1.0.0   ")
        print(colorama.Fore.RED + "                                                                ___/  /               ")
        print(colorama.Fore.RED + "                                                               /_____/                ")

        print("\n" * 2)



        """
        Applications to be scanned are listed to the user
        """
        app_list = ["Instagram", "Facebook", "Twitter", "Reddit",
                    "Youtube", "Pinterest", "Github", "LinkedIn",
                    "About.me", "Medium.me", "Tumblr", "Vimeo",
                    "Flickr", "VK","Print All"]
        """
        ["Instagram", "LinkedIn"]
        """
        app_1 = colorama.Fore.CYAN + "[" + colorama.Fore.RED + f"{str(1)}" + colorama.Fore.CYAN + "]" + colorama.Fore.GREEN + f"{app_list[0]} "
        app_2 = colorama.Fore.CYAN + "[" + colorama.Fore.RED + f"{str(2)}" + colorama.Fore.CYAN + "]" + colorama.Fore.GREEN + f"{app_list[1]}"
        app_3 = colorama.Fore.CYAN + "[" + colorama.Fore.RED + f"{str(3)}" + colorama.Fore.CYAN + "]" + colorama.Fore.GREEN + f"{app_list[2]}"
        app_4 = colorama.Fore.CYAN + "[" + colorama.Fore.RED + f"{str(4)}" + colorama.Fore.CYAN + "]" + colorama.Fore.GREEN + f"{app_list[3]} "
        app_5 = colorama.Fore.CYAN + "[" + colorama.Fore.RED + f"{str(5)}" + colorama.Fore.CYAN + "]" + colorama.Fore.GREEN + f"{app_list[4]}"
        app_6 = colorama.Fore.CYAN + "[" + colorama.Fore.RED + f"{str(6)}" + colorama.Fore.CYAN + "]" + colorama.Fore.GREEN + f"{app_list[5]}"
        app_7 = colorama.Fore.CYAN + "[" + colorama.Fore.RED + f"{str(7)}" + colorama.Fore.CYAN + "]" + colorama.Fore.GREEN + f"{app_list[6]} "
        app_8 = colorama.Fore.CYAN + "[" + colorama.Fore.RED + f"{str(8)}" + colorama.Fore.CYAN + "]" + colorama.Fore.GREEN + f"{app_list[7]}"
        app_9 = colorama.Fore.CYAN + "[" + colorama.Fore.RED + f"{str(9)}" + colorama.Fore.CYAN + "]" + colorama.Fore.GREEN + f"{app_list[8]}"
        app_10 = colorama.Fore.CYAN + "[" + colorama.Fore.RED + f"{str(10)}" + colorama.Fore.CYAN + "]" + colorama.Fore.GREEN + f"{app_list[9]} "
        app_11 = colorama.Fore.CYAN + "[" + colorama.Fore.RED + f"{str(11)}" + colorama.Fore.CYAN + "]" + colorama.Fore.GREEN + f"{app_list[10]}"
        app_12 = colorama.Fore.CYAN + "[" + colorama.Fore.RED + f"{str(12)}" + colorama.Fore.CYAN + "]" + colorama.Fore.GREEN + f"{app_list[11]}"
        app_13 = colorama.Fore.CYAN + "[" + colorama.Fore.RED + f"{str(13)}" + colorama.Fore.CYAN + "]" + colorama.Fore.GREEN + f"{app_list[12]} "
        app_14 = colorama.Fore.CYAN + "[" + colorama.Fore.RED + f"{str(14)}" + colorama.Fore.CYAN + "]" + colorama.Fore.GREEN + f"{app_list[13]}"
        app_15 = colorama.Fore.CYAN + "[" + colorama.Fore.RED + f"{str(15)}" + colorama.Fore.CYAN + "]" + colorama.Fore.GREEN + f"{app_list[14]}"
        app_16 = colorama.Fore.CYAN + "[" + colorama.Fore.RED + f"{str(16)}" + colorama.Fore.CYAN + "]" + colorama.Fore.GREEN + f"Check all"
        result1 = " " * 5 + app_1 + " " * 3 + app_2 + " " * 3 + app_3
        result2 = " " * 5 + app_4 + " " * 6 + app_5 + " " * 4 + app_6
        result3 = " " * 5 + app_7 + " " * 6 + app_8 + " " * 3 + app_9
        result4 = " " * 5 + app_10 + " " * 2 + app_11 + " " * 4 + app_12
        result5 = " " * 5 + app_13 + " " * 5 + app_14 + " " * 8 + app_15
        result6 = " " * 21 + app_16
        print(result1)
        print(result2)
        print(result3)
        print(result4)
        print(result5)
        print(result6)
while True:
    if __name__ == "__main__":
        Main_Frame()
        query = input(colorama.Fore.RED + "Do you want to continue the process (Y/N): ")
        if query.lower() == "y":
            continue
        elif query.lower() == "n":
            break
        else:
            print(colorama.Fore.RED + "Please make a valid choice!!!")
            query = input(colorama.Fore.RED + "Do you want to continue the process (Y/N): ")



