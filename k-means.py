# -*- coding: utf-8 -*-
"""
Created on Mon May 16 09:34:40 2016

to show how to use k-means function

@author: welion
"""

from pylab import *
from scipy.cluster.vq import *

list1 = [88,74,96,85]
list2 = [92,99,95,94]
list3 = [91,87,99,95]
list4 = [78,99,97,81]
list5 = [88,78,98,84]
list6 = [100,98,100,92]

data = vstack((list1,list2,list3,list4,list5,list6))
centroids,_=kmeans(data,2) #n=2 分成2类
#print "centroids is :  %s" %centroids #聚类中心
result,_=vq(data,centroids) 
print result

