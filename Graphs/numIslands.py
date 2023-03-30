# Graph problem 200: Number of Islands

# Given an m x n 2d grid map of '1's (land) and '0's (water),
# return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all 4 edges of the grid are all
# surrounded by water.


class Solution:
    def numIslands(self, grid) -> int:
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.padMatrix(grid)
        result = 0
        m, n = len(grid), len(grid[0])
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == '1':
                    result += 1
                    self.dfs(grid, i, j)
        return result

    def dfs(self, grid, r, c):
        grid[r][c] = '0'
        for dr, dc in self.directions:
            newR, newC = r + dr, c + dc
            if grid[newR][newC] == '1':
                self.dfs(grid, newR, newC)

    def padMatrix(self, grid):
        newRow = self.padCols(grid)
        self.padRows(grid, newRow)

    def padCols(self, grid):
        for row in grid:
            row.insert(0, '0')
            row.append('0')
        return ['0'] * len(grid[0])

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
# print(s.numIslands(grid1))
print(s.numIslands(grid2))

