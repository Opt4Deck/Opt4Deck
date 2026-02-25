###############
# version-0.1 #
###############
1. Overview:
   This Python module implements the Simplex algorithm for solving linear programming problems (LPP) involving the maximization of
   a linear objective function subject to linear inequality constraints. It is intended for students, researchers, and professional
   engineers working on optimization tasks in operations research, production planning, or engineering design.

2. Key-features:
    - Supports maximization problems with inequality constraints of the ≤ type.
    - Generates step-by-step tabular output of the Simplex procedure.
    - Fully implemented in pure Python, with no external dependencies.
    - Lightweight and easy to integrate into other optimization workflows.

3. Usage:
   To execute the Simplex method, import the module and call the main function:
        opt,sol = simplex.main(Aug,Z_err,Max_iter)
   Parameters:
    - Aug{list[list[float]]}: The augmented matrix containing the coefficients of the objective function and the system constraints.
    - Z_err{float}: A small tolerance value used for zero comparisons. Optional; default is Z_err=0.00001.
    - Max_iter{int}: The maximum number of iterations. Optional; default is Max_iter=100
   Returns:
    - opt{float}: The optimal value of the objective function.
    - sol{list[float]}: The vector of optimal values for the design (decision) variables.

4. Output:
    - steps.txt: All intermediate results of the optimization process are recorded in this file, providing a concise and
                 detailed log of the Simplex iterations for further inspection or debugging.

5. Dependencies:
    - datetime

6. Notes:
    - This version supports maximization problems only.
    - All constraint inequalities must be of the ≤ type.
    - Future versions will include support for minimization and artificial variables (two-phase method).

7. Author:
   Giannis Serafeim, PhD
   Mechanical Engineering - National Technical University of Athens (NTUA)
   e-mail: opt4deck@gmail.com
