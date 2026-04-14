from scipy.optimize import linprog
import numpy as np

class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        n = len(robot)
        m = len(factory)
    
        costs = []
        for r in robot:
            for f_pos, limit in factory:
                costs.append(abs(r - f_pos))
            
        A_eq = np.zeros((n, n * m))
        for i in range(n):
            A_eq[i, i*m : (i+1)*m] = 1
        b_eq = np.ones(n)
    
        A_ub = np.zeros((m, n * m))
        for j in range(m):
            for i in range(n):
                A_ub[j, i*m + j] = 1
        b_ub = [f[1] for f in factory]
    
        res = linprog(costs, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, method='highs')
    
        return int(round(res.fun))        