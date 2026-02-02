# https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/description/
# 2672: Number of Adjacent Elements with the Same Color

from typing import List


class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        result = [0] * len(queries)
        colors = [0] * n
        for i, (index, new_color) in enumerate(queries):
            old_color = colors[index]
            colors[index] = new_color
            if i == 0:
                continue
            # check for same color
            if new_color == old_color:
                result[i] = result[i - 1]
                continue
            change = 0
            # left
            if index > 0:
                if colors[index - 1] == new_color:
                    change += 1
                elif old_color != 0 and colors[index - 1] == old_color:
                    change -= 1
            # right
            if index < n - 1:
                if colors[index + 1] == new_color:
                    change += 1
                elif old_color != 0 and colors[index + 1] == old_color:
                    change -= 1
            result[i] = result[i - 1] + change
        return result
