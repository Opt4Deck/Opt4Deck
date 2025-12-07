# Example-2: Finding the local minimum of a mathematical function
# min: f = (2.0-x)^2.0+(x-y)^2.0-10.0
# Optimization type: variables unboundaries
#-------------------------------------------------------------------------
import bfgs

def fun(x,arg):
    return (arg[1]-x[0])**2.0+(x[0]-x[1])**2.0-arg[0]

res = bfgs.main(Fun=fun,OptVal=[0.0,0.0],Argume=[10.0,2.0],Bound=[(False,0.0,5.0),(False,0.0,5.0)],Conver=0.00001,Max_iter=1000)

print('-----')
print('Success: Example-2 executed successfully!')
print('Objective value:',res[0])
print('Variable vector:',res[1])
