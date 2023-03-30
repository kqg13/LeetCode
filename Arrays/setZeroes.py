# Medium Array problem 73: Set Matrix Zeroes

# Given a m x n matrix, if an element is 0, set its entire row
# and column to 0. Do it in-place.

# Example:
# Input:
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]

# Output:
# [
#  [1,0,1],
#  [0,0,0],
#  [1,0,1]
# ]


class Solution:
    def setZeroes(self, matrix):
        """
        : type matrix: List[List[int]]
        Do not return anything, modify matrix in-place instead.
        """
        self.zeroes = []
        self.n_rows = len(matrix)
        self.n_cols = len(matrix[0])

        def find_zeroes():
            for r in range(0, self.n_rows):
                for c in range(0, self.n_cols):
                    if matrix[r][c] == 0:
                        self.zeroes.append((r, c))

        def set_rows():
            for c in range(0, self.n_cols):
                for dim in self.zeroes:
                    matrix[dim[0]][c] = 0

        def set_cols():
            for r in range(0, self.n_rows):
                for dim in self.zeroes:
                    matrix[r][dim[1]] = 0

        find_zeroes()
        set_rows()
        set_cols()
