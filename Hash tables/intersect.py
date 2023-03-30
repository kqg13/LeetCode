# Easy hash table/binary search problem 350: Intersection of Two Arrays II

# Given two arrays, write a function to compute their intersection.
#
# Example 1:
# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2], Output: [2,2]
# Example 2:
# Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4], Output: [4,9]

from collections import Counter


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        common_c = Counter(nums1) & Counter(nums2)
        output = []
        for k in common_c:
            lst = [k] * common_c[k]
            output.extend(lst)
        return output
