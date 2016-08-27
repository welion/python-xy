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
import socket
import socks
import urllib2
from sockshandler import SocksiPyHandler

from bs4 import BeautifulSoup
import time


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

    def Get_list(self,page):
        bsobj = BeautifulSoup(page,'lxml')
        h4_list=[]
        ss_list=[]
        for i in bsobj.findAll('h4'):
            h4_list.append(i.text)
        for i in range(5):
            server_dict={}
            server = h4_list[i*7:(i+1)*7]
            item_info=str(server[0]).split(":")[-1]
            server_dict['server'] = item_info
            item_info=str(server[1]).split(":")[-1]
            server_dict['server_port'] = item_info
            item_info=str(server[2]).split(":")[-1]
            server_dict['password'] = item_info
            item_info=str(server[3]).split(":")[-1]
            server_dict['method'] = item_info
            item_info=str(server[4]).split(":")[-1]
            server_dict['status'] = item_info
            if server_dict['status'] == '正常':
                ss_list.append(server_dict)
        return ss_list

    def Test_SS_speed(self,ss_list):
        result_list = []
        for i in range(len(ss_list)):
            server_port = "108"+str(i)
            command = "sslocal -s " + "\"" +ss_list[i]['server']+ "\""  + " -p " + "\"" +ss_list[i]['server_port'] + "\"" + " -l " + server_port +  " -k " + "\"" + ss_list[i]['password'] + "\"" + " -m " +  "\"" + ss_list[i]['method'] + "\"" + " &"
            print command
            os.system(command)
            time.sleep(2)
            opener = urllib2.build_opener(SocksiPyHandler(socks.SOCKS5, "127.0.0.1", int(server_port) ))
            start_time = time.time()
            try:

                if opener.open('https://www.tumblr.com/').getcode()==200:
                    end_time = time.time()
                    speed = end_time - start_time
                    opener.close()
                else:
                    speed = -1
            except Exception:
                    speed = -1
                    pass
            ss_list[i]['speed']=speed
            result_list.append(ss_list[i])

        time.sleep(1)
        os.system("pkill sslocal")
        return result_list








if __name__ == '__main__':
    page = Free_SS().Get_Page()

    list = Free_SS().Get_list(page)
    print Free_SS().Test_SS_speed(list)
