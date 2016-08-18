# -*- coding: utf-8 -*-
"""
Created on Tue May 24 15:47:12 2016

@author: welion
"""

#filename: Get-ss-acct 
#To get a account from www.ishadowsocks.net

import urllib
from urllib2 import HTTPError
from bs4 import BeautifulSoup

URL="http://www.ishadowsocks.net/"

def Get_Page(URL):
    try:
        html = urllib.urlopen(URL)
    except HTTPError as e:
        return None
    page = html.read()
    return page

def Sort_Page(html_page):
    Server_list=[]
    bsObj = BeautifulSoup(html_page)
    Server_text = bsObj.findAll("div",{"class":"col-lg-4 text-center"})
    for i in Server_text[0:3]:
        for j in i.findAll({"h4"}):
            lines = str(j.get_text()).split(':')
            if len(lines) > 1:
                Server_list.append(lines)            
    return Server_list
            
            
html_page = Get_Page(URL)
list1 = Sort_Page(html_page)

for i in list1:
    print "%s " %i
dict1 = dict(list1)

#    name,element = str(i).split(u':')
#    print name + "=======" + element
    
    
    