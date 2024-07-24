# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 18:25:01 2024

@author: sudib
"""
###############################################################################
#                               KALMAN FILTER                                              
###############################################################################

import matplotlib.pyplot as plt
#import control as ct
import numpy as np

def plottingfunction(xaxisvector,yaxisvector,titlestring,xaxisstring,yaxisstring,filesavingname):
    plt.figure(figsize=(8,6))
    plt.plot(xaxisvector,yaxisvector,color='green',linewidth=3)
    plt.title(titlestring,fontsize=14)
    plt.xlabel(xaxisstring,fontsize=14)
    plt.ylabel(yaxisstring,fontsize=14)
    plt.tick_params(axis='both',which='major', labelsize=14)
    plt.grid(visible=True)
    plt.savefig(filesavingname,dpi=800)
    plt.show()

###Introducing Noise
###Formatting Kalman Filter to filter out this noise exrensively

actual_range=10
num_measurement=100
measured_range=np.random.normal(actual_range,0.5,num_measurement)
plt.plot(measured_range,'o-')
    
R=0.1 #measurement convariance
C=0.01 #process convariance

x=np.zeros(num_measurement) #measuremnt of range
p=np.zeros(num_measurement) #measurement of error
x_minus=np.zeros(num_measurement) #measurement of range in the just prev instance 
p_minus=np.zeros(num_measurement) #measurement of error in the just prev instance
k_gain=np.zeros(num_measurement) #kalman filter gain

x[0]=0
p[0]=1


for i in range(1,num_measurement):
    x_minus[i]=x[i-1]
    p_minus[i]=p[i-1]
    k_gain[i]=p_minus[i]/(p_minus[i]+R)
    x[i]=x_minus[i]+k_gain[i]*(measured_range[i]-x_minus[i])
    p[i]=(1-k_gain[i]*p_minus[i])
    plt.plot(x)
    plt.plot(measured_range)
    plt.axis([0,100,8,11])
    plt.savefig('KALMAN FILTER OUTPUT',dpi=800)



    