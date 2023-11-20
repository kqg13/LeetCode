# 740 - Delete and Earn
# https://leetcode.com/problems/delete-and-earn/description/

from collections import defaultdict


class Solution:
    def deleteAndEarnRecursive(self, nums) -> int:
        self.d = defaultdict(lambda: 0)
        for num in nums:
            self.d[num] += num
        max_nums = max(nums)
        result = self.deleteAndEarnHelper(max_nums)
        return result

    def deleteAndEarnHelper(self, i):
        if i <= 0:
            return 0
        pick = self.d[i] + self.deleteAndEarnHelper(i - 2)
        not_pick = self.deleteAndEarnHelper(i - 1)
        return max(pick, not_pick)

    # Space-optimized DP: O(NlogN)
    def deleteAndEarn(self, nums) -> int:
        d = defaultdict(lambda: 0)
        for num in nums:
            d[num] += num
        sorted_keys = sorted(d.keys())
        best_incl = d[sorted_keys[0]]
        best_excl = 0
        for i, num in enumerate(sorted_keys[1:]):
            best_excl_new = max(best_incl, best_excl)
            if num - sorted_keys[i] == 1:
                best_incl = best_excl + d[num]
            else:
                best_incl = best_excl_new + d[num]
            best_excl = best_excl_new
        return max(best_incl, best_excl)
