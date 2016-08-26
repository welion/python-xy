#-*- encoding: utf-8 -*-
#!/usr/bin/env python
"""
get free acct from URL=http://freeshadowsocks.cf/

author: welion

"""
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import urllib
import os,sys
from bs4 import BeautifulSoup


class Free_SS():
    URL = 'http://freeshadowsocks.cf/'
    def Get_Page(self):
        try:
            page = urllib.urlopen(self.URL).read()
            return page
        except Exception:
            print "Get page from Freeshadowsocks.com Failed T^T "
            return None

    def Parse_Page(self,page):
        h4_list=[]
        ss_list=[]
        bsobj = BeautifulSoup(page,'lxml')
        for i in bsobj.findAll('h4'):
            h4_list.append(i.text)
        for i in range(5):
            server_dict={}
            server = h4_list[i*7:(i+1)*7]
            for j in range(4):
                item,item_info=str(server[j]).split(":")
                server_dict[item] = item_info
            ss_list.append(server_dict)


        return ss_list




if __name__ == '__main__':
    page = Free_SS().Get_Page()

    list = Free_SS().Parse_Page(page)
    for i in list:
        print i
        print "----------------------"