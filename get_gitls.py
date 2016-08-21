# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 16:05:33 2016

@author: welion
"""

import os
import time
import threading

from bs4 import BeautifulSoup
import requests


URL_BASE='http://c2.1024mx.info/pw/'
PATH = '/home/welion/Downloads/aiwei'
URL_SITE='http://c2.1024mx.info/pw/thread.php?fid=14'

class Take_Girls():
    def Get_link(self,URL):
        pics = []
        page=requests.get(URL).content
        bs1=BeautifulSoup(page,"lxml").findAll('div',{"class":"tpc_content"})
        for i in bs1:
            for j in i.findAll('img'):
                p_link = j.get('src')
                pics.append(p_link)
        return pics

    def Get_page_link(self,URL):
        URL_BASE = 'http://c2.1024mx.info/pw/'
        page_list=[]
        page=requests.get(URL).content
        bs2=BeautifulSoup(page,'lxml')
        for i in bs2.findAll('h3'):
            buttom =str(i.find('a').get('href'))
            page_link=URL_BASE + buttom
            page_list.append(page_link)

        return page_list


    def Download_Pic(self,pics,PATH):

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

    link_list = Take_Girls().Get_page_link(URL_SITE)

    print link_list

    print "-------------Get link_list OK-------------------"
    os.chdir(PATH)


    page_num = len(link_list)
    threads = []
    for i in range(page_num):
        pics_list = Take_Girls().Get_link(link_list[i])
        print pics_list

        t = threading.Thread(target=Take_Girls().Download_Pic,args=(pics_list,PATH))
        threads.append(t)

    for t in threads:
        t.setDaemon(True)
        t.start()
        print "Threading ON!"
    t.join()

    print "All Over!"
