#!-*- coding: utf-8 -*-
#!/usr/bin/env python

#file name: closeMeansKO.py

import matplotlib.pyplot as plt
from matplotlib.finance import quotes_historical_yahoo_ohlc
from datetime import date
from datetime import datetime
import pandas as pd

today = date.today()
start = (today.year, today.month, today.day-13)
quotes = quotes_historical_yahoo_ohlc('KO',start,today)
fields = ['date','open','close','high','low','volume']


timelist=[]
for i in range(0,len(quotes)):
    x = date.fromordinal(int(quotes[i][0]))
    y = datetime.strftime(x,'%Y%m%d')
    timelist.append(y)
quotesdf = pd.DataFrame(quotes,index=timelist,columns=fields)
quotesdf = quotesdf.drop(['date'],axis=1)
print quotesdf





