# 45 - Jump Game II
# https://leetcode.com/problems/jump-game-ii/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def jump(self, nums):
        """
        nums: List[List[int]]
        return: int
        """
        n = len(nums)
        dp = [i for i in range(0, n)]
        for i in range(n - 1):
            for j in range(1, nums[i] + 1):
                if i + j >= n: break

                current_val = dp[i + j]
                jump = 1 + dp[i]
                dp[i + j] = min(current_val, jump)
                if i + j == n - 1:
                    return dp[-1]

        return dp[-1]
