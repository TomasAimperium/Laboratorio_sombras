
import numpy as np
from numpy import sin,cos,tan
from math import pi

conv = 2*pi/360
A = 4
s = 6
h = 2
phi = 0

def ratio(bet,alp,psi):
    bet,alp,psi = conv*bet,conv*alp,conv*psi
    #base de la placa
    xb = -0.5*A*cos(bet) + s
    yb = -0.5*A*sin(bet) + h
    B = [xb,yb]
    
    #limite de la sombra
    xp = (0.5*A*(sin(alp) + cos(alp)*tan(psi)) + s*tan(bet))/(tan(bet) + tan(psi))
    yp = tan(bet)*(xp - s) + h
    P = [xp ,yp]
    
    d = np.sqrt((P[0] - B[0])**2 + (P[1] - B[1])**2)
    
    # if (P[0] >= B[0]) and (d < A):
    S = 1 - d/A
    # elif (P[0] >= B[0]) and (d >= A):
    #     S = 0
    # elif (P[0] < B[0]):    
    #     S = 1
    return S

def potencia0(alp,psi):
    P = A*sin(pi - conv*psi  - conv*alp)
    return P

def potencia(alp1,alp0,psi):
    P = A*ratio(alp1,alp0,psi)*sin(pi - conv*psi  - conv*alp1)
    return P


def potencia_iterativa(bet,psi):
    # bet,psi = conv*np.array(bet),conv*psi
    P = []
    S = [1]
    P.append(A*sin(pi - conv*psi - conv*bet[0]))
    for i in range(len(bet)-1):
        P.append(A*ratio(bet[i+1],bet[i],psi)*sin(pi - conv*psi - conv*bet[i+1]))
        S.append(ratio(bet[i+1],bet[i],psi))
    return P