
#!/opt/bin/python

import json
import urllib
import os

def Get_VPN1():
    URL = 'https://api.mianvpn.com/ajax.php?verify=true&mod=getfreess&t=1471675338943'
    response = urllib.urlopen(URL)
    html = response.read().decode('utf-8')
    ss = json.loads(html)
    ip = ss[0]['i']
    method = ss[0]['m']
    passwd = ss[0]['pw']
    port = ss[0]['p']
    status = ss[0]['st']

    if not status and ss[1]['st']:
        ip = ss[1]['i']
        method = ss[1]['m']
        passwd = ss[1]['pw']
        port = ss[1]['p']
    else:
        ip = "103.207.70.48"
        passwd = "Li0nss1234"
        port = "8899"
        method = "aes-256-cfb"

    command = "/koolshare/ss/new_ssconfig.sh restart "+"\""+ip+"\" "+"\""+passwd+"\" "+port+" \""+method+"\""
    return command

if __name__=='__main__':
    print Get_VPN1()
