# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 09:36:50 2015

@author: welion
"""

import os
import urllib2
import numpy as np
import scipy as sp

import tornado.httpclient

def fetch(url):
	http_header = {'User-Agent':'Mozilla/5.0 (Linux; U; Android 5.1.1; zh-cn; Lenovo P1c72 Build/LMY47V) AppleWebKit/533.1 (KHTML, like Gecko)Version/4.0 MQQBrowser/5.4 TBS/025478 Mobile Safari/533.1'}
	http_request = tornado.httpclient.HTTPRequest(url=url, method='GET', headers=http_header, connect_timeout=120, request_timeout=600)
	
	http_client = tornado.httpclient.HTTPClient()
	
	http_response = http_client.fetch(http_request)
	print http_response.code
	
	for field in http_response.headers.get_all():
		print field
	
	return http_response.body
 
from  matplotlib.finance import quotes_historical_yahoo
from datetime import date
import pandas as pd

today = date.today()
start=(today.year-1,today.month,today.day)
quote = quotes_historical_yahoo('AXP',start,today)
df=pd.DataFrame(quote)
print df

import  matplotlib as mp 
import pylab

sp = quotes_historical_yahoo('^GSPC', start, today,
                                asobject=True, adjusted=True)
returns = (sp.open[1:] - sp.open[:-1])/sp.open[1:]
[n,bins,patches] = pylab.hist(returns, 100)
mu = np.mean(returns)
sigma = np.std(returns)
x = sp.normpdf(bins, mu, sigma)
plot(bins, x, color='red', lw=2)
