# optimize.py — GA optimization for Bezier thickness under stress constraint (penalty method)
# Uses: beam.py (analysis) + genetic.py (optimizer)
#-------------------------------------------------------------------------
import math
import numpy as np
import beam
import genetic

# Objective: fitness function to maximize
def fun(val,arg):
    Forc,Leng,Widt,Sden,Smat,Mref = arg
    # normalization (design variables -> physical parameters)
    y1 = -0.005-0.145*val[0]
    x2 = val[1]
    y2 = -0.005-0.145*val[2]
    Bcurve = beam.bezier([(0.0,y1),(x2,y2),(Leng,-0.005)],np.linspace(0.0,Leng,41))
    Grid = beam.grid(Bcurve)
    Cent,Area = beam.elem(Grid)
    Mass = beam.mass(Widt,Sden,Area)
    Norm = beam.stress(Forc,Leng,Widt,Smat,Bcurve,Cent)
    viol = max(0.0,max([abs(float(Norm[i][j])) for i in range(0,len(Norm)) for j in range(0,len(Norm[i]))])/Smat-1.0)
    Cpen = 0.5+0.5*math.exp(-viol)
    return 10.0*Cpen/(1.0+math.exp(0.5*(Mass-Mref)/Mref))

#----------#
#   MAIN   #
#----------#
Forc = 5000.0
Leng = 10.0
Widt = 0.10
Sden = 7850.0
Syie = 355*(10.0**6.0)
Sfac = 1.5
Mref = 583.75
# Optimization: call process through Genetic Algorithm
opt,sol = genetic.main(Fun=fun,Argume=(Forc,Leng,Widt,Sden,Syie/Sfac,Mref),Bound=[(0.0,10.0),(0.0,10.0),(0.0,10.0)],Decimal=2,P_mut=0.025,Max_iter=5002,Max_pop=100)
# Results: print the control points of Bezier-curve
print('-----')
print('Successful evaluation of Bezier control points (CPs):')
print(' -cp1: (%.3f,%.3f)'%(0.0,-0.005-0.145*sol[0]))
print(' -cp2: (%.3f,%.3f)'%(sol[1],-0.005-0.145*sol[2]))
print(' -cp3: (%.3f,%.3f)'%(Leng,-0.005))
