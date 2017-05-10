#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 20:46:05 2017

@author: zongyiwang
"""
import matplotlib.pyplot as plt


ts = 10 # timestep in years 
wd = 4000 # water depth in meters
L = 1350 # watts/m2
albedo = 0.3
epsilon = 1
sigma = 5.67E-8 #W/(m2 K4) S-B constant

heatCapacity = wd * 4.2E6 #J/K m2
timeYears = [0]
Tk = [0.]
heatContent = heatCapacity * Tk[0]
heatIn = L*(1-albedo)/4
heatOut = 0
for time in range(0, 100):
    timeYears.append(ts + timeYears[-1])
    heatOut = epsilon * sigma * pow(Tk[-1],4)
    print("timeYears: " + str(timeYears[-1]), "heatOut(k): " + str(heatOut))
    heatContent = heatContent+(heatIn - heatOut)* ts* 3.14E7 #seconds/year
    Tk.append(heatContent/heatCapacity)
'''
dHeatContent/dt = L*(1-alpha)/4 - epsilon * sigma * T^4
T[K] = HeatContent [J/m2] / HeatCapacity [J/m2 K]
HeatContent(t+1) = HeatContent(t) + dHeatContent/dT * TimeStep
'''         
          
plt.plot( timeYears, Tk)
plt.xlabel("Time (years)")
plt.ylabel("Termperature (k)")
plt.title("Naked Planet Model",fontsize = 14,fontweight = 'bold' )
plt.show()