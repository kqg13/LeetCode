# 339: Nested List Weight Sum
# https://leetcode.com/problems/nested-list-weight-sum/

from typing import List


class NestedInteger:
    def __init__(self, value=None):
        pass

    def isInteger(self):
        pass

    def add(self, elem):
        pass

    def setInteger(self, value):
        pass

    def getInteger(self):
        pass

    def getList(self):
        pass


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        self.result = 0
        self.depthSumHelper(nestedList, 1)
        return self.result

    def depthSumHelper(self, nestedList, depth):
        for ele in nestedList:
            if ele.isInteger():
                self.result += (depth * ele.getInteger())
            else:
                new_nested_list = ele.getList()
                self.depthSumHelper(new_nested_list, depth + 1)


s = Solution()
nestedList1 = [[1, 1], 2, [1, 1]]  # Expected: 10
nestedList2 = [1, [4, [6]]]  # Expected: 27
nestedList3 = [0]  # Expected: 0
