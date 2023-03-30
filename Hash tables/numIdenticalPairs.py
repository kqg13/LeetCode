# 1512: Number of Good Pairs
# https://leetcode.com/problems/number-of-good-pairs/

from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums) -> int:
        theMap = defaultdict(list)
        result = 0
        for i, num in enumerate(nums):
            if num not in theMap:
                theMap[num].append(i)
            else:
                nIndices = len(theMap[num])
                # print("nIindices: ", nIndices)
                result += nIndices
                theMap[num].append(i)
                # print("result: ", result)
        return result

    # Explanation: https://leetcode.com/problems/number-of-good-pairs/discuss/939461/Java-1-PASS-One-Pass-Solution-%2B-Intuitive-Explanation
    def numIdenticalPairsBetter(self, nums) -> int:
        all_nums = defaultdict(int)
        result = 0
        for num in nums:
            result += all_nums[num]
            print(result)
            all_nums[num] += 1
            print(all_nums)
        return result


nums1 = [1, 2, 3, 1, 1, 3]  # Expected: 4
nums2 = [1, 1, 1, 1]  # Expected: 6
nums3 = [1, 2, 3]  # Expected: 0
s = Solution()
s.numIdenticalPairsBetter(nums1)
# s.numIdenticalPairs(nums2)
# s.numIdenticalPairs(nums3)
