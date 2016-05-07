# -*- coding: utf-8 -*-
"""
Created on Sat May 07 10:38:00 2016

@author: welion
"""
import matplotlib.pylab as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
 
def f(x,y):
    z = x + y
    z = np.array([[-2,-3,1,2,3,4],
                  [-1,-2,0.5,0,1,1.5],[-0.5,1,1,2,3,4],[-0.2,1,1,3,4,5],[0,1,2,3,2,1],[1,2,3,4,5,2]])
    z[1][1] = 9
    return z
 
n = 1
 
#均匀生成-3到3之间的n个值
x = np.arange(-3,3,n)
y = np.arange(-3,3,n)
#生成网格数据
X,Y = np.meshgrid(x,y)

fig = plt.figure()
#2行2列的子图中的第一个，第一行的第一列
subfig1 = fig.add_subplot(2,2,1)
#画等值线云图
surf1 = plt.contourf(X, Y, f(X,Y))
#添加色标
fig.colorbar(surf1)
#添加标题
plt.title('contourf+colorbar')
 
#d第二个子图，第一行的第二列
subfig2 = fig.add_subplot(2,2,2)
#画等值线
surf2 = plt.contour(X, Y, f(X,Y))
#等值线上添加标记
plt.clabel(surf2, inline=1, fontsize=10, cmap='jet')
#添加标题
plt.title('contour+clabel')
 
#第三个子图，第二行的第一列
subfig3 = fig.add_subplot(2,2,3,projection='3d')
#画三维边框
surf3 = subfig3.plot_wireframe(X, Y, f(X,Y), rstride=10, cstride=10, color = 'y')
#画等值线
plt.contour(X, Y, f(X,Y))
#设置标题
plt.title('plot_wireframe+contour')
 
#第四个子图，第二行的第二列
subfig4 = fig.add_subplot(2,2,4,projection='3d')
#画三维图
surf4 = subfig4.plot_surface(X, Y, f(X,Y), rstride=1, cstride=1, cmap='jet',
        linewidth=0, antialiased=False)
#设置色标
fig.colorbar(surf4)
#设置标题
plt.title('plot_surface+colorbar')
 
plt.show()