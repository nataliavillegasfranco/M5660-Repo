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
x = np.linspace(-1,1,20)
a = [0,0,0,1] # p(x) = x^3
fig, ax = plt.subplots()
ax.plot( x, pfun(x,a) )
plt.xlabel('$x$')
plt.ylabel('$p(x)$')
title_str = '$%.4f$'%( a[0] )
for i in range(1,len(a)):
    title_str += '$\,+\, %.4f x^{%d}$ '%( a[i], i )
plt.title('$p(x) =$ %s'%title_str, fontsize=14 )
plt.show()
'''

a = [-2030, 5741, 1, -11482, 8118]
x0 = [0.707107]
x = np.linspace(-1,1,100)
conds = cond_pfun(x,a)
# print 'relative condition number is ', conds[0]
fig, ax = plt.subplots()
ax.plot( x, cond_pfun(x,a) )
plt.axvline(x0[0],color='r',linestyle='--') # vertical line
plt.axvline(0,color='r',linestyle='--') # vertical line
plt.axvline(-x0[0],color='r',linestyle='--') # vertical line
plt.xlabel('$x$',fontsize=14)
plt.ylabel('$\kappa_{p(x)}$',fontsize=16)
plt.yscale('log')
title_str = '$%.4f$'%( a[0] )
for i in range(1,len(a)):
    title_str += '$\,+\, %.4f x^{%d}$ '%( a[i], i )
plt.title('Condition Number for \n$p(x) =$ %s'%title_str, fontsize=14 )
plt.show()