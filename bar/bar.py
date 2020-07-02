# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('Agg') #silent mode


#------------------ FONT_setup ----------------------
font = {'family' : 'arial', 
    'color'  : 'black',
    'weight' : 'normal',
    'size' : 16.0,
    }
plt.style.use(['science','no-latex', 'scatter'])
plt.rcParams['font.sans-serif']=[font['family']]    #Arial as the default font
plt.rcParams['axes.unicode_minus']=False   #show minus sign normally 

#------------------ Data Load ----------------------
content = np.loadtxt("bar.txt",comments=['#','@'],skiprows=1)

#------------------ Figure Setup ----------------------
fig, axes = plt.subplots(1,1)
x1 = content[:,0]
y1 = content[:,1]
y2 = content[:,2]
xlocation =  np.linspace(1, len(x1) * 0.6, len(x1))
#https://blog.csdn.net/sinat_38340111/article/details/81022904?utm_source=blogxgwz3
plt.bar(xlocation, y1, alpha=0.2, width=0.15, color='red', label='undergraduate student', lw=3)
plt.bar(xlocation+0.15, y2, alpha=0.2, width=0.15, color='blue', label='graduate student', lw=3)
plt.legend(loc='best', prop=dict(family=font['family'],size=font['size']-2))

#Label setup
axes.set_xlabel('Year',fontdict=font)
axes.set_ylabel('Numbers',fontdict=font)

#Ticket setup
labels = list(map(lambda x:'%d' %x,x1))
plt.xticks(xlocation+0.075,labels, fontsize=font['size']-2,fontname=font['family'] ,rotation = 0)  #x ticks
#plt.yticks(fontsize=font['size']-2,fontname=font['family'])

#Limit setup
#axes.set_ylim((0.1, y.max()*1.1)) # set y limits manually
#axes.set_xlim((0, 1)) # set y limits manually

#Figure size
fig = plt.gcf()
fig.set_size_inches(8, 6)
plt.savefig('bar.jpg',dpi= 300)