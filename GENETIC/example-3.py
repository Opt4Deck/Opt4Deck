# Example-3: Maximization of a discontinuous function
# max: f(x,y) = 1+5(e^(-(x-2)^2-(y-2)^2))/(x^2+y^2)
# The function is undefined at (0,0), and the region around it is treated as noise.
# A small exclusion zone is introduced, assigning an arbitrary value inside it.
#-------------------------------------------------------------------------
import genetic
import math

def fun(x,arg):
    if x[0]**2.0+x[1]**2.0>0.10:
        return 1.0+5.0*(math.exp(-(x[0]-2.0)**2.0-(x[1]-2.0)**2.0))/(x[0]**2.0+x[1]**2.0)
    else:
        return 0.0001

res = genetic.main(Fun=fun,Argume=[],Bound=[(-5.0,5.0),(-5.0,5.0)],Decimal=2,P_mut=0.025,Max_iter=1500)

print('-----')
print('Success: Example-3 executed successfully!')
print('Objective value:',res[0])
print('Variable vector:',res[1])
