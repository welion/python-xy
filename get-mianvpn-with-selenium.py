# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 13:07:21 2016

get mianvpn.com with selenium & PantomJS


@author: welion
"""

import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup
import requests


URL1='https://www.mianvpn.com/'
URL2="http://192.168.1.1/Main_Login.asp"
URL3='http://c2.1024mx.info/pw/thread.php?fid=14'
URL4='http://c2.1024mx.info/pw/htm_data/14/1608/408824.html'
URL5='http://c2.1024mx.info/pw/htm_data/14/1608/408833.html'
URL_BASE='http://c2.1024mx.info/pw/'
URL6='http://c2.1024mx.info/pw/thread.php?fid=16'
URL7='http://c2.1024mx.info/pw/htm_data/14/1608/409224.html'
URL8='http://c2.1024mx.info/pw/htm_data/14/1608/409220.html'

os.chdir('C:\\Users\welion\Downloads\pic-get')


bsobj = BeautifulSoup(requests.get(URL7).content)
pics = bsobj.findAll("div",{"class":"tpc_content"})
print pics
pic = []
for i in pics:
    for j in i.findAll('img'):
        p = j.get('src')
        pic.append(p)
        print p
print "List the pic OK"

name = []
for i in range(len(pic)):
    name.append(str(i) + '.jpg')
    
def GetPic(name,URL):
    picture=requests.get(URL).content
    f = open(name,'wb')
    f.write(picture)
    f.close()
    print "Get picture " + name + " OK!"

for i in range(len(pic)):
    GetPic(name[i],pic[i])
    
#def get_link_form_page(URL):
#    page = requests.get(URL).content
#    bs=BeautifulSoup(page)
#    h3=bs.findAll('h3')
#    print h3 
