# -*- coding: utf-8 -*-
"""
Created on Thu Jun 02 20:50:28 2016

@author: welion
"""

#!/bin/python env

import paramiko
import smtplib
from email.mime.text import MIMEText


MAIL_HOST = "smtp.sina.com"
SUBJECT = "Route_infomation_new"
MAIL_FROM = "auto_pop_mail@sina.com"
MAIL_TO = "zhongwanhua001@qq.com"

ROUTE_HOST = "192.168.1.1"
ROUTE_SSH_PORT = 22222
ROUTE_USER_NAME = "admin"
ROUTE_USER_PASS = "!QAZ2wsx"
ROUTE_COMMAND = "ifconfig ppp0"

def Exec_command():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ROUTE_HOST,ROUTE_SSH_PORT,ROUTE_USER_NAME,ROUTE_USER_PASS)

    stdin,stdout,stderr = ssh.exec_command(ROUTE_COMMAND)
    line = stdout.readlines()
    ssh.close()
    return line


def Send_Mail(ip_info):
    msg = MIMEText(ip_info,"html","utf-8")
    msg['Subject'] = SUBJECT
    msg['From'] = MAIL_FROM
    msg['To'] = MAIL_TO

    try:
        server = smtplib.SMTP()
        server.connect(MAIL_HOST,"25")
        server.starttls()
        server.login("auto_pop_mail@sina.com","zwh123")
        server.sendmail(MAIL_FROM,[MAIL_TO],msg.as_string())
        server.quit()
        print "Send mail successfully!"
    except Exception,e:
        print "Send mail FAIL: "+str(e)

if __name__ == '__main__':
    ip_info = Exec_command()[1]
    Send_Mail(ip_info)