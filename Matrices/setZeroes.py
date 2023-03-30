# Matrix problem 73: Set Matrix Zeroes

# Given a m x n matrix, if an element is 0, set its entire row and col to 0.
# Do it in-place.

# Example:
# Input:
# [
#   [1, 1, 1],
#   [1, 0, 1],
#   [1, 1, 1]]

# Output:
# [
#  [1, 0, 1],
#  [0, 0, 0],
#  [1, 0, 1]]


class Solution:
    def setZeroes(self, matrix):
        """
        : type matrix: List[List[int]]
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        isFirstRow, isFirstCol = self.isFirstRow(matrix), self.isFirstCol(matrix)
        self.setCoordinates(matrix, m, n)
        self.fillMatrix(matrix, m, n)
        self.fillFirsts(matrix, n, isFirstRow, isFirstCol)

    def isFirstRow(self, matrix):
        # Returns whether first row needs to be set to 0s
        return 0 in matrix[0]

    def isFirstCol(self, matrix):
        # Returns whether first col needs to be set to 0s
        for row in matrix:
            if row[0] == 0:
                return True
        return False

    def setCoordinates(self, matrix, m, n):
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

    def fillMatrix(self, matrix, m, n):
        for row in range(1, m):
            if matrix[row][0] == 0:
                matrix[row] = [0] * n
        for col in range(1, n):
            if matrix[0][col] == 0:
                for row in range(1, m):
                    matrix[row][col] = 0

    def fillFirsts(self, matrix, n, isFirstRow, isFirstCol):
        if isFirstRow:
            matrix[0] = [0] * n
        if isFirstCol:
            for row in matrix:
                row[0] = 0


s = Solution()
mtx1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]]

mtx2 = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]]

mtx3 = [
        [0, 1]]


mtx4 = [
        [0], [1]]
