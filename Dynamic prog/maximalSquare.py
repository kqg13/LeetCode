# 221- Maximal Square
# https://leetcode.com/problems/maximal-square/description/

class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        # fill first row
        dp[0] = [int(r) for r in matrix[0]]
        # fill first col
        for i in range(1, m):
            dp[i][0] = int(matrix[i][0])

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j]) + 1

        result = max([max(row) for row in dp])
        return result ** 2


m1 = [
         ["1", "0", "1", "0", "0"],
         ["1", "0", "1", "1", "1"],
         ["1", "1", "1", "1", "1"],
         ["1", "0", "0", "1", "0"]
     ]   # Expected: 4

m2 = [
        ["0", "1"],
        ["1", "0"]
     ]  # Expected: 1
