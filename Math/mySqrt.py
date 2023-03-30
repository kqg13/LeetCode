# Easy problem 69: Sqrt(x)

# Implement int sqrt(int x).
#
# Compute and return the square root of x, where x is guaranteed to be a
# non-negative integer. Since the return type is an integer, the decimal
# digits are truncated and only the integer part of the result is returned.

from math import trunc


class Solution:
    def mySqrt(self, x):
        """
        :param x: int
        :return: int
        """
        return trunc(x ** 0.5)

    def mySqrtBinarySearch(self, x):
        """
        :param x: int
        :return: int
        """
        if x <= 1: return x
        low, high = 1, x
        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1


s = Solution()
print(s.mySqrt(25))
print(s.mySqrtBinarySearch(25))
