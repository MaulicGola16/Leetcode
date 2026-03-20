class Solution:
    def numberOfSubmatrices(self, grid):
        n = len(grid)
        m = len(grid[0])

        sum_mat = [[0]*m for _ in range(n)]
        cntX = [[0]*m for _ in range(n)]

        res = 0

        for i in range(n):
            for j in range(m):

                val = 0
                x = 0

                if grid[i][j] == 'X':
                    val = 1
                    x = 1
                elif grid[i][j] == 'Y':
                    val = -1

                sum_mat[i][j] = val
                cntX[i][j] = x

                if i > 0:
                    sum_mat[i][j] += sum_mat[i-1][j]
                    cntX[i][j] += cntX[i-1][j]
                if j > 0:
                    sum_mat[i][j] += sum_mat[i][j-1]
                    cntX[i][j] += cntX[i][j-1]
                if i > 0 and j > 0:
                    sum_mat[i][j] -= sum_mat[i-1][j-1]
                    cntX[i][j] -= cntX[i-1][j-1]

                if sum_mat[i][j] == 0 and cntX[i][j] > 0:
                    res += 1

        return res