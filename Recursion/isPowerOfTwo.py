# 231. Power of Two
# https://leetcode.com/problems/power-of-two/

# Given an integer n, return true if it is a power of two. Otherwise, return false.
# An int n is a power of two, if there exists an integer x such that n == 2^x.


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0 or n % 2 == 1:
            return False
        return self.isPowerOfTwoHelper(n, 1)

    def isPowerOfTwoHelper(self, n, i):
        if pow(2, i) == n:
            return True
        if pow(2, i) > n:
            return False
        return self.isPowerOfTwoHelper(n, i + 1)


s = Solution()
n1, n2, n3 = 1, 3, 16
print(s.isPowerOfTwo(n1))
print(s.isPowerOfTwo(n2))
print(s.isPowerOfTwo(n3))
