# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 11:25:23 2015

@author: welion
"""


#Filename:quotes.py
#Get Dow Jones Industrial Avarage from Yahoo with quotes_historical_yahoo
#!/bin/python

from matplotlib.finance import quotes_historical_yahoo_ochl
from datetime import date
import pandas as pd

today = date.today()
start = (today.year,today.month-3,today.day)
quotes = quotes_historical_yahoo_ochl('AXP',start,today,asobject=False)
fields = ['date','open','close','high','low','volume']
timelist=[]
for i in range(0,len(quotes)):
    x = date.fromordinal(int(quotes[i][0]))
    y = datetime.strftime(x,'%Y%m%d')
    timelist.append(y)
quotesdf = pd.DataFrame(quotes,index=timelist,columns=fields)
quotesdf = quotesdf.drop(['date'],axis=1)


quotesdf.index.name='No.'

