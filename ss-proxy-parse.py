import pycurl
from StringIO import StringIO
 
buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.URL, 'https://twitter.com/')
c.setopt(pycurl.PROXY,'localhost')
c.setopt(pycurl.PROXYPORT,1080)
c.setopt(pycurl.PROXYTYPE,pycurl.PROXYTYPE_SOCKS5)
 
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()
body = buffer.getvalue()

print body
