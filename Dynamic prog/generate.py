# 118: Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows):
        # Init matrix with 1s so you have first and last element filled
        dp = [[1] * i for i in range(1, numRows + 1)]

        if numRows > 2:
            for i in range(2, numRows):
                prev = len(dp[i - 1])
                for j in range(prev + 1):
                    if j == 0 or j == prev:
                        continue
                    else:
                        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

        return dp[:numRows]


s = Solution()
numRows1, numRows2, numRows3 = 5, 2, 1
