import numpy as np
import pylab as plt

def pfun(x,a):
    '''
    ''Computes polynomial in basis {1,x^2, x^3, ..., x^n} given coefficients 
    '' a = [a_0, a_1, ... a_n] 
    a: {array-like} of coefficients of a polynomial of degree n = len(a)-1
    x: single value for which 
    '''
    x = np.array(x)
    return [np.dot(a,np.power(x[i],range(len(a))) ) for i in range(len(x))]
    
def cond_pfun(x,a):
    '''
    computes the condition number of the polynomial
    '''
    return np.divide(
                np.multiply(np.abs(x), 
                            np.abs( np.sum( pfun(x, [n*a[n+1] for n in range(len(a) - 1)] ) ) ) ), 
                np.abs(pfun(x,a)))
'''
# a little example to make sure our polynomial-generating code works and 
# is properly vectorized
x = np.linspace(-1,1,20)
a = [0,0,0,1] # p(x) = x^3
fig, ax = plt.subplots()
ax.plot( x, pfun(x,a) )
plt.xlabel('$x$', fontsize=14)
plt.ylabel('$p(x)$', fontsize=16)
title_str = '$%.4f$'%( a[0] )
for i in range(1,len(a)):
    title_str += '$\,+\, %.4f x^{%d}$ '%( a[i], i )
plt.title('$p(x) =$ %s'%title_str, fontsize=14 )
plt.show()
'''

a = [-2030, 5741, 1, -11482, 8118]
x0 = [0.707107]
print 'Relative condition number for x = %f is '%x0[0], cond_pfun(x0,a)[0], '\n' # quite ill-conditioned
x_res = 5000
x_min = -1.0
x_max = 1.0
x = np.linspace(x_min, x_max, x_res) # let's investigate the neighborhood 
conds = cond_pfun(x,a)
fig, ax = plt.subplots()
ax.plot( x, cond_pfun(x,a) )
plt.axvline(x0[0], color='r', linestyle='--') # vertical line
plt.axvline(0, color='r', linestyle='--') # vertical line
plt.axvline(-x0[0], color='r', linestyle='--') # vertical line
ax.plot([x_min, x_max],np.array([1, 1])*np.min(conds), color='b', linestyle='--') # horizontal line

plt.xlabel('$x$',fontsize=14)
plt.ylabel('$\kappa_{p(x)}$', fontsize=16)
plt.yscale('log')
title_str = '$%d$'%( a[0] )
for i in range(1,len(a)):
    title_str += '$\,+\, %d x^{%d}$ '%( a[i], i )
plt.title('Condition Number for \n$p(x) =$ %s'%title_str, fontsize=14 )
plt.show()