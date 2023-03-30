# Easy DP problem 70: Climbing Stairs

# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can
# you climb to the top?  Note: Given n will be a positive integer.


class Solution:
    def __init__(self):
        self.memo = {}

    # Memoization (top-down): time O(N) space O(N)
    def climb_memo(self, n):
        """
        :param n: int
        :return: int
        """
        if n in self.memo:
            return self.memo[n]
        elif n < 0:
            return 0
        elif n == 0:
            return 1
        else:
            res = self.climb_memo(n - 2) + self.climb_memo(n - 1)
            self.memo[n] = res
            return res

    # DP (1-D bottom-up): time O(N) space O(N)
    def climb_dp(self, n):
        """
        :param n: int
        :return: int
        """
        dp = [1, 1, 2]
        if n == 0 or n == 1 or n == 2:
            return dp[n]

        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])

        return dp[-1]

# Reference: memoization vs. DP
# https://stackoverflow.com/questions/6184869/what-is-the-difference-between-memoization-and-dynamic-programming

s = Solution()
print(s.climb_dp(4))
print(s.climb_dp(5))

