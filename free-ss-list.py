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
import json
import socket
import socks
import urllib2
import paramiko
import requests
from sockshandler import SocksiPyHandler

from bs4 import BeautifulSoup
import time

ROUTE_HOST = "192.168.1.1"
ROUTE_SSH_PORT = 22222
ROUTE_USER_NAME = "admin"
ROUTE_USER_PASS = "!QAZ2wsx"


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



        SS_URL='https://api.mianvpn.com/ajax.php?verify=true&mod=getfreess&t=1471752067793'

        resp = urllib.urlopen(SS_URL).read()
        ss = json.loads(resp)

        hk_server={}
        sg_server={}
        hk_server['server']=ss[0]['i']
        hk_server['server_port']=ss[0]['p']
        hk_server['password']=ss[0]['pw']
        hk_server['method']=ss[0]['m']
        hk_server['status']=ss[0]['st']

        sg_server['server']=ss[1]['i']
        sg_server['server_port']=ss[1]['p']
        sg_server['password']=ss[1]['pw']
        sg_server['method']=ss[1]['m']
        sg_server['status']=ss[1]['st']

        ss_list.append(hk_server)
        ss_list.append(sg_server)

        return ss_list




    def Test_SS_speed(self,ss_list):
        result_list = []
        os.system('pkill sslocal')
        for i in range(len(ss_list)):
            server_port = "108"+str(i)
            command = "sslocal -s " + "\"" +ss_list[i]['server']+ "\""  + " -p " + "\"" +ss_list[i]['server_port'] + "\"" + " -l " + server_port +  " -k " + "\"" + ss_list[i]['password'] + "\"" + " -m " +  "\"" + ss_list[i]['method'] + "\"" + " 2>1 &"
#            print command
            os.system(command)
            time.sleep(2)
            opener = urllib2.build_opener(SocksiPyHandler(socks.SOCKS5, "127.0.0.1", int(server_port) ))
            start_time = time.time()
            try:

                if opener.open('https://www.google.com/').getcode()==200:
                    end_time = time.time()
                    speed = end_time - start_time
                else:
                    speed = 10000000
            except Exception:
                    speed = 10000000
                    pass
            ss_list[i]['speed']=speed
            result_list.append(ss_list[i])

        time.sleep(1)
        os.system("pkill sslocal")
        return result_list


    def speed(self,s):
        return s['speed']

    def Sort_ss(self,result_list):
        sort_list = sorted(result_list, key=self.speed)

        COMMAND = "/koolshare/ss/new_ssconfig.sh restart" + " \"" + sort_list[0]['server'] + "\" " + " \"" + sort_list[0]['password'] + "\" " + sort_list[0]['server_port']  + " \""+ sort_list[0]['method']  + "\""
        return COMMAND



def restart_ss(RESTART_COMMAND):
    ssh_route = paramiko.SSHClient()
    ssh_route.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_route.connect(ROUTE_HOST,ROUTE_SSH_PORT,ROUTE_USER_NAME,ROUTE_USER_PASS)
    stdin,stdout,stderr = ssh_route.exec_command(RESTART_COMMAND)
    ssh_route.close()

    print "Restart!"


def test_google():
    URL='https://www.google.com.hk/'
    try:
        h = requests.get(URL)
        if h.status_code < 400:
            return True
    except Exception :
        return False

if __name__ == '__main__':

    count = 0
    print str(time.ctime()) + "Link VPN " + str(test_google())
    for i in range(3):
        if not test_google():
            count = count + 1
            print "Connect Failed T^T %d times" %count
            if count >= 3:
                page = Free_SS().Get_Page()
                list = Free_SS().Get_list(page)
                result_list = Free_SS().Test_SS_speed(list)
                RESTART_COMMAND = Free_SS().Sort_ss(result_list)
                restart_ss(RESTART_COMMAND)
                print "Restart ! " + str(time.ctime())

                count=0

        time.sleep(12)
