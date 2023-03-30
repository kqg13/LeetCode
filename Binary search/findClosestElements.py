# LeetCode 658: Find Closest Elements

# Given a sorted int array arr, two integers k and x, return the k closest ints to x in the array.
# The result should also be sorted in ascending order.
#
# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b

# Examples:
# arr1 = [1, 2, 3, 4, 5], k = 4, x = 3 --> [1, 2, 3, 4]
# arr2 = [1, 2, 3, 4, 5], k = 4, x = -1 --> [1, 2, 3, 4]

import bisect


class Solution(object):
    # O(logN + K)
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        self.results = []
        index, low, high = self.getIndex(arr, x)

        n = len(arr)
        while len(self.results) != k:
            dl, dr = float('inf'), float('inf')
            if low > -1:
                dl = abs(x - arr[low])
            if high < n:
                dr = abs(x - arr[high])
            closest = min(dl, dr)
            # print("low: ", low, "high: ", high, "dl: ", dl, "dr: ", dr)
            if dl == closest:
                self.results.insert(0, arr[low])
                low -= 1
            else:
                self.results.append(arr[high])
                high += 1
        return self.results

    def getIndex(self, arr, x):
        index = bisect.bisect_left(arr, x)
        low, high = index - 1, index
        if index < len(arr) and arr[index] == x:
            self.results.append(x)
            high = index + 1
        print(index, low, high)
        return index, low, high


arr1, k1, x1 = [1, 2, 3, 4, 5], 4, 3
arr2, k2, x2 = [1, 2, 3, 4, 5], 4, -1
arr3, k3, x3 = [3, 5, 8, 10], 2, 15
s = Solution()
# print(s.findClosestElements(arr1, k1, x1))
# print(s.findClosestElements(arr2, k2, x2))
print(s.findClosestElements(arr3, k3, x3))

