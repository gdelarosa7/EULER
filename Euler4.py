#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 21:15:56 2021

@author: dr.guillermo

Code for solving the differential equation
using Euler method
with initial conditions 
to find the aproximation to yfinal 
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')


# definimos la Ed a resolver
def dydx(x,y):
    #return y*np.sqrt(x)
    return (x-y)

# condiones iniciales
n= 5
x0=0
xf=1
y0=2

# Calculo del tamño de paso h 
h=(xf-x0)/n
#inicializamos arreglos(x,y)
x=[x0]
y=[y0]
# iteraciones 
for i in range(n):
    print(i)
    y0= y0 + h*dydx(x0,y0)
    y.append(y0)
    x0=x0+h
    x.append(x0)
    print(x0, y0)
print(x)
print(y)


plt.scatter(x,y).set_color("green")
plt.title('ED - Método de Euler')
plt.xlabel('Intervalo x')
plt.ylabel('y')
plt.grid(axis='both', color='0.95')
plt.show()
