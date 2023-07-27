# 931: Minimum Path Falling Sum
# https://leetcode.com/problems/minimum-falling-path-sum/description/

class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        nRows, nCols = len(matrix), len(matrix[0])
        dp = self.padMatrix(nRows, nCols)
        # fill first row
        dp[0][1:nCols + 1] = matrix[0]

        for i in range(1, nRows):
            for j in range(1, nCols + 1):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + matrix[i][j - 1]
        lastRow = dp[-1]
        return min(lastRow)

    @staticmethod
    def padMatrix(nRows, nCols):
        dp = [[float('inf')] * (nCols + 2) for _ in range(nRows)]
        return dp


s = Solution()
m1 = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]  # Expected: 13
m2 = [[-19, 57], [-40, -5]]  # Expected: 59
print(s.minFallingPathSum(m1))
print(s.minFallingPathSum(m2))
