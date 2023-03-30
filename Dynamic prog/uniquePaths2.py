# https://leetcode.com/problems/unique-paths-ii/

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        self.obstacleGrid = obstacleGrid
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        grid = [[0] * n for _ in range(m)]
        self.doFirstRowAndCol(m, n, grid)

        for i in range(1, m):
            for j in range(1, n):
                if self.obstacleGrid[i][j] == 1:
                    continue
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]

        return grid[m - 1][n - 1]

    def doFirstRowAndCol(self, m, n, grid):
        for j in range(n):
            if self.obstacleGrid[0][j] == 1:
                break
            grid[0][j] = 1

        for i in range(m):
            if self.obstacleGrid[i][0] == 1:
                break
            grid[i][0] = 1
