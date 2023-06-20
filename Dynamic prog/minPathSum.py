# 64: Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid) -> int:
        """
        grid: List[List[int]]
        return: int
        """
        self.matrix = grid.copy()
        nRows, nCols = len(self.matrix), len(self.matrix[0])
        self.setFirstRowAndCol(grid, nRows, nCols)
        for i in range(1, nRows):
            for j in range(1, nCols):
                best = min(grid[i-1][j], grid[i][j-1])
                self.matrix[i][j] = grid[i][j] + best
        bottomRight = self.matrix[nRows-1][nCols-1]
        return bottomRight

    def setFirstRowAndCol(self, grid, nRows, nCols):
        # Set first row
        for col in range(1, nCols):
            self.matrix[0][col] = grid[0][col] + grid[0][col-1]
        # Set first col
        for row in range(1, nRows):
            self.matrix[row][0] = grid[row][0] + grid[row-1][0]


s = Solution()
grid1 = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]  # Expected: 7
grid2 = [[1, 2, 3], [4, 5, 6]]  # Expected: 12
s.minPathSum(grid1)
s.minPathSum(grid2)
