#!/usr/bin/env python

import urllib
import urllib2
from bs4 import BeautifulSoup

html = urllib.urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)

print html
