# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 12:59:56 2019

@author: FOBOS
"""

import math as ms

dt=0.001

class rocket:
    
    def __init__(self,mass,fuel,coordinates, speeds,speed_fuel=3660):
        self.mass=mass
        self.fuel=fuel
        self.coordinates=coordinates
        self.speeds=speeds
        self.speed_fuel=speed_fuel
        
        
    def __str__(self):
        return "Status of the rocket now is:"+str(self.mass)+", "+str(self.fuel)+", "+str(self.coordinates)+", "+str(self.speeds)
    
class moon_orbit_rocket(rocket):
     
    def delta_eiler_method(self,alpha,mu,t):
        u0,u1=self.speeds[0],self.speeds[1]
        r,phi=self.coordinates[0],self.coordinates[1]
        m=self.mass
        mt=self.fuel
        for j in range(int(t/dt)):
            a1=(mu*self.speed_fuel)*ms.cos(alpha)/m-1.62+r*(u1**2)
            a2=((mu*self.speed_fuel)*ms.sin(alpha)/m-2*u0*u1)/r
            if ms.sqrt(a1**2+a2**2)>29.43:
                print('your pilot is dead')
                break
            du0=(a1)*dt
            du1=(a2)*dt
            dphi=u1*dt+(du1*dt)/2
            dr=u0*dt+(du0*dt)/2
            phi+=dphi
            r+=dr
            u0+=du0
            u1+=du1
            m+=-mu*dt
            mt+=-mu*dt
        return m,mt,[r,phi],[u0,u1]
#count the system's dynemic with eiler method of solving equations below(polar system of coordinates)
           
#Fr/m-g =r'' − r(ϕ')^2

#Ft/m = rϕ'' + 2 r'ϕ'            

#turning speed is infinite

Petia=moon_orbit_rocket(6200,4000,[1738000,0],[0,0])
while True:
    alpha,mu,t=map(float,input('Alpha mu t (500 0 0 to interapte)').split())
    if alpha==500:
        break
    alpha=alpha*3.14/180
    a,b,c,d=Petia.delta_eiler_method(alpha,mu,t)
    Petia.mass,Petia.fuel,Petia.coordinates,Petia.speeds=a,b,c,d
    print(Petia)
    
    


