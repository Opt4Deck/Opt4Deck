# Example-2: Minimize a linear program (converted to maximization)
# min: Z = 1.0*x1-3.0*x2 => max: z = -1.0*x1+3.0*x2
# s.t. 1.0*x1+1.0*x2 <= 6.0
#      2.0*x1+1.0*x2 <= 8.0
#-------------------------------------------------------------------------
import simplex

Amat = [[-1.0,3.0,0.0,0.0,0.0],
        [1.0,1.0,1.0,0.0,6.0],
        [2.0,1.0,0.0,1.0,8.0]]

res = simplex.main(Aug=Amat,Z_err=0.000000001,Max_iter=10)

print('-----')
print('Success: Example-2 executed successfully!')
print('Objective value:',-res[0],'# Reported as a minimization result!')
print('Variable vector:',res[1])
