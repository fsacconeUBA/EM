import numpy as np
import matplotlib.pyplot as plt
import math

f = np.linspace(start = 1, stop = 100000, num = 10000)
w = 2*math.pi*f 


R=50.0 #ohm
G=0.02 #mho
C=0.00001 #F
L=0.001 #Hy
Rc=100 #ohm

def Z0(w):
    return (np.array(np.complex(R, w*L)/np.complex(G, w*C)))**(1/2)

Z2=np.vectorize(Z0)
print((Rc-Z2(15))/(Rc+Z2(15)))

x1= np.real(Z2(w)) 
y1= np.imag(Z2(w)) 

def g(w):
	return (np.array((Rc-Z2(w))/(Rc+Z2(w))))

rho=np.vectorize(g)
print (rho(15))

x2= np.real(rho(w)) 
y2= np.imag(rho(w))

plt.style.use('seaborn-bright')

fig, ax = plt.subplots()
ax.plot(x1, -y1 , '-r', label='TL')
plt.legend(loc='upper right')
plt.xlabel('Z0`(\u03C9)',fontsize=12)
plt.ylabel('-Z0"(\u03C9)',fontsize=12)
plt.grid()
plt.show()

fig, ax = plt.subplots()
ax.plot(f, (x2**2+y2**2)**(1/2) , '-g', label='|\u03C1| ')
plt.legend(loc='lower right')
plt.xlabel('f(Hz)',fontsize=12)
plt.ylabel('|\u03C1 (\u03C9)|',fontsize=12)
plt.grid()
plt.show()
