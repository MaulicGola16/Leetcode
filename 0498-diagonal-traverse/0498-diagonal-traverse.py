class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        f = lambda d: [mat[i][d-i] for i in range(len(mat)) if 0 <= d-i < len(mat[0])]
        return [v for d in range(len(mat)+len(mat[0])-1) for v in f(d)[::(-1)**(d+1)]]
