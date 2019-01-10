# Easy problem 561: Array Partition I


class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        maxsum = 0
        for i in range(0, len(nums)-1, 2):
            maxsum += min(nums[i], nums[i + 1])
        return maxsum


s = Solution()
nums = [1, 4, 3, 2]
print(s.arrayPairSum(nums))
