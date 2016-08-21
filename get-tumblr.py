import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import socks
import socket
import requests
import urllib,urllib2
from bs4 import BeautifulSoup

URL='http://youaremywordliu.tumblr.com/'
URL1='http://wu-sand.tumblr.com/'

socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',1080)
socket.socket=socks.socksocket

resp=requests.get(URL1).content
obj=BeautifulSoup(resp,'lxml').findAll('img')
for i in obj:
    print i

