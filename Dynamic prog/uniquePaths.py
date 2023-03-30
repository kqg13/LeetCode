# LeetCode Problem 62: Unique Paths
# https://leetcode.com/problems/unique-paths/

# A robot is located at the top-left corner of a m x n grid
# (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of
# the grid.  How many possible unique paths are there?

# Input: m = 3, n = 3 --> 6
# Input: m = 7, n = 3 --> 28
# Input: m = 3, n = 2 --> 3


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.unique_paths = 0
        self.m, self.n = m, n
        self.uniquePathsHelper(0, 0)
        return self.unique_paths

    def uniquePathsHelper(self, r, c):
        if r == self.m - 1 and c == self.n - 1:
            self.unique_paths += 1
            return
        if r == self.m or c == self.n:
            return
        self.uniquePathsHelper(r + 1, c)
        self.uniquePathsHelper(r, c + 1)

    # for memoization trick is to start backwards
    def uniquePathsMemo(self, m, n):
        self.m, self.n = m, n
        self.memo = [[0] * n for _ in range(m)]
        self.fillFirstRow()
        self.fillFirstCol()
        return self.uniquePathsMemoHelper(self.m - 1, self.n - 1)

    def fillFirstRow(self):
        for i in range(self.n):
            self.memo[0][i] = 1

    def fillFirstCol(self):
        for i in range(self.m):
            self.memo[i][0] = 1

    def uniquePathsMemoHelper(self, r, c):
        if self.memo[r][c] != 0:
            return self.memo[r][c]
        # no need to check out of bounds because memoization will catch it
        from_up = self.uniquePathsMemoHelper(r - 1, c)
        from_left = self.uniquePathsMemoHelper(r, c - 1)
        self.memo[r][c] = from_up + from_left
        return self.memo[r][c]


s = Solution()
m1, n1 = 3, 3
m2, n2 = 7, 3
m3, n3 = 3, 2

# print(s.uniquePaths(m1, n1))
# print(s.uniquePaths(m2, n2))
print(s.uniquePathsMemo(m2, n2))
