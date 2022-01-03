import numpy as np
import matplotlib.pyplot as plt
import math

f = np.linspace(start = 0.1, stop = 100000, num = 100)
w = 2*math.pi*f 
#print(w[10])

Rs=40.0 #ohm
Rcp=1000.0 #ohm
Rccp=1.0 #ohm
Rscp=40.0 #ohm
C=0.00001 #F
Lscp=0.001 #Hy

def Z(w):
    return np.array(Rs + 1/(1/np.complex(Rcp, -1/(w*C))+(1/Rccp))+1/np.complex(1/Rscp, -1/(w*Lscp)))

Z2=np.vectorize(Z)
#print (Z2(w))

x= np.real(Z2(w)) 
y= np.imag(Z2(w)) 

plt.style.use('seaborn-bright')

fig, ax = plt.subplots()
ax.plot(f, (x**2+y**2)**(1/2) , '-b', label='|Z| según modelo Wang-2012 modificado')
plt.legend(loc='lower right')
plt.xlabel('f(Hz)',fontsize=12)
plt.ylabel('|Z (\u03C9)|',fontsize=12)
plt.grid()
plt.show()

fig, ax = plt.subplots()
ax.plot(x, -y , '-r', label='Nyquist plot según modelo Wang-2012 modificado')
plt.legend(loc='upper right')
plt.xlabel('Z`(\u03C9)',fontsize=12)
plt.ylabel('-Z"(\u03C9)',fontsize=12)
plt.grid()
plt.show()
