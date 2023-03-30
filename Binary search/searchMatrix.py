# Binary Search Problem 74: Search a Matrix

# Write an efficient algo that searches for a value in an m x n matrix.
# This matrix has the following properties:

# Ints in each row are sorted from left to right.
# The first int of each row is greater than the last int of previous row.

# Examples:
# matrix1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target1 = 3 --> T
# matrix2 = [[1, 3, 5,v7], [10, 11, 16, 20], [23, 30, 34, 60]], target2 = 13 ---> F


class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        return True


s = Solution()
matrix1, target1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3
matrix2, target2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13
print(s.searchMatrix(matrix1, target1))
s.searchMatrix(matrix2, target2)
