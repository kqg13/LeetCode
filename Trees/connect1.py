# 116: Populating Next Right Pointers in Each Node
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        self.connect_dfs(root)
        return root

    def connect_dfs(self, node):
        if node is None:
            return

        # Case 1
        if node.left:
            node.left.next = node.right
        # Case 2
        if node.next and node.right:
            node.right.next = node.next.left

        self.connect_dfs(node.left)
        self.connect_dfs(node.right)