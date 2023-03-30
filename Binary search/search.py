# Easy binary search problem 704: Binary Search

# Given a sorted (in ascending order) integer array nums of n elements and a
# target value, write a function to search target in nums. If target exists,
# then return its index, otherwise return -1.

from bisect import bisect_left


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def search_rec(low, high, nums, target):
            if high >= low:
                mid = (low + high) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    return search_rec(mid + 1, high, nums, target)
                else:
                    return search_rec(low, mid - 1, nums, target)
            else:
                return -1

        return search_rec(0, len(nums) - 1, nums, target)

    # Iterative
    def search_iter(self, nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid
        return -1

    def search_iter2(self, nums, target):
        N = len(nums)
        if N == 0:
            return -1
        l = 0
        r = N - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

    # Using bisect module which assumes list is sorted
    def bisect_search(self, nums, target):
        index = bisect_left(nums, target)
        return index if index < len(nums) and nums[index] == target else -1

    def makeInts(self, n):
        if n == 1:
            return [0]
        results = list()
        nFill, is_odd = n // 2, n % 2
        num = 1
        for _ in range(nFill):
            results.append(num)
            results.append(num * -1)
            num += 1
        if is_odd:
            results.append(0)
        return results


nums1 = [5, 6, 7, 8, 12]
t = 9
s = Solution()
print(s.makeInts(1))
