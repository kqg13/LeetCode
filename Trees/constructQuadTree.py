# 427: Construct Quad Tree
# https://leetcode.com/problems/construct-quad-tree/description/


from typing import List


# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        self.grid = grid
        quadTree = self.constructHelper(0, len(grid), 0, len(grid[0]))
        return quadTree

    def isSameValues(self, sr, er, sc, ec):
        first_ele = self.grid[sr][sc]
        for i in range(sr, er):
            for j in range(sc, ec):
                ele = self.grid[i][j]
                if ele != first_ele:
                    return False, 0
        return True, first_ele

    def constructHelper(self, sr, er, sc, ec) -> 'Node':
        isSame, val = self.isSameValues(int(sr), int(er), int(sc), int(ec))
        if isSame:
            node = Node(val, True, None, None, None, None)
            return node

        n = er - sr
        half_length = n//2

        topLeft = self.constructHelper(sr, sr + half_length, sc, sc + half_length)
        topRight = self.constructHelper(sr, sr + half_length, sc + half_length, ec)
        bottomLeft = self.constructHelper(sr + half_length, er, sc, sc + half_length)
        bottomRight = self.constructHelper(sr + half_length, er, sc + half_length, ec)
        node = Node(val, False, topLeft, topRight, bottomLeft, bottomRight)
        return node


grid1 = [
            [0, 1],
            [1, 0]
        ]

grid2 = [
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0]
        ]
