###############
# version-0.1 #
###############
1. Overview:
   This module implements an optimization algorithm based on the Adjoint Method, specifically designed for fitting dynamic systems to
   a prescribed aim-distribution. The methodology applies to systems governed by first-order linear differential equations and enables
   efficient evaluation of the sensitivity of the mismatch with respect to the design variables. By solving one forward and one adjoint
   system, the module computes the adjustment field with computational cost independent of the dimensionality of the parameter space. It
   supports variable bounds, automated management of the forward–adjoint optimization loop, and generation of the required distributions,
   providing a robust computational tool for engineering and computational physics applications where accurate matching to a aim state
   is required.

2. Key-features:
    - Implementation of the Adjoint Method for aim-distribution adjustment in first-order linear ODE systems: A(u)*dx/dt+B(u)*x=F(t;u)
    - Numerical solution of forward–adjoint equations with direct construction of the adjustment field.
    - Support for variable bounds with optional enforcement.
    - Gradient evaluation via the adjoint equation, with cost independent of parameter dimensionality.
    - Structured input interface for supplying A(u),B(u),F(t;u), and aim-distributions.
    - Automated optimization loop management with detailed step logging.
    - Tailored for adjustment problems rather than generic extremum search.

3. Usage:
   To execute the Adjoint Method, import the module and call the main function:
        err,sol = adjoint.main(Amat,Bmat,Fmat,x_ini,x_aim,OptVal,Bound,Conver,Max_iter)
   Parameters:
    - Amat: Function returns the inertia matrix A(u) of the design variables. ---> Amat = lambda OptVal: np.array([[1.0,-1.0],[-1.0,1.0,]])
    - Bmat: Function returns the damping matrix B(u) of the design variables. ---> Bmat = lambda OptVal: np.array([[1.0,0.0],[0.0,1.0]])
    - Fmat: Function returns a list of time-dependent forcing distribution. ---> Fmat = lambda OptVal: [np.array([[t,],[t**2.0,],]) for t in time]
    - x_ini{tuple[bool,array[float]]}: Specifies the initial or terminal condition for the state equation. ---> x_ini = (False,np.array([[0.0,],[0.0,]]))
       The boolean flag determines the time location of the prescribed condition:
          i) False: initial condition at t = 0 (forward-in-time integration)
         ii) True: terminal condition at t = τ (backward-in-time integration)
    - x_aim{list[tuple[float,array[float]]]}: Aim-distribution at discrete time points. ---> x_aim = [(0.0,np.array([[0.0,],[0.0,]])),(0.1,np.array([[0.5],[1.0,]]))...]
    - OptVal{list[float]}: List containing the initial values of the design variables.
    - Bound{list[tuple[bool,float,float]]}: List of tuples defining the boundary conditions for each variable.
       Each tuple has the form:
          i) True or False ---> to enforce or ignore the bounds.
         ii) lower bound.
        iii) upper bound.
    - Conver{float}: Convergence tolerance. Optional; default is Conver=0.001.
    - Max_iter{int}: Maximum number of iterations. Optional; default is Max_iter=100.
   Returns:
    - err{float}: The final mismatch between the aim-distribution and the computed response.
    - sol{list[float]}: The vector of optimal values for the design (decision) variables.

4. Output:
    - steps.txt: All intermediate results of the optimization process are recorded in this file, providing a concise and
                 detailed log of the Adjoint-based iterations for further inspection or debugging.
    - distr.txt: The time-series of the computed (fitted) distributions and the corresponding aim-distributions are recorded,
                 allowing direct comparison between the system response and the target evolution.

5. Dependencies:
    - math
    - numpy
    - datetime

6. Notes:
    - The Adjoint Method addresses adjustment (state-matching) problems rather than generic extremum search.
    - Forward and adjoint equations must be defined consistently with respect to time discretization and boundary conditions.
    - Solution quality depends on the problem formulation, the initial conditions, and the ability to approximate the aim-distribution.
    - Convergence is influenced by the choice of initial values and by the enforcement of variable bounds.
    - The err variable is a key performance indicator, quantifying the mismatch with the aim-distribution.
    - All intermediate steps are automatically logged for reproducibility and diagnostic purposes.
    - The module can be integrated into larger optimization frameworks without reliance on external numerical libraries.

7. Author:
   Giannis Serafeim, PhD
   Mechanical Engineering - National Technical University of Athens (NTUA)
   e-mail: opt4deck@gmail.com 
