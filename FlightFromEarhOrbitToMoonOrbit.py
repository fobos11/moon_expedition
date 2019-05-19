# -*- coding: utf-8 -*-
"""
Created on Thu May  9 21:55:06 2019

@author: FOBOS
"""
import numpy as np
import scipy.integrate as integrate
mu=246
w=0
const1=398440000000000
alpha0=0
r0=384405
w0=0.00000265
const2=4892100640000*r0

def fun1(t,y):
    return np.array([y[1],
                     (1/(ShIZO.mass-mu*t)*ShIZO.speed_fuel*mu*np.sin((180-y[0]-ShIZO.tangag-w*t)*3.14/180))/y[2]-2*y[3]*y[1]/y[2],
                     y[3],1/(ShIZO.mass-mu*t)*ShIZO.speed_fuel*mu*np.cos((180-y[0]-ShIZO.tangag-w*t)*3.14/180)-(const1/(y[2]**2))+y[2]*(y[1]**2)])
#right part of ordinary system of diferencial equations

def fun2(t,y):
    return np.array([y[1],
                     (1/(ShIZO.mass-mu*t)*ShIZO.speed_fuel*mu*np.sin((180-y[0]-ShIZO.tangag-w*t)*3.14/180))/y[2]-2*y[3]*y[1]/(y[2])
                     +((const2*np.sin(180-y[0]+alpha0+w0*t)/(y[2]*(y[2]**2+r0**2-2*y[2]*r0*np.cos(y[0]-alpha0-w0*t)))))/y[2],
                     y[3],1/(ShIZO.mass-mu*t)*ShIZO.speed_fuel*mu*np.cos((180-y[0]-ShIZO.tangag-w*t)*3.14/180)-const1/(y[2]**2)+y[2]*(y[1]**2)
                     +(const2*np.sqrt(1-(np.sin(180-y[0]+alpha0+w0*t))**2)/(y[2]*(y[2]**2+r0**2-2*y[2]*r0*np.cos(y[0]-alpha0-w0*t))))])    
    

class rocket:
    
    def __init__(self,mass,fuel,coordinates, speeds,speed_fuel=3660,turning_speed=1,tangag=0):
        self.mass=mass
        self.fuel=fuel
        self.coordinates=coordinates
        self.speeds=speeds
        self.speed_fuel=speed_fuel
        self.turning_speed=turning_speed
        self.tangag=tangag
    def __str__(self):
        return "Status of the rocket now is:"+str(self.mass)+", "+str(self.fuel)+", "+str(self.tangag)+', '+str(self.coordinates)+", "+str(self.speeds)
    
ShIZO=rocket(163000,117700,[6560000,0],[0,0.001188])
b=integrate.RK45(fun1,0,np.array([ShIZO.coordinates[1],
                         ShIZO.speeds[1],ShIZO.coordinates[0],0]),10)

    



     