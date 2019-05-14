from math import *

dt = 0.01
g_Earth = 9.81
R_Earth = 6375*10**3 
S = 0.25*pi*3.9**2 
m = 5500 
p0 = 101325 
mu = 398600*10**9
Cx = 0.85


def count_height(h):
    T = 273
    g = g_Earth*R_Earth**2/(R_Earth+h)**2
    p = p0*exp(-g*h*0.029/(8.31*T))
    #print (p,g)
    return g,p

def count_rocket (x,y,vx,vy,a,gamma,Cy,F,t):
    dGamma, gamma, Cy = Vvod(Cy, gamma)
    time = dGamma/(5*pi/180)
    if dGamma == 0:
        time = int(input('Введите время полета: '))
    t = t + time
    print (vx,vy)
    for i in range (int(time/dt)):
        g, p = count_height(y)
        v = (vx**2+vy**2)**0.5
        Q = (Cx*S*p*(v**2))/(2*m)
        N = (Cy*S*p*(v**2))/(2*m)
        Py = N*cos(gamma)
        Pz = N*sin(gamma)
        n = (Q**2+Py**2+Pz**2)**0.5/(m*g_Earth) #в относительных единицах
        if n>=10:
            print ("Pilot is dead", n)
            F = False
            break
        a = (Q**2+Py**2+(m*g)**2)**0.5/m   
        r = (x**2+y**2)**0.5
        ax = -Q*(vx/v) + Py*(vy/v) - (mu/r**2)*x/r
        ay = -Q*(vy/v) + Py*(vx/v) - (mu/r**2)*y/r
        vx = vx + ax*dt
        vy = vy + ay*dt
        gamma = atan(vy/vx)
        x = x + vx*dt + ax*dt**2/2
        y = y + vy*dt + ay*dt**2/2
    if y<3000:
        if v<=300:
            print ('YAY!')
        else:
            print ('Pilot is dead ;C ')
        
        F = False        
    return x,y,vx,vy,a,gamma,Cy,F,t

def Printer(x,y,v,a,time):
    print('X: ', "%.3f" % x)
    print('Y: ', "%.3f" % y)
    print('V: ', "%.3f" % v)
    print('a: ', "%.3f" % a)
    print('Time: ', "%.1f" % time)

def Vvod(Cy, gamma):
    print('Введите изменение угла тангажа: ')
    dGamma = radians(float(input()))
    gamma = gamma - dGamma
    Cy = Cy*cos(gamma)
    return dGamma, gamma, Cy

F= True
GlobalTime = 0
h = 120*10**3
y = h
x = 0
vy = 0
vx = 11030#(mu/(h+R_Earth))**0.5
a = 9.81*6375**2/((6375 + h)**2)
gamma = pi/2
Cy = 0.134*Cx

while F:
    x,y,vx,vy,a,gamma,Cy,F,GlobalTime = count_rocket (x,y,vx,vy,a,gamma,Cy,F,GlobalTime)
    Printer(x,y,(vx**2+vy**2)**0.5,a,GlobalTime)

