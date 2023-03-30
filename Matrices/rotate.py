# Matrix Problem #48: Rotate Image

# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.

# Examples:
# matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] --> [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
# matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# --> [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
# matrix3 = [[1]] --> [[1]]
# matrix4 = [[1, 2], [3, 4]] --> [[3, 1], [4, 2]]

import numpy as np


class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        np_matrix = np.array(matrix)
        self.rotateHelper(np_matrix)
        return np_matrix.tolist()

    def rotateHelper(self, np_matrix):
        n = len(np_matrix)
        if n == 1:
            return
        elif n == 2:
            self.doRotations(np_matrix)
        else:
            self.doRotations(np_matrix)
            # print(np_matrix)
            self.rotateHelper(np_matrix[1:-1, 1:-1])

    def doRotations(self, np_matrix):
        n = len(np_matrix)
        for i in range(n - 1):
            np_matrix[0, 0 + i], np_matrix[0 + i, n - 1] = np_matrix[0 + i, n - 1], np_matrix[0, 0 + i]
            np_matrix[0, 0 + i], np_matrix[n - 1, n - 1 - i] = np_matrix[n - 1, n - 1 - i], np_matrix[0, 0 + i]
            np_matrix[0, 0 + i], np_matrix[n - 1 - i, 0] = np_matrix[n - 1 - i, 0], np_matrix[0, 0 + i]


s = Solution()
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
matrix3 = [[1]]
matrix4 = [[1, 2], [3, 4]]
print(s.rotate(matrix1))
print(s.rotate(matrix2))  # [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
print(s.rotate(matrix3))
