# 1277: Count Square Submatrices with All Ones
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
# Optimal: https://leetcode.com/problems/count-square-submatrices-with-all-ones/solutions/441620/dp-with-figure-explanation/

class Solution:
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        dp_board = matrix.copy()
        m, n = len(dp_board), len(dp_board[0])
        iterations = min(m, n)
        # first iteration for 1x1s
        result = sum([sum(row) for row in dp_board])

        self.padFirstRowLastColumn(dp_board, m, n)

        for iteration in range(2, iterations + 1):  # do iterations starting from second
            for r, row in enumerate(dp_board[:-1]):
                for c, col in enumerate(row[:-1]):
                    if col and dp_board[r + 1][c] == dp_board[r + 1][c + 1] == dp_board[r][c + 1] == 1:
                        result += 1
                    else:
                        dp_board[r][c] = 0
        return result

    def padFirstRowLastColumn(self, dp_board, m, n):
        # Pad last row
        dp_board.append([0] * n)
        # Pad last col
        for row in dp_board:
            row.append(0)


s = Solution()
matrix1 = [
              [0, 1, 1, 1],
              [1, 1, 1, 1],
              [0, 1, 1, 1]
          ]

matrix2 = [
              [1, 0, 1],
              [1, 1, 0],
              [1, 1, 0]
          ]
