###############
# version-0.1 #
###############
1. Overview:
   This module provides a fully functional implementation of a Genetic Algorithm (GA) tailored for nonlinear optimization problems
   formulated as maximization tasks. It operates on a population of candidate solutions, applying the classical evolutionary steps
   of selection, crossover, mutation, and population update. The algorithm requires only a user-defined objective function and simple
   parameter specifications, making it suitable for engineering, scientific, and numerical applications.

2. Key-features:
    - Fully implemented Genetic Algorithm designed for nonlinear maximization problems.
    - Binary chromosome encoding with automatic determination of required bit-resolution.
    - Stochastic selection mechanism based on roulette-wheel evaluation.
    - Single-point crossover with probabilistic crossover-point selection.
    - Bit-flip mutation applied independently to each gene with user-defined mutation probability.
    - Automatic rejection of duplicate chromosomes to preserve genetic diversity.
    - Population growth and pruning rules governed by user-defined maximum population size.
    - Detailed logging of all generations (chromosomes, decoded values, fitness scores).

3. Usage:
   To execute the GA method, import the module and call the main function:
        opt,sol = genetic.main(Fun,Argume,Bound,Decimal,P_mut,Max_iter,Max_pop)
   Parameters:
    - Fun: User-defined objective function. It must accept two inputs: the variable vector (x) and the argument list (arg). ---> Fun(x,arg)
    - Argume{list[float/int/bool]}: List of additional arguments passed directly to the objective function.
    - Bound{list{tuple[float,float]}}: List of tuples defining the boundary conditions for each variable.
       Each tuple has the form:
         i) lower bound.
        ii) upper bound.
    - Decimal{int}: The numerical precision (number of decimal digits) used for binary encoding.
    - P_mut{float}: Mutation probability for each gene. Optional; default is P_mut=0.025.
    - Max_iter{int}: Maximum number of iterations/generations. Optional; default is Max_iter=1000.
    - Max_pop{int}: Maximum allowable population size. Optional; default is Max_pop=100.
    Returns:
     - opt{float}: The optimal value of the objective function.
     - sol{list[float]}: The vector of optimal values for the design (decision) variables.

4. Output:
    - steps.txt: All intermediate results of the optimization process are recorded in this file, providing a concise and
                 detailed log of the GA iterations/generations for further inspection or debugging.

5. Dependencies:
    - random
    - time
    - datetime

6. Notes:
    - The algorithm performs unconstrained maximization only.
    - Genetic operations (selection, crossover and mutation) are fully stochastic, which means results may vary between runs.
    - Due to its stochastic nature, convergence to the global optimum depends on a sufficient population size and number of generations.
    - Duplicate chromosomes are automatically rejected to preserve genetic diversity and avoid unnecessary algorithmic evaluations.
    - Variable bounds are strictly enforced.
    - The module can be imported and reused as part of larger optimization workflows.

7. Author:
   Giannis Serafeim, PhD
   Mechanical Engineering - National Technical University of Athens (NTUA)
   e-mail: opt4deck@gmail.com
