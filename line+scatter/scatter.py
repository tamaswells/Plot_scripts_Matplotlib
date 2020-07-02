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
plt.style.use(['science','no-latex'])
plt.rcParams['font.sans-serif']=[font['family']]    #Arial as the default font
plt.rcParams['axes.unicode_minus']=False   #show minus sign normally 

#------------------ Data Load ----------------------
content = np.loadtxt("scatter.dat",comments=['#','@'])

#------------------ Figure Setup ----------------------
fig, axes = plt.subplots(1,1)
labels = ['y=x','y=x^1.1','y=log(x)']
x = content[:,0] 
for i in range(1,content.shape[1]):
    axes.plot(x, content[:,i],label=labels[i-1],lw=2)
    axes.scatter(x, content[:,i], s=20)

#Legend
plt.legend(loc='best', prop=dict(family=font['family'],size=font['size']-2),markerscale=3.0)

#Label setup
axes.set_xlabel('x',fontdict=font)
axes.set_ylabel('y',fontdict=font,rotation=0)

#Ticket setup
plt.xticks(fontsize=font['size']-2,fontname=font['family'])
plt.yticks(fontsize=font['size']-2,fontname=font['family'])
#axes.set_xticklabels(group_labels, rotation=0,fontsize=font['size']-2,fontname=font['family'])

#Limit setup
axes.set_xlim((x.min(), x.max())) # set x limits manually

#Figure size
fig = plt.gcf()
fig.set_size_inches(8, 6)
plt.savefig('scatter.jpg',dpi= 300)
