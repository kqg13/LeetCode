# 116: Populating Next Right Pointers in Each Node II
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    class Solution(object):
        def connect(self, root):
            """
            :type root: Node
            :rtype: Node
            """
            self.connect_dfs(root)
            return root

        def connect_dfs(self, node):
            if node is None:
                return
            # Case 1
            if node.left and node.right:
                node.left.next = node.right

            next_node = self.find_next_helper(node)

            # Case 2
            if node.left and not node.right:
                node.left.next = next_node
            elif node.right:
                node.right.next = next_node

            self.connect_dfs(node.right)
            self.connect_dfs(node.left)

        def find_next_helper(self, node):
            while node.next:
                node = node.next
                if node.left:
                    return node.left
                elif node.right:
                    return node.right
            return None