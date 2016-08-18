# -*- coding: utf-8 -*-
"""
Created on Mon Aug 15 16:05:33 2016

@author: welion
"""

import os

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup
import requests


URL_BASE='http://c2.1024mx.info/pw/'
#PATH = '/data/public/'

class Take_Girls():
    def Get_link(self,URL):
        pics = []
        try:
            page=requests.get(URL).content
            bs1=BeautifulSoup(page).findAll('div',{"class":"tpc_content"})
            for i in bs1:
                for j in i.findAll('img'):
                    p_link = j.get('src')
                    pics.append(p_link)
            return pics
        except :
            print "Get link Error..."
            return None
            
    def Get_file_name(self,pics_list):
        name_list = []
        for i in pics_list:
            name.append(i.split('/')[-1])
        return name_list
    
    def Download_Pic(self,pics,PATH):
        for i in range(len(pics)):
            name = str(pics[i].split('/')[-1])
            pic = requests.get(pics[i]).content
            with open(name,'wb') as f:
                f.write(pic)
                print "Download " + name + " ok!"
                f.close()

if __name__=='__main__':
    URL='http://c2.1024mx.info/pw/htm_data/14/1608/409420.html'    
    pics_list=Take_Girls().Get_link(URL)
    print pics_list
    os.chdir("C:\Users\welion\Downloads\pic-get")
    PATH="C:\Users\welion\Downloads\pic-get"
    Take_Girls().Download_Pic(pics_list,PATH)
                    
            