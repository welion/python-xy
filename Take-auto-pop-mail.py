# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 12:41:51 2016

@author: welion
"""


import os
import poplib
import email
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr


POP_SERVER = "pop.sina.com"
USERNAME = "auto_pop_mail@sina.com"
PASSWD = "zwh123"



server = poplib.POP3(host=POP_SERVER)
print(server.getwelcome())
server.user(USERNAME)
server.pass_(PASSWD)
resp, mails, octets = server.list()
print(mails)
index = len(mails)
resp, lines, octets = server.retr(index)
msg_content = '\r\n'.join(lines)
msg = Parser().parsestr(msg_content)
#server.quit()



                                                     