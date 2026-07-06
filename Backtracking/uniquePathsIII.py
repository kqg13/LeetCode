# 980: Unique Paths III
# https://leetcode.com/problems/unique-paths-iii/description/

from typing import List


# O(3^(m x n))
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.padMatrix()
        m, n = len(self.grid), len(self.grid[0])

        start_square = self.getStartSquare(m, n)
        start_row, start_col = start_square

        self.total_squares_to_visit = sum(square != -1 for row in self.grid for square in row)

        self.visited = set()
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # D, U, R, L
        self.result = 0

        self.backtrack(0, start_row, start_col)

        return self.result

    def backtrack(self, current_squares_visited, r, c):
        if self.grid[r][c] == -1:
            return
        if (r, c) in self.visited:
            return

        if self.grid[r][c] == 2:
            if current_squares_visited == self.total_squares_to_visit - 1:  # less the end square
                self.result += 1
            return

        self.visited.add((r, c))
        current_squares_visited += 1

        for dr, dc in self.directions:
            new_r, new_c = r + dr, c + dc
            self.backtrack(current_squares_visited, new_r, new_c)

        self.visited.remove((r, c))

    def getStartSquare(self, m, n):
        for i in range(m):
            for j in range(n):
                if self.grid[i][j] == 1:
                    return i, j

    def padMatrix(self):
        self.padCols()
        self.padRows()

    def padCols(self):
        for row in self.grid:
            row.insert(0, -1)
            row.append(-1)

    def padRows(self):
        width = len(self.grid[0])
        top_row = [-1] * width
        bottom_row = [-1] * width
        self.grid.insert(0, top_row)
        self.grid.append(bottom_row)


grid1 = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]  # Expected: 2
grid2 = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]  # Expected: 4
grid3 = [[0, 1], [2, 0]]  # Expected: 0
