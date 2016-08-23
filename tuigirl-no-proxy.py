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

PATH = 'C:\Users\welion\Downloads\pic-get\\tuigirl\\'
URL_BASE='http://www.xiuren.org/'

PAGE_URL = 'http://www.xiuren.org/category/miitao.html'

GIRL_URL = 'http://www.xiuren.org/tuigirl-068.html'


class Tui_Girl():
    def make_girl_url(self):
        girl_list = []
        for i in range(10,74):
            url = 'http://www.xiuren.org/tuigirl-0'+str(i)+'.html'
            girl_list.append(url)
        return girl_list
        
    def tui_special_list(self):
        url_list = []        
        special_list = []

        for i in range(1,8):
            url = 'http://www.xiuren.org/category/TuiGirl-'+str(i)+'.html'
            url_list.append(url)
        for i in url_list:
            girl_list = self.get_special_girl_list(i)
            special_list = special_list + girl_list
        return special_list
     
    def get_special_girl_list(self,PAGE_URL):
         resp = requests.get(PAGE_URL).content
         girl_list = []
         obj = BeautifulSoup(resp, 'lxml').findAll('a',{'target':'_blank'})
         for i in obj:
             if str(i.get('href')).find("special") > 0:
                 girl_list.append(i.get('href'))
         return girl_list
       
        
    
    def get_page_list(self,URL_BASE):
        resp=requests.get(URL_BASE).content
        page_list = []
        obj=BeautifulSoup(resp,'lxml').findAll('a')
        for i in obj:
            if str(i.get('href')).find('category') > 0:
                page_list.append(i.get('href'))
    
        return page_list
    
    def get_girl_list(self,PAGE_URL):
        resp = requests.get(PAGE_URL).content
        girl_list = []
        obj = BeautifulSoup(resp, 'lxml').findAll('a',{'target':'_blank'})
        for i in obj:
            if str(i.get('href')).find("xiuren") > 0:
                girl_list.append(i.get('href'))
        print girl_list
        return girl_list
    
    def get_img_list(self,GIRL_URL):
        resp = requests.get(GIRL_URL).content
        img_list = []
        obj = BeautifulSoup(resp, 'lxml').findAll('a')
        for i in obj:
            if str(i.get('href')).find('jpg') > 0:
                img_list.append(i.get('href'))
    
        return img_list
        

    
    def download_pic(self,pics,PATH):
    
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

#
#if __name__=='__main__':
#
#    os.chdir(PATH)
#    link_list = Tui_Girl().make_girl_url()
#    page_num = len(link_list)
#
#    threads = []
#
#    for i in range(page_num):
#        img_list = Tui_Girl().get_img_list(link_list[i])
#
#        print img_list
#
#        t = threading.Thread(target=Tui_Girl().download_pic,args=(img_list,PATH))
#        threads.append(t)
#
#    for t in threads:
#        t.setDaemon(True)
#        t.start()
#        print "Thread ON !" + "    " + time.ctime()
#    t.join()
#
#    print "All Done ---------" + time.ctime()


if __name__=='__main__':

    os.chdir(PATH)
    
    link_list = Tui_Girl().tui_special_list()
    page_num = len(link_list)

    threads = []

    for i in range(page_num):
        img_list = Tui_Girl().get_img_list(link_list[i])
        t = threading.Thread(target=Tui_Girl().download_pic,args=(img_list,PATH))
        threads.append(t)

    for t in threads:
        t.setDaemon(True)
        t.start()
        print "Thread ON !" + "    " + time.ctime()
    t.join()

    print "All Done ---------" + time.ctime()


