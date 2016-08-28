import numpy as np
import pylab as plt


def est_exp(x, x0, order):
	result = 0
	y = x - x0
	for n in range(order):
		result += np.divide(y**n,np.math.factorial(n) )
	return result*np.exp(x0)
order = 5
x0 = 53
x = np.linspace(0,65,66)
est = est_exp(x, x0, order)
fig, ax = plt.subplots() #multiple plots all on figure ax
ax.plot(x,np.exp(x)-est)
plt.axvline(x0,color='r',linestyle='--') #plot vertical line for epsilon & annotate
plt.show()

