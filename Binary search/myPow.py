# Medium binary search problem 50: Pow(x, n)

# Implement pow(x, n), which calculates x raised to the power.
# Example 1: Input: 2.00000, 10 Output: 1024.00000
# Example 2: Input: 2.10000, 3  Output: 9.26100


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        def calc_pow(x, n):
            if n == 0:
                return 1.0
            temp = self.myPow(x, n // 2)
            if n % 2 == 0:
                temp = temp * temp
            else:
                temp = x * temp * temp
            return temp

        if n < 0:
            return 1 / calc_pow(x, abs(n))
        else:
            return calc_pow(x, n)


s = Solution()
print(s.myPow(2, 10))
