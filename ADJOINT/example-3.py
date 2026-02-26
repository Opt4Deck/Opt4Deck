# Example-3: Identification of the (k) of a beam heat-transfer problem (finite element method)
# Governing equation: CdT/dt+KT=Q(t),
#        |1 0 0 0 0|          | 1 -1  0  0  0|            |0|
#        |0 1 0 0 0|          |-1  2 -1  0  0|            |0|
#    C = |0 0 1 0 0|ρΑdx, K = | 0 -1  2 -1  0|kA/dx and Q=|0|
#        |0 0 0 1 0|          | 0  0 -1  2 -1|            |0|
#        |0 0 0 0 1|          | 0  0  0 -1  1|            |0|
# Forward-in-time integration of the governing equation
#-------------------------------------------------------------------------
import adjoint
import math
import numpy as np

time = np.linspace(0.0,5000.0,501)
Amat = lambda OptVal: np.array([[1.0,0.0,0.0,0.0,0.0],\
                                [0.0,1.0,0.0,0.0,0.0],\
                                [0.0,0.0,1.0,0.0,0.0],\
                                [0.0,0.0,0.0,1.0,0.0],\
                                [0.0,0.0,0.0,0.0,1.0]])*900.0*2700.0*(10.0**(-4.0))*0.2
Bmat = lambda OptVal: OptVal[0]*np.array([[1.0,-1.0,0.0,0.0,0.0],\
                                          [-1.0,2.0,-1.0,0.0,0.0],\
                                          [0.0,-1.0,2.0,-1.0,0.0],\
                                          [0.0,0.0,-1.0,2.0,-1.0],\
                                          [0.0,0.0,0.0,-1.0,1.0]])*(10.0**(-4.0))/0.2
Fmat = lambda OptVal: [np.array([[0.0,],[0.0,],[0.0,],[0.0,],[0.0,]]) for t in time]

x_ini = (False,np.array([[300.0,],[293.0,],[293.0,],[293.0,],[293.0,]]))
x_aim = [(t,np.array([[294.4+4.7096*math.exp(-0.001296*t),],[294.0+0.002594*t*math.exp(-0.000886*t),],[294.4-1.6065*math.exp(-0.002340*t),],[294.4-1.5840*math.exp(-0.000787*t),],[294.4-1.6950*math.exp(-0.000605*t),]])) for t in time]

res = adjoint.main(Amat,Bmat,Fmat,x_ini,x_aim,OptVal=[300.0,],Bound=[(True,150.0,400.0),],Conver=0.000001,Max_iter=50)

print('-----')
print('Success: Example-3 executed successfully!')
print('Error:',res[0])
print('Variable vector:',res[1])
print('Note: The solution represents the best achievable approximation of the target curves, since exact identification is not possible for the given system.')
