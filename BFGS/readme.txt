###############
# version-0.1 #
###############
1. Overview:
   This module implements a numerical optimization algorithm based on the Broyden–Fletcher–Goldfarb–Shanno (BFGS) quasi-Newton method.
   It is designed for the optimization (minimization or maximization) of a user-defined objective function, with or without variable
   bounds. The algorithm is applicable to non-linear problems and, depending on the function landscape and the chosen initial values,
   it may converge to a local stationary point — that is, a local minimum, maximum, or saddle point.

2. Key-features:
    - Implementation of the BFGS quasi-Newton method.
    - Supports optimization with or without variable bounds.
    - Numerical estimation of the gradient (first derivatives) via finite differences.
    - Iterative Hessian approximation updated through the BFGS update formula.
    - Simple function interface with minimal dependencies.
    - Detailed logging of intermediate steps and gradient updates.

3. Usage:
   To execute the BFGS method, import the module and call the main function:
        opt,sol = bfgs.main(Fun,OptVal,Argume,Bound,Conver,Max_iter)
   Parameters:
    - Fun: User-defined objective function. It must accept two inputs: the variable vector (x) and the argument list (arg). ---> Fun(x,arg)
    - OptVal{list[float]}: List containing the initial values of the design variables.
    - Argume{list[float/int/bool]}: List of additional arguments passed directly to the objective function.
    - Bound{list{tuple[bool,float,float]}}: List of tuples defining the boundary conditions for each variable.
       Each tuple has the form:
          i) True or False ---> to enforce or ignore the bounds.
         ii) lower bound.
        iii) upper bound.
    - Conver{float}: Convergence tolerance. Optional; default is Conver=0.001.
    - Max_iter{int}: Maximum number of iterations. Optional; default is Max_iter=100.
   Returns:
    - opt{float}: The optimal value of the objective function.
    - sol{list[float]}: The vector of optimal values for the design (decision) variables.

4. Output:
    - steps.txt: All intermediate results of the optimization process are recorded in this file, providing a concise and
                 detailed log of the BFGS iterations for further inspection or debugging.

5. Dependencies:
    - math
    - numpy
    - datetime

6. Notes:
    - The algorithm may converge to a local rather than global optimum.
    - Proper scaling of input variables and a well-chosen initial guess can significantly improve convergence behavior.
    - Boundary handling is applied through reflection when a variable exceeds its allowed range (only when bounds are enforced [True]).
    - Gradients and the main diagonal of the Hessian at the first iteration are evaluated numerically via finite differences.
    - No line-search procedure is implemented; each iteration proceeds with a fixed unit step.
    - The module can be imported and reused in other optimization frameworks.

7. Author:
   Giannis Serafeim, PhD
   Mechanical Engineering - National Technical University of Athens (NTUA)
   e-mail: opt4deck@gmail.com
