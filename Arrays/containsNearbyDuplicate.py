# Array problem 219: Contains Nearby Duplicates

# Given an array of integers and an integer k, find out whether there are
# two distinct indices i and j in the array such that nums[i] = nums[j]
# and the absolute difference between i and j is at most k.

# Ex. 1: nums = [1, 2, 3, 1], k = 3 --> true
# Ex. 2: nums = [1, 0, 1, 1], k = 1 --> true
# Ex. 3: nums = [1, 2, 3, 1, 2, 3], k = 2 --> false


from collections import defaultdict


class Solution:
    def containsNearbyDuplicate(self, nums, k) -> bool:
        theDict = defaultdict(lambda: [[], 0])  # [[indices], count]
        for i, num in enumerate(nums):
            theDict[num][0].append(i)
            theDict[num][1] += 1
        for v in theDict.values():
            if v[1] > 1:
                # Calc deltas
                v[0] = [v[0][i + 1] - v[0][i] for i in range(len(v[0]) - 1)]
                if min(v[0]) <= k:
                    return True
        return False

    def containsNearbyDuplicateBetter(self, nums, k) -> bool:
        theDict = {}
        for i, num in enumerate(nums):
            val = theDict.get(num, -1)
            if val > -1:
                delta = i - val
                if delta <= k:
                    return True
            theDict[num] = i
        return False
