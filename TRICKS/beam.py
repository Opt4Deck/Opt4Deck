# beam.py — cantilever beam utilities (geometry, mesh, mass, bending stress)
# Thickness H(x) is defined by a 3-point quadratic Bezier curve
# Grid uses negative y for plotting; stresses follow Euler–Bernoulli theory
#-------------------------------------------------------------------------
import math
import numpy as np

# Bezier-curve: thickness distribution
def bezier(control,r):
    x_mat=np.array([i[0] for i in control]) ; y_mat=np.array([i[1] for i in control])
    c_mat=np.zeros([len(control),len(control)],dtype=float)
    for i in range(0,len(c_mat)):
       for j in range(0,len(c_mat[0])):
           if i<=j: c_mat[i][j]=((-1)**(j-i-2))*(math.factorial(len(control)-1)/(math.factorial(j)*math.factorial(len(control)-j-1)))*(math.factorial(j)/(math.factorial(i)*math.factorial(j-i)))
    x_100=[] ; y_100=[]
    for i in range(0,101):
        t=i/100.0 ; t_mat=np.array([t**j for j in range(0,len(control))])
        x_100.append(np.matmul(np.matmul(x_mat.transpose(),c_mat),t_mat)) ; y_100.append(np.matmul(np.matmul(y_mat.transpose(),c_mat),t_mat))
    y_bez = []
    for i in range(0,len(r)):
        found = False
        for j in range(1,len(x_100)):
            if r[i]>=x_100[j-1] and r[i]<=x_100[j]:
                if abs(x_100[j]-x_100[j-1])<1e-9: continue
                y_bez.append(y_100[j-1]+(y_100[j]-y_100[j-1])*(r[i]-x_100[j-1])/(x_100[j]-x_100[j-1]))
                found = True
                break
        if not found: y_bez.append(y_100[0] if r[i]<=x_100[0] else y_100[-1])
    return [(r[i],y_bez[i]) for i in range(0,len(r))]

# Mesh: generate a 2D grid over the beam domain
def grid(Bcurve):
    grid = []
    for x,h in Bcurve:
        H = abs(h)
        grid.append([(x,y) for y in np.linspace(0.0,-H,21)])
    return grid

# Elements: compute area and centroid of each element
def elem(grid):
    cent,area = [],[]
    for i in range(1,len(grid)):
        cent.append([])
        area.append([])
        for j in range(1,len(grid[i])):
            x1,y1 = grid[i-1][j-1][0],grid[i-1][j-1][1]
            x2,y2 = grid[i-1][j][0],  grid[i-1][j][1]
            x3,y3 = grid[i][j][0],    grid[i][j][1]
            x4,y4 = grid[i][j-1][0],  grid[i][j-1][1]
            cent[i-1].append(((x1+x2+x3+x4)/4.0,(y1+y2+y3+y4)/4.0))
            area[i-1].append(abs(x1*y2+x2*y3+x3*y4+x4*y1-y1*x2-y2*x3-y3*x4-y4*x1)/2.0)
    return cent,area

# Mass: steel mass estimation
def mass(Widt,Sden,Area):
    volume = 0.0
    for i in range(0,len(Area)):
        for j in range(0,len(Area[i])):
            volume = volume+Area[i][j]*Widt
    return Sden*volume

# Thickness: interpolated thickness at a given cross-section
def thick(x,Bcurve):
    for i in range(1,len(Bcurve)):
        if x>=Bcurve[i-1][0] and x<Bcurve[i][0]+1e-9: return Bcurve[i-1][1]+(Bcurve[i][1]-Bcurve[i-1][1])*(x-Bcurve[i-1][0])/(Bcurve[i][0]-Bcurve[i-1][0])
    return Bcurve[-1][1]

# Stress: normal bending stress evaluation
def stress(Forc,Leng,Widt,Smat,Bcurve,Cent):
    norm = []
    for i in range(0,len(Cent)):
        norm.append([])
        for j in range(0,len(Cent[i])):
            Mome = Forc*(Leng-Cent[i][j][0])
            Thic = max(abs(thick(Cent[i][j][0],Bcurve)),1e-4)
            Iner = Widt*(Thic**3.0)/12.0
            norm[i].append(Mome*(Cent[i][j][1]+Thic/2.0)/Iner)
    return norm
