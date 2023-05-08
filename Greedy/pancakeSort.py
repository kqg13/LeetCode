# 969: Pancake Sorting
# https://leetcode.com/problems/pancake-sorting/

class Solution:
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        results = list()
        for i in range(len(arr), 1, -1):
            if self.isSorted(arr):
                return results
            maxIndex = self.getMaxIndex(arr, i)
            self.flipArray(arr, maxIndex + 1)
            self.flipArray(arr, i)
            results.extend([maxIndex + 1, i])
        return results

    def getMaxIndex(self, arr, indexVal):
        return arr.index(indexVal)

    def isSorted(self, arr):
        for i in range(len(arr) - 1):
            if arr[i + 1] < arr[i]:
                return False
        return True

    def flipArray(self, arr, k):
        arr[0:k] = arr[0:k][::-1]


s = Solution()
arr1 = [3, 2, 4, 1]
