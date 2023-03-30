# 378: Kth Smallest Element in a Sorted Matrix


# Given an n x n matrix where each of the rows and cols are sorted in asc order,
# return the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.

# Input: matrix1 = [[1, 5, 9], [10, 11, 13], [12, 13, 15]], k1 = 8 ---> 13
# Input: matrix2 = [[-5]], k2 = 1 ---> -5


import heapq as hq


class Solution:
    def kthSmallest(self, matrix, k):
        """
        :param matrix: List[List[int]]
        :param k: int
        :return: int
        """
        flatList = [item for sublist in matrix for item in sublist]
        hq.heapify(flatList)
        return hq.nsmallest(k, flatList)[k - 1]


s = Solution()
matrix1, k1 = [[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8
matrix2, k2 = [[-5]], 1
print(s.kthSmallest(matrix1, k1))
print(s.kthSmallest(matrix2, k2))

