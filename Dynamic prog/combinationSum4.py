# Medium DP problem 377: Combination Sum IV
# https://leetcode.com/problems/combination-sum-iv/


# Time: O(N * len(target)) Space: O(N)
class Solution:
    def combinationSum4(self, target, nums):
        """
        :param target: int
        :param nums: List[int]
        :return: int
        """
        results = [0] * (target + 1)
        results[0] = 1

        for i in range(1, len(results)):
            for j in range(0, len(nums)):
                if i - nums[j] >= 0:
                    results[i] += results[i - nums[j]]
        return results[-1]


# Test
s = Solution()
nums = [2, 3, 4, 7]
tar = 7
print(s.combinationSum4(tar, nums))
