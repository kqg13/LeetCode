# Easy heap problem 703: Kth Largest Element in a Stream

# Design a class to find the kth largest element in a stream. Note that it is
# the kth largest element in the sorted order, not the kth distinct element.
#
# Your KthLargest class will have a constructor which accepts an integer k
# and an integer array nums, which contains initial elements from the stream.
# For each call to the method KthLargest.add, return the element representing
# the kth largest element in the stream.

# Example:
# int k = 3;
# int[] arr = [4,5,8,2];
# KthLargest kthLargest = new KthLargest(3, arr);
# kthLargest.add(3);   // returns 4
# kthLargest.add(5);   // returns 5
# kthLargest.add(10);  // returns 5
# kthLargest.add(9);   // returns 8
# kthLargest.add(4);   // returns 8

from heapq import heappush, heappushpop, heappop, heapify


# Time: O(NlogN), Space: O(k)
class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.nums = nums
        self.heap = heapify(self.nums)
        while len(self.nums) > k:
            heappop(self.nums)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.k:  # Check capacity
            heappush(self.nums, val)
        else:
            heappushpop(self.nums, val)
        return self.nums[0]


k = 1
nums = []
obj = KthLargest(k, nums)
print(obj.add(-3))
