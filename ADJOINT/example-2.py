# Example-2: Identification of the omega (ω1 and ω2) of a 2x2 system
# Governing equation: Adx/dt+Bx=F(t)
#    A = |1/ω1  0  |, B = |1   0| and   F(t)=|sin(ω1*t)+cos(ω1*t)|
#        | 0   1/ω2|      |0   1|            |cos(ω2*t)-sin(ω2*t)|
# Backward-in-time integration of the governing equation
#-------------------------------------------------------------------------
import math
import numpy as np
import adjoint

time = np.linspace(0.0,1.0*math.pi/2.0,101)
Amat = lambda OptVal: np.array([[1.0/OptVal[0],0.0],[0.0,1.0/OptVal[1]]])
Bmat = lambda OptVal: np.array([[1.0,0.0],[0.0,1.0]])
Fmat = lambda OptVal: [np.array([[np.sin(OptVal[0]*t)+np.cos(OptVal[0]*t),],[np.cos(OptVal[1]*t)-np.sin(OptVal[1]*t),]]) for t in time]

x_ini = (True,np.array([[0.0,],[0.0,]]))
x_aim = [(t,np.array([[np.sin(2.0*t),],[np.cos(3.0*t),]])) for t in time]

res = adjoint.main(Amat,Bmat,Fmat,x_ini,x_aim,OptVal=[1.0,1.5],Bound=[(False,0.0,5.0),(False,0.0,5.0)],Conver=0.0001,Max_iter=20)

print('-----')
print('Success: Example-2 executed successfully!')
print('Error:',res[0])
print('Variable vector:',res[1])
