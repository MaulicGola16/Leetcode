class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        maximum = 1

        for i in range(rows):
            for j in range(cols):
                max_side = min(rows - i, cols - j)

                for side in range(maximum + 1, max_side + 1):
                    ref = sum(grid[i][j:j + side])
                    is_magic_sq = True

                    for r in range(i + 1, i + side):
                        if sum(grid[r][j:j + side]) != ref:
                            is_magic_sq = False
                            break

                    if not is_magic_sq:
                        continue

                    for c in range(j, j + side):
                        if sum(grid[r][c] for r in range(i, i + side)) != ref:
                            is_magic_sq = False
                            break

                    if not is_magic_sq:
                        continue

                    if sum(grid[i + s][j + s] for s in range(side)) != ref:
                        continue

                    if sum(grid[i + s][j + side - 1 - s] for s in range(side)) != ref:
                        continue

                    maximum = side

        return maximum