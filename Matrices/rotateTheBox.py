# 1861: Rotate the Box
# https://leetcode.com/problems/rotating-the-box/description/

from typing import List
import numpy as np


class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rotated = np.rot90(boxGrid, 3).tolist()
        m, n = len(rotated), len(rotated[0])
        for c in range(n):
            low_drop = m - 1
            for r in range(m - 1, -1, -1):
                curr_cell = rotated[r][c]
                if curr_cell == '.':
                    continue
                elif curr_cell == '*':
                    low_drop = r - 1
                else:
                    rotated[r][c] = '.'
                    rotated[low_drop][c] = '#'
                    low_drop -= 1
        return rotated


boxGrid1 = [
                ["#", ".", "#"]
           ]

boxGrid2 = [
                ["#", ".", "*", "."],
                ["#", "#", "*", "."]
           ]

boxGrid3 = [
                ["#", "#", "*", ".", "*", "."],
                ["#", "#", "#", "*", ".", "."],
                ["#", "#", "#", ".", "#", "."]
           ]

boxGrid4 = [
                [1, 2, 3],
                [4, 5, 6]
           ]
s = Solution()
s.rotateTheBox(boxGrid3)
