# Example-1: Maximization of a nonlinear mathematical function
# max: f(x) = 1-(e^(-(x^2)/5))cos(x^2)
# The function is positive and exhibits multiple local stationary points.
#-------------------------------------------------------------------------
import math
import genetic

def fun(x,arg):
    return arg[0]+math.exp(-(x[0]**2.0)/5.0)*math.cos(x[0]**2.0)

res = genetic.main(Fun=fun,Argume=[1.0,],Bound=[(-5.0,5.0),],Decimal=3,P_mut=0.025,Max_iter=500)

print('-----')
print('Success: Example-1 executed successfully!')
print('Objective value:',res[0])
print('Variable vector:',res[1])
