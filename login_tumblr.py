# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 12:31:38 2015

@author: welion
"""

#!/usr/bin/env python

import cookielib
import urllib
import urllib2
import argparse

ID_USERNAME = 'login_field'
ID_PASSWORD = 'password'
USERNAME = '353566165@qq.com'
PASSWORD = 'zwh12345'
LOGIN_URL = 'https://www.tumblr.com/login'
NORMAL_URL = 'https://www.tumblr.com/dashboard'

def extract_cookies_info():
    """ Fake login to a site with cookie """
    # set cookie jar
    cj = cookielib.CookieJar()
    login_data = urllib.urlencode({ID_USERNAME : USERNAME,
				ID_PASSWORD : PASSWORD})
    # create url opener
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    resp = opener.open(LOGIN_URL, login_data)
    print resp.read()

    # send login info
    for cookie in cj:
	print "-------First time cookie: %s--> %s" %(cookie.name, cookie.value)
	
    print "Headers : %s" %resp.headers

    # now access without any login info
    resp = opener.open(NORMAL_URL)
    for cookie in cj:
	print "++++Second time cookie: %s --> %s" %(cookie.name, cookie.value)

    print "Headers : %s" %resp.headers

if __name__ == '__main__':
    extract_cookies_info()