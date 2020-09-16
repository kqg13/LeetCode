# Medium Greedy Problem 1564: Put Boxes Into the Warehouse I

# Given two arrays of positive ints boxes and warehouse representing the heights
# of some boxes of unit width, and the heights of n rooms in a warehouse, respectively.
# The warehouse's rooms are labeled from 0 to n - 1 from left to right where
# warehouse[i] is the height of the ith room.

# Boxes are put into the warehouse by the following rules:
# 1- Boxes can't be piled up;
# 2- You can rearrange the order of the boxes;
# 3- Boxes can only be pushed into warehouse from left to right only;
# 4- If the height of some room in the warehouse < height of a box, then the
#    box will be stopped before that room, so are the boxes behind it.

# Return the maximum # of boxes you can put into the warehouse

# Ex 1: boxes = [4, 3, 4, 1], warehouse = [5, 3, 3, 4, 1] --> 3
# Ex 2: boxes = [1, 2, 2, 3, 4], warehouse = [3, 4, 1, 2] --> 3
# Ex 3: boxes = [1, 2, 3], warehouse = [1, 2, 3, 4] --> 1
# Ex 4: boxes = [4, 5, 6], warehouse = [3, 3, 3, 3, 3] --> 0


class Solution(object):
    def maxBoxesInWarehouse(self, boxes, warehouse):
        """
        :type boxes: List[int]
        :type warehouse: List[int]
        :rtype: int
        """
        for i in range(1, len(warehouse)):
            if warehouse[i - 1] < warehouse[i]:
                warehouse[i] = warehouse[i - 1]

        boxes_sorted = sorted(boxes)  # O(NlogN)
        box, n, count = 0, len(warehouse) - 1, 0
        for i in range(n, -1, -1):
            if boxes_sorted[box] <= warehouse[i]:
                box += 1
                count += 1
        print(count)
        return count


s = Solution()
b1, w1 = [4, 3, 4, 1], [5, 3, 3, 4, 1]
b2, w2 = [1, 2, 2, 3, 4], [3, 4, 1, 2]
b3, w3 = [1, 2, 3], [1, 2, 3, 4]
b4, w4 = [4, 5, 6], [3, 3, 3, 3, 3]
s.maxBoxesInWarehouse(b1, w1)
s.maxBoxesInWarehouse(b2, w2)
s.maxBoxesInWarehouse(b3, w3)
s.maxBoxesInWarehouse(b4, w4)
