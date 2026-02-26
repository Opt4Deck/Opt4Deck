# Example-1: Identification of the capacitance (C) of an RC electrical circuit
# Governing equation: RCdv/dt+v=Vs(t), R = 5Ω and Vs(t) = 5V
# Forward-in-time integration of the governing equation
#-------------------------------------------------------------------------
import adjoint
import math
import numpy as np

time = np.linspace(0.0,0.8,101)
Amat = lambda OptVal: np.array([[5.0*(10.0**(-2.0))*OptVal[0],],])
Bmat = lambda OptVal: np.array([[1.0,],])
Fmat = lambda OptVal: [np.array([[5.0,],]) for t in time]

x_ini = (False,np.array([[0.0,],]))
x_aim = [(t,np.array([[5.0*(1.0-math.exp(-8.0*t)),],])) for t in time]

res = adjoint.main(Amat,Bmat,Fmat,x_ini,x_aim,OptVal=[1.5,],Bound=[(True,0.0,5.0),],Conver=0.0001,Max_iter=20)

print('-----')
print('Success: Example-1 executed successfully!')
print('Error:',res[0])
print('Variable vector:',res[1])
