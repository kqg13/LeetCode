# Medium DP Problem 300: Longest Increasing Subsequence

# Given an unsorted array of integers, find the length of longest increasing
# subsequence.

# Input: [10, 9, 2, 5, 3, 7, 101, 18] ---> 4


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        includedBest, overallBest = [1] * len(nums), [1] * len(nums)

        for i, n in enumerate(nums[1:], start=1):
            recentMax, recentMin = self.recentMaxMin(nums, i, includedBest)

            ib = 0
            if recentMin != -1:
                ib = includedBest[recentMin]
            includedBest[i] = ib + 1

            ob = 0
            if recentMax != -1:
                ob = overallBest[recentMax]
            overallBest[i] = max(includedBest[i], ob)

        print("in: ", includedBest, "ob: ", overallBest)
        return overallBest[-1]

    def recentMaxMin(self, nums, index, includedbest):
        el, recentMax, recentMin = nums[index], -1, -1

        # Get recent max index
        for i in range(index - 1, -1, -1):
            if nums[i] >= el:
                recentMax = i
                break
        # Get recent max of mins index
        allMins = []
        allMins.extend(i for i in range(index - 1, -1, -1) if nums[i] < el)

        if allMins:
            maxOfIBmins = max(includedbest[idx] for idx in allMins)
            recentMin = includedbest.index(maxOfIBmins)

        return recentMax, recentMin


s = Solution()
seq1 = [10, 9, 2, 5, 3, 7, 101, 18]
seq2 = [3, 2, 66, 1, 5, 2, 4, 20]
seq3 = [1, 3, 6, 7, 9, 4, 10, 5, 6]

# print(s.lengthOfLIS(seq1))
print(s.lengthOfLIS(seq2))
# print(s.lengthOfLIS(seq3))
