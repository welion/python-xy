#-*- encoding:utf-8 -*-
#/usr/bin/env python

import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import socks
import socket
import requests
import urllib,urllib2
from bs4 import BeautifulSoup
import threading
import time

PATH = '/home/welion/Downloads/xiuren'
URL_BASE='http://www.xiuren.org/'
URL='http://youaremywordliu.tumblr.com/'
PAGE_URL = 'http://www.xiuren.org/category/miitao.html'
GIRL_URL = 'http://www.xiuren.org/miitao-015.html'

socks.set_default_proxy(socks.SOCKS5,'127.0.0.1',1080)
socket.socket=socks.socksocket



def get_page_list(URL_BASE):
    resp=requests.get(URL_BASE).content
    page_list = []
    obj=BeautifulSoup(resp,'lxml').findAll('a')
    for i in obj:
        if str(i.get('href')).find('category') > 0:
            page_list.append(i.get('href'))

    return page_list

def get_girl_list(PAGE_URL):
    resp = requests.get(PAGE_URL).content
    girl_list = []
    obj = BeautifulSoup(resp, 'lxml').findAll('a',{'target':'_blank'})
    for i in obj:
        if str(i.get('href')).find("xiuren") > 0:
            girl_list.append(i.get('href'))
    return girl_list

def get_img_list(GIRL_URL):
    resp = requests.get(GIRL_URL).content
    img_list = []
    obj = BeautifulSoup(resp, 'lxml').findAll('a')
    for i in obj:
        if str(i.get('href')).find('jpg') > 0:
            img_list.append(i.get('href'))

    return img_list

def download_pic(pics,PATH):

        for i in range(len(pics)):
            name = str(pics[i].split('/')[-1])
            try:
                if not os.path.exists(PATH+name):
                    pic = requests.get(pics[i]).content
                    with open(name,'wb') as f:
                        f.write(pic)
                        print "Download " + name + " ok!" + " ------- " + str(time.ctime())
                        f.close()
                else:
                    print name + " Already Downloaded :)"
            except Exception:
                pass

if __name__=='__main__':
    os.chdir(PATH)
    girl_list = []
    page_list = get_page_list(URL_BASE)
    for i in page_list[0:4]:
        girl_list = girl_list + get_girl_list(i)

    print len(girl_list)
    img_list = []
    for i in girl_list[0:10]:
        img_list = img_list + get_img_list(i)
    print img_list
    print len(img_list)

    download_pic(img_list,PATH)


