# cinema.py — visualization for evolutionary optimization
# Uses: results stored in steps.txt
#-------------------------------------------------------------------------
import math
import numpy as np
import beam
#import Opt4Deck
import matplotlib.pyplot as plt
#from matplotlib.patches import Polygon
import matplotlib as mpl

# Initialization: colormap + persistent figure handles
cmap = mpl.colormaps['coolwarm']
plt.ion()
_fig, _ax1, _ax2, _his, _aim, _fai, _dot, _mas = None, None, None, [], [], None, None, None

# Graph: update a snapshot of the optimization
def graph(Forc,Leng,Widt,Smat,Mref,Mesh,Gen,y1,x2,y2):
    global _fig, _ax1, _ax2, _his, _aim, _fai, _dot, _mas
    if _fig is None:
        _fig,(_ax1,_ax2) = plt.subplots(2,1,figsize=(15.0,5.0))
        _fig.subplots_adjust(hspace=0.25)
        plt.show(block=False)
        _ax1.set_xlabel('Generation [-]')
        _ax1.set_ylabel('Mass [kg]')
        _mas = _ax1.text(0.98,0.95,'',transform=_ax1.transAxes,ha='right',va='top',fontsize=11)
        (_fai,) = _ax1.plot([],[],color='black',linestyle='dashed',linewidth=1.5)
        (_dot,) = _ax1.plot([],[],color='red',marker='o',markersize=15.0)
        sm = mpl.cm.ScalarMappable(norm=mpl.colors.Normalize(vmin=0.0,vmax=1.0),cmap=cmap)
        sm.set_array([])
        cbar = _fig.colorbar(sm,ax=_ax2,label=r'$|\sigma|/\sigma_y$')
        pos2 = _ax2.get_position()
        pos1 = _ax1.get_position()
        _ax1.set_position([pos2.x0,pos1.y0,pos2.width,pos1.height])
    _ax2.cla()
    _ax2.set_xlabel('Length [m]')
    _ax2.set_ylabel('Thickness [mm]')
    _ax2.set_xlim(-0.5,10.5)
    _ax2.set_ylim(125.0*min(y1,y2),0.0)
    _fig.suptitle('%s'%(Gen[2]),fontweight='bold')
    _ax1.grid(True)
    _ax2.grid(True)
    _his.append(Gen[1])
    _aim.append(Mref+2.0*Mref*math.log(10.0/Gen[3]-1.0))
    _fai.set_data(_his,_aim)
    _dot.set_data([_his[-1],],[_aim[-1],])
    _mas.set_text(f'Mass = {_aim[-1]:.1f} kg')
    _ax1.relim()
    _ax1.autoscale_view()
    _ax2.plot([],[],color='black',linestyle='dashed',linewidth=1.5,marker='o',markerfacecolor='red',markersize=9.0,label='Bezier-curve')
    _ax2.plot([x for x in np.linspace(0.0,10.0,51)],[-100.0*math.sqrt(6.0*Forc*(Leng-x)/(Widt*Smat)) for x in np.linspace(0.0,10.0,51)],color='green',linestyle='dashed',linewidth=1.5,label='Math approximation')
    for i in range(0,len(Mesh)):
        _ax2.fill([p[0] for p in Mesh[i][0]],[100.0*p[1] for p in Mesh[i][0]],color=Mesh[i][1])
        _ax2.plot([0.0,x2,Leng],[100.0*y1,100.0*y2,-0.5],color='black',linestyle='dashed',linewidth=1.5,marker='o',markerfacecolor='red',markersize=9.0)
    _ax2.legend(loc='lower right',frameon=False)
    _fig.canvas.draw_idle()
    if str(Gen[2])=='generation-0000':
        plt.pause(2.5)
    elif str(Gen[2])=='generation-5000':
        plt.pause(5.0)
    else:
        plt.pause(0.0005)

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
Smat = Syie/Sfac

# read data from steps.txt
with open('./steps.txt','r') as f:
    data = [i.split() for i in f]
Gen = [(int(i),int(data[i][1][-5:-1]),str(data[i][1][:-1]),float(data[i][2])) for i in range(6,len(data)) if data[i][0]=='#']

Val = 0.0
for i in range(0,len(Gen),50):
    for j in range(Gen[i][0]+1,Gen[i+1][0]):
        if float(data[j][-1])>=Val: v0,v1,v2,Val = float(data[j][0]),float(data[j][1]),float(data[j][2]),float(data[j][-1])
    # normalization (design variables -> physical parameters)
    y1 = -0.005-0.145*v0
    x2 = v1
    y2 = -0.005-0.145*v2
    Bcurve = beam.bezier([(0.0,y1),(x2,y2),(Leng,-0.005)],np.linspace(0.0,Leng,41))
    Grid = beam.grid(Bcurve)
    Cent,Area = beam.elem(Grid)
    Mass = beam.mass(Widt,Sden,Area)
    Norm = beam.stress(Forc,Leng,Widt,Syie/Sfac,Bcurve,Cent)
    # create mesh with colour of elements
    Mesh = []
    for j in range(1,len(Grid)):
        for k in range(1,len(Grid[j])):
            Mesh.append(([Grid[j-1][k-1],Grid[j-1][k],Grid[j][k],Grid[j][k-1],Grid[j-1][k-1]],cmap(abs(Norm[j-1][k-1])/Smat)))
    graph(Forc,Leng,Widt,Syie/Sfac,Mref,Mesh,Gen[i],y1,x2,y2)
