# -*- coding: utf-8 -*-
"""
Created on Wed May 11 21:55:54 2016

@author: welion
"""

<<<<<<< HEAD
from urllib.request import urlopen
from bs4.BeautifulSoup import 
=======
from urllib import urlopen
from urllib2 import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read())
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title
    
title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print "Title could not be found"
else: 
    print title
>>>>>>> origin/master
