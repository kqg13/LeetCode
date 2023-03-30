# LeetCode Divide & conquer problem 240: Search a 2D Matrix II

# Write an efficient algo that searches for target val in an m x n integer matrix.
# The matrix has the following properties:

# Ints in each row are sorted in ascending from left to right.
# Ints in each col are sorted in ascending from top to bottom


class Solution:
    # Time: O(m + n), Space: O(1)
    def searchMatrixOptimal(self, matrix, target) -> bool:
        rows, cols = len(matrix) - 1, len(matrix[0]) - 1
        m, n = rows, 0
        while 0 <= m <= rows and 0 <= n <= cols:
            if matrix[m][n] == target:
                return True
            elif matrix[m][n] > target:
                m -= 1
            else:
                n += 1
        return False

    # Time: O(NlogN) divide & conquer solution
    def searchMatrix(self, matrix, target: int) -> bool:
        m, n = len(matrix) - 1, len(matrix[0]) - 1
        self.matrix = matrix
        self.target = target
        return self.searchMatrixHelper(0, m, 0, n)

    def searchMatrixHelper(self, t, b, l, r):
        # Base case: check whether it's an empty submatrix
        if t > b or l > r:
            return False
        mid = (l + r) // 2
        found, index = self.searchColumn(mid, t, b)
        if found:
            return True
        return self.searchMatrixHelper(index + 1, b, l, mid - 1) or self.searchMatrixHelper(t, index, mid + 1, r)

    def searchColumn(self, columnNum, top, bottom):
        for i in range(top, bottom + 1):
            num = self.matrix[i][columnNum]
            if num == self.target:
                return True, i
            elif num > self.target:
                return False, i - 1
        return False, bottom


s = Solution()

# Expected: True
m1 = [[1, 4, 7, 11, 15],
      [2, 5, 8, 12, 19],
      [3, 6, 9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]]
t1 = 5

# Expected: False
m2 = [[1, 4, 7, 11, 15],
      [2, 5, 8, 12, 19],
      [3, 6, 9, 16, 22],
      [10, 13, 14, 17, 24],
      [18, 21, 23, 26, 30]]
t2 = 20
