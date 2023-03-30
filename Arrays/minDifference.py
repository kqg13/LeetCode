# 1509: Minimum Difference Between Largest and Smallest in Three Moves
# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/

class Solution(object):
    def minDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 4:
            return 0
        sorted_nums = sorted(nums)
        min_array = sorted_nums[:4]
        max_array = sorted_nums[-4:]
        d = [x1 - x2 for (x1, x2) in zip(max_array, min_array)]
        return min(d)

    def testGetTopFourMaxMin(self, nums):
        maxV = [float('-inf')] * 4
        for n in nums:
            if n > maxV[0]:
                maxV[0] = n
                for i in range(0, 3):
                    if maxV[i] > maxV[i + 1]:
                        maxV[i], maxV[i + 1] = maxV[i + 1], maxV[i]
            print("top 4 max: ", maxV)

        minV = [float('inf')] * 4
        for n in nums:
            if n < minV[0]:
                minV[0] = n
                for i in range(0, 3):
                    if minV[i] < minV[i + 1]:
                        minV[i], minV[i + 1] = minV[i + 1], minV[i]
            print("top 4 mins: ", minV)


s = Solution()
s.testGetTopFourMaxMin([3, 1, 9, 0, 11])
