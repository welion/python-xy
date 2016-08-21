#-*- encoding:utf-8 -*-
#!/usr/bin/env python

ROSI_BASE  = 'http://www.mmxyz.net/'
ROSI_BASE2 = 'http://www.mmxyz.net/category/rosi/yuer/'
ROSI_BASE3 = 'http://www.mmxyz.net/category/rosi/xiaomao/'
ROSI_BASE4 = 'http://www.mmxyz.net/category/rosi/xinxin/'
PAGE_URL='http://www.mmxyz.net/rosi-1714/'

import os
import time
import threading
import requests
from bs4 import BeautifulSoup


import sys
reload (sys)
sys.setdefaultencoding('utf-8')

PATH = '/home/welion/Downloads/rosi/'

class Get_ROSI():
    def Get_page_list(self,ROSI_BASE):
        page_list = []
        basepage = requests.get(ROSI_BASE).content
        baseobj = BeautifulSoup(basepage,'lxml')
        for i in baseobj.findAll('a',{'class':'inimg'}):
            page_list.append(i.get('href'))

        return page_list

    def Get_img_list(self,PAGE_URL):
        img_list = []
        page = requests.get(PAGE_URL).content
        pageobj = BeautifulSoup(page,'lxml')
        for i in pageobj.findAll('img',{"class":"attachment-thumbnail"}):
            if i.get('src').find('150x150.jpg') > 0:
                img_link = str(i.get('src')).replace('-150x150','')
                img_list.append(img_link)

        return img_list

    def Download_Pic(self, pics, PATH):

        for i in range(len(pics)):
            name = str(pics[i].split('/')[-1])
            try:
                if not os.path.exists(PATH + name):
                    pic = requests.get(pics[i]).content
                    with open(name, 'wb') as f:
                        f.write(pic)
                        print "Download " + name + " ok!" + " ------- " + str(time.ctime())
                        f.close()
                else:
                    print name + " Already Downloaded :)"
            except Exception:
                pass

if __name__ == '__main__':
    os.chdir(PATH)
    page_list = Get_ROSI().Get_page_list(ROSI_BASE2)
    page_list.extend(Get_ROSI().Get_page_list(ROSI_BASE3))
    page_list.extend(Get_ROSI().Get_page_list(ROSI_BASE4))


    page_num = len(page_list)

    threads = []

    for i in range(page_num):
        img_list = Get_ROSI().Get_img_list(page_list[i])
        print img_list

        t = threading.Thread(target=Get_ROSI().Download_Pic,args=(img_list,PATH))
        threads.append(t)

    for t in threads:
        t.setDaemon(True)
        t.start()
        print "Threading ON!"
    t.join()

    print "All Over!"









