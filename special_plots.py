import matplotlib.pyplot as plt
import seaborn as sns
from math import pi
import  numpy as np
from numpy import sin,cos,tan
sns.set()

conv = 2*pi/360
A = 4
s = 4
h = 2
phi = 0


def plot_placa_(alpha,N,phi):
    alpha = alpha*conv
    phi = phi*conv
    plt.vlines(x=N*s, ymin=0, ymax=h, linewidth=2, color='black')
    
    x = np.linspace(-0.5*A*cos(alpha),0.5*A*cos(alpha),100)     
    y_ = tan(alpha)*x + h
    
    plt.plot(x+N*s,y_, linewidth=2, color='black')
    
    x_ = np.linspace(-100,100,100)
    
    plt.plot(x_ + N*s ,
             -tan(phi)*x_ + y_[-1] + tan(phi)*x[-1],
             linewidth=2, 
             color='orange',alpha = 0.3)
    

def plot_placa(alpha,N,phi):
    alpha = alpha*conv
    phi = phi*conv
    plt.vlines(x=A+N*s, ymin=0, ymax=h, linewidth=5, color='black')
    
    x = np.linspace(A-0.5*A*cos(alpha),A+0.5*A*cos(alpha),100)     
    y_ = tan(alpha)*x + h - A*tan(alpha)
    
    plt.plot(x+N*s,y_, linewidth=5, color='black')
    
    x_ = np.linspace(-100,100,100)
    
    plt.plot(x_ + N*s ,
             -tan(phi)*x_ + y_[-1] + tan(phi)*x[-1],
             linewidth=2, 
             color='orange',alpha = 0.3)
