# 39: Combination Sum
# https://leetcode.com/problems/combination-sum/

# Given an array of distinct ints candidates and a target integer, return a list of all unique
# combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.
#
# It is guaranteed that the number of unique combinations that sum up to
# target is < 150 combinations for the given input.


class Solution(object):
    def combinationSum(self, candidates, target):
        self.candidates = candidates
        self.target = target
        self.results = list()
        self.combinationSumHelper(0, [], target)
        return self.results

    def combinationSumHelper(self, start, current, delta):
        # 2 base cases
        if delta == 0:
            self.results.append(current.copy())
        if delta < 0:
            return
        for i in range(start, len(self.candidates)):
            current.append(self.candidates[i])
            delta -= self.candidates[i]
            self.combinationSumHelper(start + i, current, delta)
            current.pop()
            delta += self.candidates[i]


candidates1, target1 = [2, 3, 6, 7], 7
candidates, target2 = [2, 3, 5], 8
candidates3, target3 = [2], 1
candidates4, target4 = [1], 1
candidates5, target5 = [1], 2
s = Solution()

