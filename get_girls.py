# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 16:05:33 2016

@author: welion
"""

import os


from bs4 import BeautifulSoup
import requests



URL_BASE='http://s2.lulujjs.info/pw/'
PATH = 'C:\Users\welion\Downloads\pic-get\'
URL_SITE='http://s2.lulujjs.info/pw/thread.php?fid=14&page=2'

class Take_Girls():
    def Get_link(self,URL):
        pics = []
        page=requests.get(URL).content
        bs1=BeautifulSoup(page).findAll('div',{"class":"tpc_content"})
        for i in bs1:
            for j in i.findAll('img'):
                p_link = j.get('src')
                pics.append(p_link)
        return pics

    def Get_page_link(self,URL):
        URL_BASE = 'http://s2.lulujjs.info/pw/'
        page_list=[]
        page=requests.get(URL).content
        bs2=BeautifulSoup(page)
        for i in bs2.findAll('h3'):
            buttom =str(i.find('a').get('href'))
            page_link=URL_BASE + buttom
            page_list.append(page_link)

        return page_list


    def Download_Pic(self,pics,PATH):
        for i in range(len(pics)):
            name = str(pics[i].split('/')[-1])
            try:
                pic = requests.get(pics[i]).content
                with open(name,'wb') as f:
                    f.write(pic)
                    print "Download " + name + " ok!"
                    f.close()
            except Exception:
                pass

if __name__=='__main__':

    URL1='http://s2.lulujjs.info/pw/htm_data/14/1608/410949.html'
    link_list = Take_Girls().Get_page_link(URL_SITE)

    #pics_list=Take_Girls().Get_link(URL1)
    #print pics_list
    os.chdir(PATH)
    for i in link_list:
        pics_list = Take_Girls().Get_link(i)
        print pics_list
        Take_Girls().Download_Pic(pics_list,PATH)
            
