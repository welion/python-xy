# -*- coding: utf-8 -*-
"""
Created on Wed Dec 09 18:16:14 2015

@author: welion
"""

import os,sys
import pycurl
import datetime
import time
import pymongo


def Moni(URL):
#    URL="http://yangfuliu.website:8888"
    c = pycurl.Curl()
    c.setopt(pycurl.URL, URL)
    c.setopt(pycurl.CONNECTTIMEOUT, 5)
    c.setopt(pycurl.TIMEOUT, 5)
    c.setopt(pycurl.NOPROGRESS, 1)
    c.setopt(pycurl.FORBID_REUSE, 1)
    c.setopt(pycurl.MAXREDIRS, 1)
    c.setopt(pycurl.DNS_CACHE_TIMEOUT,30)
    try:
        c.perform()
        print " "
    except Exception,e:
        print "connecion error:"+str(e)
        sys.exit()
    NAMELOOKUP_TIME =  c.getinfo(c.NAMELOOKUP_TIME)
    CONNECT_TIME =  c.getinfo(c.CONNECT_TIME)
    PRETRANSFER_TIME =   c.getinfo(c.PRETRANSFER_TIME)
    STARTTRANSFER_TIME = c.getinfo(c.STARTTRANSFER_TIME)
    TOTAL_TIME = c.getinfo(c.TOTAL_TIME)
    HTTP_CODE =  c.getinfo(c.HTTP_CODE)
    SIZE_DOWNLOAD =  c.getinfo(c.SIZE_DOWNLOAD)
    HEADER_SIZE = c.getinfo(c.HEADER_SIZE)
    SPEED_DOWNLOAD=c.getinfo(c.SPEED_DOWNLOAD)
    time_stamp= time.localtime(int(time.time()))
    DATETIME =  time.strftime('%Y%m%d%H%M%S',time_stamp)

    result = {"DATA_TIME":DATETIME,
              "URL":URL,
              "HTTP_CODE":HTTP_CODE,
             "NAMELOOKUP_TIME":NAMELOOKUP_TIME*1000,
             "CONNECT_TIME":CONNECT_TIME*1000,
             "PRETRANSFER_TIME":PRETRANSFER_TIME*1000,
             "STARTTRANSFER_TIME":STARTTRANSFER_TIME*1000,
             "TOTAL_TIME":TOTAL_TIME*1000,
             "SIZE_DOWNLOAD":SIZE_DOWNLOAD,
             "HEADER_SIZE":HEADER_SIZE,
             "SPEED_DOWNLOAD":SPEED_DOWNLOAD,}
    return result

def InsertDB(data,IP,PORT,DB_NAME):
    client = pymongo.MongoClient(IP,int(PORT))
    db = client[DB_NAME]
    post = db[DB_NAME]
    post.insert(data)

if __name__=='__main__':
    URL="http://yangfuliu.website:8888"
    URL_BOB="http://buy.bobcardjf.com/mall/ui/giftIndex.action"
    URL_HXB="http://creditshop.hxb.com.cn/index.html"
    URL_WZ="http://trip.wzbank.cn/BTSFlightM/ui/index"
    URL_SRCB="http://ccmall.srcb.com/mall/ui/giftIndex.action"
    IP='127.0.0.1'
    PORT=27018
    DB_NAME='monitor'
    ret=Moni(URL)
    ret_bob=Moni(URL_BOB)
    ret_hxb=Moni(URL_HXB)
    ret_wz=Moni(URL_WZ)
    ret_srcb=Moni(URL_SRCB)
    InsertDB(ret,IP,PORT,DB_NAME)
    InsertDB(ret_bob,IP,PORT,DB_NAME)
    InsertDB(ret_hxb,IP,PORT,DB_NAME)
    InsertDB(ret_wz,IP,PORT,DB_NAME)
    InsertDB(ret_srcb,IP,PORT,DB_NAME)
    exit()