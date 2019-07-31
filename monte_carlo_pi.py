# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:54:19 2017

@author: roberw
"""
import scipy as sp
import matplotlib.pylab as plt


#Area of a circle is pi*r**2
#if we know the area of a square with side = 1m is 1m^2 then the probability
#that a randomly placed dot in the square is within a circle that fits
#perfectly indise the square is pi*r^2/1. If the number of dots inside the
#circle is n and the total number of dots is N then we arrive at the equation
#n/N = pi*r^2 /1. We can then re-arrange to get
#pi = n/(N*r^2)


def dot(n):
    #random sample
    x = sp.rand() - 0.5
    y = sp.rand() - 0.5
    
    r = sp.sqrt(x*x+y*y)
    if r <= 0.5:
        n +=1
        return x, y, n
    else:
        return 0, 0, n

N = int(1e4)
n=0
x_c = []
y_c = []

for i in range(N):
    x, y, n = dot(n)
    x_c.append(x)
    y_c.append(y)

plt.plot(x_c,y_c,'o')

print('The value of pi using %d random samples is %.5f'%(N, n/(N*0.5**2)))