# -*- coding: utf-8 -*-
"""
Created on Mon May 16 10:16:18 2016

@author: welion
"""

from matplotlib.finance import quotes_historical_yahoo
from pylab import *
from scipy.cluster.vq import *
from datetime import date

listDji = ['AXP','CVX','CAT','DIS','JNJ','MCD','UTX','WMT','XOM','GE','GS','JPM','MMM','NKE','PFE','TRV','V','CSCO','IBM','INTC','KO','MRK','MSFT','T','VZ','BA','DD','HD','PG','UNH']
quotes = [[0 for col in range(90)] for row in range(30)]

today = date.today()
start = (today.year,today.month-3,today.day)

for i in range(30):
        quotes[i]=quotes_historical_yahoo(listDji[i],start,today)


listTemp = [[0 for col in range(len(quotes[0]))] for row in range(30)]




print quotes

for i in range(30):
    for j in range(len(quotes[i])-1):
        if (quotes[i][j+1][2] > quotes[i][j][2]):
            listTemp[i][j] = -1
        else:
            listTemp[i][j] = 1

print listTemp
            
data = vstack(listTemp)
centroids,_=kmeans(data,4)
result,_=vq(data,centroids)

print "_____________________________________________________"
print result