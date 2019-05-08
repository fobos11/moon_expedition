import math as m

heightOrbit=0

density=4.8*m.exp(-0.000117*heightOrbit)

massRocket=2766700

rocketAngle=0

angleTime=0

angle=0

Vx=465.1
Vy=0 

def newPosition(delta_ti,massRocket,rocketAngle,angleTime,Vx,Vy,heightOrbit,angle):
    
    density=4.8*m.exp(-0.000117*heightOrbit)
    massRocket=massRocket-13314*delta_ti
    
    if angleTime!=0:
        rocketAngle=rocketAngle+(3.141/180)*delta_ti
        angleTime=angleTime-delta_ti
    
    beta=-(massRocket*(9.81-Vx)/delta_ti-34350000*m.cos(rocketAngle))/(massRocket*Vx/delta_ti+34350000*m.sin(rocketAngle))
    
    Vx=((-massRocket/delta_ti)+m.sqrt((massRocket/delta_ti)*(massRocket/delta_ti)+4*density*m.sqrt(beta*beta+1)*(Vx*massRocket/delta_ti+34350000*m.sin(rocketAngle))))/(2*density*m.sqrt(beta*beta+1))
    
    Vy=beta*Vx
    
    heightOrbit=heightOrbit+delta_ti*Vy
    
    angle=angle+delta_ti*Vx/6375000
    
    return Vx,Vy,heightOrbit,angle,massRocket,rocketAngle,angleTime

angleTime=75
rocketAngle=0
for i in range(120):
    Vx,Vy,heightOrbit,angle,massRocket,rocketAngle,angleTime=newPosition(1,massRocket,rocketAngle,angleTime,Vx,Vy,heightOrbit,angle)
    print("Vx={0}, Vy={1}, heightOrbite={2}, angle={3} massRocket={4}, rocketAngle={5}".format (Vx,Vy,heightOrbit,angle,massRocket,rocketAngle))


