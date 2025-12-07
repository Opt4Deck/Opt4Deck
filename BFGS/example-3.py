# Example-3: Finding the local maximum of a two-variable mathematical function
# max: f = 10.0-(x-2.0)^2.0-(y-3.0)^2.0
# Optimization type: variables boundaries
#-------------------------------------------------------------------------
import bfgs

def fun(x,arg):
    return arg[0]-(x[0]-arg[1])**2.0-(x[1]-arg[2])**2.0

res = bfgs.main(Fun=fun,OptVal=[0.0,0.0],Argume=[10.0,2.0,3.0],Bound=[(False,-2.0,2.0),(True,-2.0,2.0)],Conver=0.00001,Max_iter=1000)

print('-----')
print('Success: Example-3 executed successfully!')
print('Objective value:',res[0])
print('Variable vector:',res[1])
print('Note: The optimizer may not reach the global maximum due to active boundaries.')
