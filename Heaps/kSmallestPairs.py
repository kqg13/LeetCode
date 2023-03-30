# 373. Find K Pairs with Smallest Sums


# You are given two int arrays nums1 and nums2 sorted in asc order and an int k.
# Define a pair (u,v) which consists of one element from the first array and one element from the second.
# Find the k pairs (u1, v1), (u2, v2) ... (uk, vk) with the smallest sums.

# Input: nums1 = [1, 7, 11], nums2 = [2, 4, 6], k = 3 ---> [[1, 2], [1, 4],[1, 6]]
# Input: nums1 = [1, 1, 2], nums2 = [1, 2, 3], k = 2 ---> [1, 1], [1, 1]
# Input: nums1 = [1, 2], nums2 = [3], k = 3 ---> [1, 3], [2, 3]


import heapq


# Time: O(N) + O(NlogK) or O(NlogK)
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :param nums1: List[int]
        :param nums2: List[int]
        :param k: int
        :return: List[List[int]]
        """
        if not nums1 or not nums2 or k < 1:
            return []
        len1, len2, hq, results = len(nums1), len(nums2), list(), list()
        # Heapify
        for i in range(len1):
            val = nums1[i] + nums2[0]
            hq.append((val, i, 0))
        heapq.heapify(hq)

        while hq and k > 0:
            val, i, j = heapq.heappop(hq)
            results.append([nums1[i], nums2[j]])
            k -= 1
            if j + 1 < len2:
                new_val = nums1[i] + nums2[j + 1]
                heapq.heappush(hq, (new_val, i, j + 1))
        return results
