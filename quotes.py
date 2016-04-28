# -*- coding: utf-8 -*-
"""
Created on Wed Dec 02 11:25:23 2015

@author: welion
"""


#Filename:quotes.py
#Get Dow Jones Industrial Avarage from Yahoo with quotes_historical_yahoo
#!/bin/python

from matplotlib.finance import quotes_historical_yahoo
from datetime import date
import pandas as pd

today = date.today()
start = (today.year-1,today.month,today.day)
quotes = quotes_historical_yahoo('AXP',start,today,asobject=False)
quotesdf = pd.DataFrame(data=quotes,columns=(u'time',u'open',u'close',u'high',u'low',u'volume'))
print quotesdf

quotesdf.index.name='No.'

