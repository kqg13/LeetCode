# Graph problem 200: Number of Islands

# Given an m x n 2d grid map of '1's (land) and '0's (water),
# return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all 4 edges of the grid are all
# surrounded by water.

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.padMatrix(grid)
        self.directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        result = 0
        m, n = len(grid), len(grid[0])
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == "1":
                    result += 1
                    self.dfs(grid, i, j)
        return result

    def dfs(self, grid: List[List[str]], r: int, c: int):
        grid[r][c] = "0"  # marking as visited
        for dr, dc in self.directions:
            newRow, newCol = r + dr, c + dc
            if grid[newRow][newCol] == "1":
                self.dfs(grid, newRow, newCol)

    def padMatrix(self, grid: List[List[str]]):
        self.padCols(grid)
        self.padRows(grid)

    def padRows(self, grid):
        n = len(grid[0])
        row_to_insert = ["0"] * n
        grid.append(row_to_insert)
        grid.insert(0, row_to_insert)

    def padCols(self, grid: List[List[str]]):
        for row in grid:
            row.insert(0, "0")
            row.append("0")


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
