# 969: Max Increase to Keep City Skyline
# https://leetcode.com/problems/max-increase-to-keep-city-skyline/

import numpy as np


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        np_grid = np.array(grid)
        maxRows = self.getMaxOfRows(np_grid)
        maxCols = self.getMaxOfCols(np_grid)
        n, result = len(grid), 0
        for r in range(n):
            for c in range(n):
                maxHeight = min(maxRows[r], maxCols[c])
                result += maxHeight - grid[r][c]
        return result

    def getMaxOfRows(self, grid):
        maxRows = np.amax(grid, axis=1)
        return maxRows.tolist()

    def getMaxOfCols(self, grid):
        maxCols = np.amax(grid, axis=0)
        return maxCols.tolist()
