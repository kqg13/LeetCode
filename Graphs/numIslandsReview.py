# Graph problem 200: Number of Islands

# Given an m x n 2d grid map of '1's (land) and '0's (water),
# return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all 4 edges of the grid are all
# surrounded by water.


class Solution:
    def numIslands(self, grid) -> int:
        self.padMatrix(grid)
        self.directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # right, left, down, up
        nIslands = 0
        m, n = len(grid), len(grid[0])
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == "1":
                    nIslands += 1
                    self.dfs(grid, i, j)
        return nIslands

    def dfs(self, grid, r, c):
        print(r, c)
        grid[r][c] = 0
        for x, y in self.directions:
            newRow, newCol = r + x, c + y
            if grid[newRow][newCol] == "1":
                self.dfs(grid, newRow, newCol)
            else:
                continue

    def padMatrix(self, grid):
        # pad cols
        newRow = self.padCols(grid)
        # pad rows
        self.padRows(grid, newRow)

    def padCols(self, grid):
        m, n = len(grid), len(grid[0])
        for m in range(m):
            grid[m].insert(0, "0")
            grid[m].append("0")
        return ["0"] * len(grid[0])

    def padRows(self, grid, newRow):
        grid.insert(0, newRow)
        grid.append(newRow)


grid1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]  # Expected output: 1

grid2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]  # Expected output: 3

s = Solution()
print(s.numIslands(grid1))
print(s.numIslands(grid2))

# correct:
# 1 1
# 1 2
# 1 3
# 1 4
# 2 4
# 2 2
# 2 1
# 3 1
# 3 2
