class secret_func:
    def __init__(self):
        import math,random
        self.root=100*random.random()
        self.calls=0

    def eval(self,x):
        import numpy as np
        import math
        if not np.isscalar(x):
            print 'Not a scalar input'
            ans=float('Nan')
            return ans
        self.calls+=1
        if self.calls > 100:
            print 'Too many accesses of function!'
            ans=float('NaN')
        else:
            ans=math.atan(50*(x-self.root))+.1*np.sin(math.pi*x)
        return ans






