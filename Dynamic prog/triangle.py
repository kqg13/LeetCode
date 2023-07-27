# 120: Triangle
# https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle):
        dp = self.padTriangle(triangle)
        dp[0][1] = triangle[0][0]
        for i in range(1, len(triangle)):
            for j in range(1, len(dp[i]) - 1):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j - 1]
        lastRow = dp[-1]
        return min(lastRow)

    def padTriangle(self, triangle):
        paddedTriangle = list()
        for row in triangle:
            nCols = len(row)
            padded = [float('inf')] * (nCols + 2)
            paddedTriangle.append(padded)
        return paddedTriangle
