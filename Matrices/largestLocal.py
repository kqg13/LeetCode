# 2373: Largest Local Values in a Matrix
# https://leetcode.com/problems/largest-local-values-in-a-matrix/

class Solution:
    def largestLocal(self, grid):
        """
        grid: List[List[int]]
        return: List[List[int]]
        """
        self.grid = grid
        grid_len = len(grid)
        output_len = grid_len - 2

        output = [[0]*output_len for _ in range(output_len)]

        for i in range(output_len):
            for j in range(output_len):
                output[i][j] = self.getLocalMax(i, j)
        print(output)
        return output

    def getLocalMax(self, init_r, init_c):
        max_ele = 0
        for r in range(init_r, init_r + 3):
            for c in range(init_c, init_c + 3):
                current_ele = self.grid[r][c]
                max_ele = max(current_ele, max_ele)
        return max_ele


s = Solution()
grid1 = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
grid2 = [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 2, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]
