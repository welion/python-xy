#!/usr/bin/env python

import os
import urllib
import json
from selenium import webdriver
from bs4 import BeautifulSoup
import time


VPN_URL = "https://www.mianvpn.com"


def Get_VPN(VPN_URL):
    driver =webdriver.PhantomJS()
    driver.get(VPN_URL)
    page = driver.page_source
    time.sleep(5)
    driver.close()
    bsobj = BeautifulSoup(page,'lxml')
    ss_obj = bsobj.findAll('div',{'id':'ss'})[0].findAll('div',{'id':'ssconfig_0'})
    ip = ss_obj[0].get('data-ip')
    method = ss_obj[0].get('data-method')
    passwd = ss_obj[0].get('data-passwd')
    port = ss_obj[0].get('data-port')

    ss_info = "{ \"server\":\"" + ip + "\", " + "\"server_port\": " + port + ", \"lcaol_port\":1080, " + "\"password\": " + "\"" + passwd + "\", " + "\"method\": " + "\"" + method + "\" }"
    return ss_info

def Get_VPN1():
    URL = 'https://api.mianvpn.com/ajax.php?verify=true&mod=getfreess&t=1471675338943'
    response = urllib.urlopen(URL)
    html = response.read().decode('utf-8')
    ss = json.loads(html)
    ip = ss[0]['i']
    method = ss[0]['m']
    passwd = ss[0]['pw']
    port = ss[0]['p']

    ss_info = "{ \"server\":\"" + ip + "\", " + "\"server_port\": " + port + ", \"lcaol_port\":1080, " + "\"password\": " + "\"" + passwd + "\", " + "\"method\": " + "\"" + method + "\" }"
    return ss_info


if __name__ == '__main__':
    # ss = Get_VPN(VPN_URL)
    ss =  Get_VPN1()
    with open('/tmp/ss.json','wb') as f:
        f.write(ss)








    
