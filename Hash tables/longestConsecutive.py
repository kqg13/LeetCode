# Problem 128: Longest Consecutive Sequence

# Given an unsorted array of ints, find the length of the longest consecutive
# elements sequence.  Your algorithm should run in O(n) complexity.

# Example: [100, 4, 200, 1, 3, 2] --> 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]


class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums: return 0
        best = 1
        theDict = {num: [num, num] for num in nums}
        for num in nums:
            print("best ", best, "num ", num, theDict)
            if num not in theDict: continue
            lower, upper = theDict[num][0] - 1, theDict[num][1] + 1
            if lower in theDict:
                theDict[lower][1] = upper - 1
                theDict[num][0] = lower
                current = theDict[lower][1] - theDict[lower][0] + 1
                best = max(best, current)
                # del theDict[num]
                continue
            if upper in theDict:
                theDict[upper][0] = lower + 1
                theDict[num][1] = upper
                current = theDict[upper][1] - theDict[upper][0] + 1
                best = max(best, current)
        return best


s = Solution()
nums1 = [100, 4, 200, 1, 3, 2]  # Expected: 4
nums2 = [100, 99, 3, 10, 1, 2]  # Expected: 3
nums3 = [0, 1, 0, 1, 2]  # Expected: 3
nums4 = [1, 2, 0, 1]  # Expected: 3
nums5 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]  # Expected: 9
# nums6 = [-1, 9, -3, -6, 7, -8, -6, 2, 9, 2, 3, -2, 4, -1, 0, 6, 1, -9, 6, 8, 6, 5, 2]
# print("nums1: ", s.longestConsecutive(nums1))
# print("nums2: ", s.longestConsecutive(nums2))
# print("nums3: ", s.longestConsecutive(nums3))
# print("nums4: ", s.longestConsecutive(nums4))
print("nums5: ", s.longestConsecutive(nums5))
# print("nums6: ", s.longestConsecutive(nums6))
