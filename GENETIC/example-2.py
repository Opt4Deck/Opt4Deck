# Example-2: Minimization via transformation to maximization
# min: f(x,y) = (x+2y-7)^2+(2x+y-5)^2 (Booth function)
# Converted to, max: f(x,y) = 100-(x+2y-7)^2-(2x+y-5)^2
# The constant 100 ensures that the transformed function remains positive.
#-------------------------------------------------------------------------
import math
import genetic

def fun(x,arg):
    return arg[0]-(x[0]+2.0*x[1]-7.0)**2.0-(2.0*x[0]+x[1]-5.0)**2.0

res = genetic.main(Fun=fun,Argume=[100.0,],Bound=[(-5.0,5.0),(-5.0,5.0)],Decimal=1,P_mut=0.025,Max_iter=1000)

print('-----')
print('Success: Example-2 executed successfully!')
print('Objective value:',res[0],'The minimum value of Booth function is:',res[0]-100.0)
print('Variable vector:',res[1])
