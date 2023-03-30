from collections import defaultdict
from collections import deque


# LeetCode #987 : Vertical Order Traversal of a Binary Tree
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def constructTree(self, inputTree, i, n):
        if inputTree is None: return None

        node = None

        if i < n and inputTree[i] is not None:
            nodeVal = inputTree[i]
            node = TreeNode(nodeVal)
            node.left = self.constructTree(inputTree, 2 * i + 1, n)
            node.right = self.constructTree(inputTree, 2 * i + 2, n)

        return node

    def verticalTraversal(self, root: TreeNode):
        """
        :param root: TreeNode
        :return: List[List[int]]
        """
        d = defaultdict(lambda: list())
        row, col = 0, 0
        queue = deque([(root, col, row)])

        while queue:
            node, col, row = queue.popleft()
            d[(col, row)].append(node.val)
            if node.left:
                new_col, new_row = col - 1, row + 1
                queue.append((node.left, new_col, new_row))
            if node.right:
                new_col, new_row = col + 1, row + 1
                queue.append((node.right, new_col, new_row))

        sorted_keys = sorted(d.keys(), key=lambda x: (x[0], x[1]))
        results = self.getResults(sorted_keys, d)

        return results

    def getResults(self, sorted_keys, d):
        results = list()
        current_col = float('inf')
        print(d)
        print(sorted_keys)

        for col, row in sorted_keys:
            lst = sorted(d[(col, row)])
            if current_col != col:
                results.append(lst)
            else:
                results[-1].extend(lst)
            current_col = col

        return results


s = Solution()
root1 = [3, 9, 20, None, None, 15, 7]  # Expected: [[9], [3, 15], [20], [7]]
tree1 = s.constructTree(root1, 0, len(root1))
print(s.verticalTraversal(tree1))

root2 = [1, 2, 3, 4, 5, 6, 7]  # Expected: [[4], [2], [1, 5, 6], [3], [7]]
tree2 = s.constructTree(root2, 0, len(root2))
s.verticalTraversal(tree2)
