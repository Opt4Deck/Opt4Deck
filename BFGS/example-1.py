# Example-1: Finding the local maximum of a mathematical function
# max: f = x*e^(-x)
# Optimization type: variable unboundaries
#-------------------------------------------------------------------------
import bfgs
import math

def fun(x,arg):
    return arg[0]+x[0]*math.exp(-x[0])

res = bfgs.main(Fun=fun,OptVal=[0.0,],Argume=[0.0,],Bound=[(False,0.0,0.90),],Conver=0.00001,Max_iter=100)

print('-----')
print('Success: Example-1 executed successfully!')
print('Objective value:',res[0])
print('Variable vector:',res[1])
