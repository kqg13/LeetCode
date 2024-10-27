# 334: Increasing Triplet Subsequence
# https://leetcode.com/problems/increasing-triplet-subsequence/


class Solution:
    def increasingTriplet(self, nums) -> bool:
        first, second = float('inf'), float('inf')

        for num in nums:
            if num > first and num > second:
                return True

            if num <= first:
                first = num
            elif num > first and num <= second:
                second = num

        return False
