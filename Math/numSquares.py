# 279: Perfect Squares
# https://leetcode.com/problems/perfect-squares/description/?envType=company&envId=citadel&favoriteSlug=citadel-six-months


from math import isqrt
from functools import cache


class Solution:
    def numSquaresRecursive(self, n: int) -> int:
        self.perf_squares = [square**2 for square in range(1, isqrt(n) + 1)]
        result = self.numSquaresHelper(n)
        print(result)
        return result

    @cache
    def numSquaresHelper(self, k):
        if k == 0: return 0
        result = float('inf')
        for perf_square in self.perf_squares:
            if k < perf_square: break
            min_square = self.numSquaresHelper(k - perf_square) + 1
            result = min(min_square, result)
        return result

    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)
        perf_squares = [square ** 2 for square in range(1, isqrt(n) + 1)]
        for i in range(1, n + 1):
            solutions = []
            for perf_square in perf_squares:
                if i - perf_square < 0: break
                solutions.append(dp[i - perf_square])
            dp[i] = min(solutions) + 1
        return dp[-1]


s = Solution()
n1 = 12  # Expected: 3
n2 = 13  # Expected: 2
