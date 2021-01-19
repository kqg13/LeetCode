# LeetCode 1219: Path with Maximum Gold

# In a gold mine grid of size m * n, each cell in this mine has an int representing
# the amount of gold in that cell, 0 if it is empty. Return the max amount of gold
# you can collect under the conditions:

# 1- Every time you are located in a cell you will collect all the gold in that cell.
# 2- From your position you can walk one step to the left, right, up or down.
# 3- You can't visit the same cell more than once.
# 4- Never visit a cell with 0 gold.
# 5- You can start and stop collecting gold from any position in the grid that has some gold.

# Examples:
# grid1 = [[0, 6, 0], [5, 8, 7], [0, 9, 0]]
# Path to get the max gold is 9 -> 8 -> 7
# grid2 = [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]] ---> 28


# Running time: O(3^n), Space: O(m * n)
class Solution:
    def getMaximumGold(self, grid) -> int:
        self.padMatrix(grid)
        paddedRows, paddedCols = len(grid), len(grid[0])
        self.visited = self.createVisited(paddedRows, paddedCols)
        self.best, self.directions = 0, [(-1, 0), (1, 0), (0, 1), (0, -1)]
        for i in range(paddedRows):
            for j in range(paddedCols):
                self.dfs(grid, 0, i, j)
        return self.best

    def dfs(self, grid, currentValue, r, c):
        if self.visited[r][c]:
            return
        if grid[r][c] == 0:
            return
        # Make updates
        self.visited[r][c] = True
        currentValue += grid[r][c]
        for dr, dc in self.directions:
            newRow, newCol = r + dr, c + dc
            self.dfs(grid, currentValue, newRow, newCol)
        self.best = max(self.best, currentValue)
        self.visited[r][c] = False

    def createVisited(self, nRows, nCols):
        visited = [[False] * nCols for _ in range(nRows)]
        return visited

    def padMatrix(self, grid):
        self.padCols(grid)
        self.padRows(grid)

    def padRows(self, grid):
        nCols = len(grid[0])
        newRow = [0] * nCols
        grid.insert(0, newRow)
        grid.append(newRow)

    def padCols(self, grid):
        for row in grid:
            row.insert(0, 0)
            row.append(0)


s = Solution()

grid1 = [[0, 6, 0],
         [5, 8, 7],
         [0, 9, 0]]

grid2 = [[1, 0, 7],
         [2, 0, 6],
         [3, 4, 5],
         [0, 3, 0],
         [9, 0, 20]]


grid3 = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

print(s.getMaximumGold(grid3))
