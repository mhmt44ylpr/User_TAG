from Tools import Youtube
from Tools import Facebook
from Tools import github
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
class Write_information(object):
    def __init__(self):
        self.user = input(" Username: ")
        self.user = self.user.replace(" " , "")
    def Get(self):
        Youtube.Yt_write(self.user)
        github.Git_Write(self.user).Get_Github()
        Facebook.Facebook_writer(self.user)
        Reddit.Reddit_writer(self.user).Get()
        tumblr.Tumblr_Write(self.user).Get()
        pinterest.Pinterest_writer(self.user).Get()
        about_me.About_me_writer(self.user).Get()
        twitter.Twitter_Writer(self.user).Get()
        Vk.VK_writer(self.user).Get()
        Flickr.Flickr_Write(self.user).Get()
        Vimeo.Vimeo_writer(self.user).Get()
        Medium_me.Medium_me_writer(self.user).Get()
        Medium_me.Medium_me_writer(self.user).About()
        instagram.Instagran_Writer(self.user).Get()

