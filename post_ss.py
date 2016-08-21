# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 10:07:59 2016

@author: welion
"""

ROUTE = '192.168.1.1'
LOGIN_URL = 'http://192.168.1.1/Main_Login.asp'
SS_PAGE = 'http://192.168.1.1/Main_Ss_Content.asp'

import os
import sys
import urllib
import json

SS_URL='https://api.mianvpn.com/ajax.php?verify=true&mod=getfreess&t=1471752067793'

resp = urllib.urlopen(SS_URL).read()
ss = json.loads(resp)

ss_ip = ss[0]['i']
ss_passwd = ss[0]['pw']
ss_method = ss[0]['m']
ss_port = ss[0]['p']

ss = "/koolshare/ss/new_ssconfig.sh restart" + " \"" + ss_ip + "\" " + " \"" + ss_passwd + "\" " + ss_port + " \""+ss_method + "\""
print ss



