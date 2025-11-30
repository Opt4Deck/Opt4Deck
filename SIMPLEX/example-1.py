# Example-1: Maximize a linear program
# max: Z = 2.0*x1+3.0*x2
# s.t. 5.0*x1+4.0*x2 <= 32.0
#      1.0*x1+2.0*x2 <= 10.0
#-------------------------------------------------------------------------
import simplex

Amat = [[2.0,3.0,0.0,0.0, 0.0],
        [5.0,4.0,1.0,0.0,32.0],
        [1.0,2.0,0.0,1.0,10.0]]

res = simplex.main(Aug=Amat,Z_err=0.000000001,Max_iter=10)

print('-----')
print('Success: Example-1 executed successfully!')
print('Objective value:',res[0])
print('Variable vector:',res[1])
