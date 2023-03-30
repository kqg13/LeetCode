# Medium heap problem 347: Top K Frequent Elements

# Given a non-empty array of integers, return the k most frequent elements.
# Example:
# Input: nums = [1, 1, 1, 2, 2, 3], k = 2    Output: [1,2]


from collections import Counter
from heapq import nlargest


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # O(NlogK)
        count = Counter(nums)  # Creates dictionary in O(N)
        print(count)
        return nlargest(k, count.keys(), key=lambda x: count[x])  # O(NlogK), note: key=get also works


nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print(Solution().topKFrequent(nums1, k1))

# closed mouths don't get fed
# compromising safety

