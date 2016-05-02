# -*- coding: utf-8 -*-
"""
Created on Mon May 02 10:25:05 2016

@author: welion
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.plot([1,2,3,4],[1,2,3,4])
plt.ylabel('some number')
plt.show()


fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

from numpy.random import randn

plt.plot(randn(50).cumsum(),'k--') 
ax1.hist(randn(100), bins=20, color='k',alpha=0.3) # 柱状图
ax2.scatter(np.arange(30),np.arange(30) + 3* randn(30)) # 散点图

#plt.savefig('figure.png') # 保存图表到文件


