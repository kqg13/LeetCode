# LeetCode Problem 62: Unique Paths

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
        return 0


s = Solution()
m1, n1 = 3, 3
m2, n2 = 7, 3
m3, n3 = 3, 2

s.uniquePaths(m1, n1)
s.uniquePaths(m2, n2)
s.uniquePaths(m3, n3)
