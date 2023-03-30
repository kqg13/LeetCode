# 2006: Count Number of Pairs With Absolute Difference K
# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/


class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result, d = 0, dict()
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
            if num - k in d:
                result += d[num - k]
            if num + k in d:
                result += d[num + k]
        return result


s = Solution()
nums1, k1 = [1, 2, 2, 1], 1
nums2, k2 = [1, 3], 3
nums3, k3 = [3, 2, 1, 5, 4], 2
nums4, k4 = [3], 20
print(s.countKDifference(nums1, k1))
print(s.countKDifference(nums2, k2))
print(s.countKDifference(nums3, k3))
print(s.countKDifference(nums4, k4))
