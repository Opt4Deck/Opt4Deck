# Example-3: Maximize a linear program
# max: Z = 5.0*x1+4.0*x2
# s.t.     6.0*x1+4.0*x2 <= 24.0
#          1.0*x1+2.0*x2 <= 6.0
#          1.0*x1-1.0*x2 <= 1.0
#-------------------------------------------------------------------------
import simplex

Amat = [[5.0,4.0,0.0,0.0,0.0,0.0],
        [6.0,4.0,1.0,0.0,0.0,24.0],
        [1.0,2.0,0.0,1.0,0.0,6.0],
        [1.0,-1.0,0.0,0.0,1.0,1.0]]

res = simplex.main(Aug=Amat,Z_err=0.000000001,Max_iter=10)

print('-----')
print('Success: Example-3 executed successfully!')
print('Objective value:',res[0])
print('Variable vector:',res[1])
