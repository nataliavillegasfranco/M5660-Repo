import numpy as np
import pylab as plt

# 'stable-like' computations of e^x 
fsize = 14

def est_exp(x, order):
	c = np.log2(np.exp(1))
	y = x*c
	dy = y - np.floor(y)
	result = 0.0
	for n in range(order+1):
		result += np.divide( np.divide(dy,c)**n, np.math.factorial(n) )
	return result*np.power(2, np.floor(y))
	
order = 5
x = np.linspace(0, 10, 400)
est = est_exp(x, order)
fig, ax = plt.subplots() #multiple plots all on figure ax
ax.plot(x,np.abs(np.exp(x)-est)/np.exp(x))
plt.ylabel('\nRelative Error', fontsize=fsize)
plt.xlabel('\nValue of $x$',fontsize=fsize)
plt.show()

