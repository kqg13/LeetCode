# 361: Bomb Enemies
# https://leetcode.com/problems/bomb-enemy/description/

from typing import List


class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        m, n, result = len(grid), len(grid[0]), 0
        results_matrix = [[[0, 0] for _ in range(n)] for _ in range(m)]
        # l_to_r
        for r in range(m):
            l_to_r, r_to_l = [0] * n, [0] * n
            runner = 0
            for c in range(n):
                cell = grid[r][c]
                if cell == 'E':
                    runner += 1
                elif cell == '0':
                    l_to_r[c] = runner
                else:
                    runner = 0
            # r_to_l
            runner = 0
            for c in range(n - 1, -1, -1):
                cell = grid[r][c]
                if cell == 'E':
                    runner += 1
                elif cell == '0':
                    r_to_l[c] = runner
                else:
                    runner = 0
            for c in range(n):
                results_matrix[r][c][0] = l_to_r[c] + r_to_l[c]
        # t_to_b
        for c in range(n):
            t_to_b, b_to_t = [0] * m, [0] * m
            runner = 0
            for r in range(m):
                cell = grid[r][c]
                if cell == 'E':
                    runner += 1
                elif cell == '0':
                    t_to_b[r] = runner
                else:
                    runner = 0
            # b_to_t
            runner = 0
            for r in range(m - 1, -1, -1):
                cell = grid[r][c]
                if cell == 'E':
                    runner += 1
                elif cell == '0':
                    b_to_t[r] = runner
                else:
                    runner = 0
            for r in range(m):
                results_matrix[r][c][1] = t_to_b[r] + b_to_t[r]

        result = max(sum(pair) for row in results_matrix for pair in row)
        return result


s = Solution()
grid1 = [["0", "E", "0", "0"], ["E", "0", "W", "E"], ["0", "E", "0", "0"]]
grid2 = [["W", "W", "W"], ["0", "0", "0"], ["E", "E", "E"]]
