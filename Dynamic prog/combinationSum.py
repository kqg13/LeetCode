# Medium DP problem 39: Combination Sum
# https://leetcode.com/problems/combination-sum/


class Solution:
    def combinationSum(self, candidates, target):
        """
        :param candidates: List[int]
        :param target: int
        :return: List[List[int]]
        """
        res = []
        # candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return None
        if target == 0:
            res.append(path)
            return None
        for i in range(index, len(nums)):
            self.dfs(nums, target - nums[i], i, path + [nums[i]], res)


# Test
s = Solution()
cand = [2, 3, 6, 7]
tar = 7
print(s.combinationSum(cand, tar))
