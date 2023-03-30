# Medium Recursion problem 46: Permutations
# https://leetcode.com/problems/permutations/
# https://www.youtube.com/watch?v=KukNnoN-SoY for good discussion on recursion tree


class Solution:
    def permute(self, nums):
        """
        :param nums: List[int]
        :return: List[List[int]]
        """
        permutations = []
        self.backtrack(nums, [], permutations)
        return permutations

    def backtrack(self, nums, current, permutations):
        if not nums:
            permutations.append(current[:])

        for i in range(len(nums)):
            new_nums = nums[:i] + nums[i+1:]
            new_perms = current + [nums[i]]
            self.backtrack(new_nums, new_perms, permutations)


s = Solution()
array = [1, 2, 3]
print(s.permute(array))
