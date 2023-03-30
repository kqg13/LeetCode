# Problem 1424: Diagonal Traverse II

# Given a list of lists of ints, nums, return all elements of nums in diagonal order.

# Input 1:    nums1 = [[1, 2, 3], [4, 5, 6], [ 7, 8, 9]]
# Output 1:   [1, 4, 2, 7, 5, 3, 8, 6, 9]
# Input 2:    nums2 = [[1, 2, 3, 4, 5], [6, 7], [8], [9, 10, 11], [12, 13, 14, 15, 16]]
# Output 2:   [1, 6, 2, 8, 7, 3, 9, 4, 12, 10, 5, 13, 11, 14, 15, 16]
# Input 3:    nums3 = [[1, 2, 3, 4, 5, 6]]
# Output 3:   [1, 2, 3, 4, 5, 6]


from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, nums):
        theDict = self.storeDiagonals(nums)
        return self.getDiagonals(theDict)

    def storeDiagonals(self, nums):
        theDict = defaultdict(list)
        for rowIndex in range(len(nums)):
            for colIndex in range(len(nums[rowIndex])):
                diagIndex = rowIndex + colIndex
                theNum = nums[rowIndex][colIndex]
                theDict[diagIndex].append(theNum)
        return theDict

    def getDiagonals(self, theDict):
        results = [v for k in theDict.keys() for v in reversed(theDict[k])]
        return results
