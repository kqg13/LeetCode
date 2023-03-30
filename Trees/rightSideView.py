# LeetCode problem 199: Binary Tree Right Side View

# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.

# Example: [1, 2, 3, null, 5, null, 4] ---> [1, 3, 4]


from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root):
        if root is None: return []
        current, children, results = [root], [], []
        while current:
            results.append(current[0].val)
            for node in current:
                if node.right:
                    children.append(node.right)
                if node.left:
                    children.append(node.left)
            current = children.copy()
            children.clear()
        return results

    def bfs(self, root: TreeNode) -> list:
        if root is None: return []
        q, results = deque([root]), []
        while len(q) > 0:
            node = q.popleft()
            results.append(node.val)
            if node.left:
                leftChild = node.left
                q.append(leftChild)
            if node.right:
                rightChild = node.right
                q.append(rightChild)
        return results

    def rightSideViewReview(self, root):
        """
        :param root: TreeNode
        :return: List[int]
        """
        if root is None:
            return None
        queue, children, results = [root], list(), list()
        while queue:
            results.append(queue[0].val)
            for node in queue:
                if node.right:
                    children.append(node.right)
                if node.left:
                    children.append(node.left)
            queue = children.copy()
            children.clear()
        return results


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)


print(s.rightSideView(root))
print(s.rightSideViewReview(root))
