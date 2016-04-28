# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 11:14:19 2015

@author: welion
"""

#***************************************************************
# Get Dow Jones Industrial finance information from Yahoo with Re
#***************************************************************
#Filename :dji.py
 
#!/bin/python
import urllib
import re
import pandas as pd

URL='http://finance.yahoo.com/q/cp?s=%5EDJI+Components'
dStr = urllib.urlopen(URL).read()
m = re.findall('<tr><td class=\"yfnc_tabledata1\"><b><a href=\".*?\">(.*?)</a></b></td><td class=\"yfnc_tabledata1\">(.*?)</td>.*?<b>(.*?)</b>.*?</tr>',dStr)

if m:

        djidf=pd.DataFrame(data=m,columns=(u'code',u'name',u'last-trade'))
        
        print djidf
else :
        print 'Not Match'
        
