import urllib
import urllib2
import json
url = 'https://api.mianvpn.com/ajax.php?verify=true&mod=getfreess&t=1471675338943'
response = urllib.urlopen(url)
html = response.read().decode('utf-8')
ss = json.loads(html)
