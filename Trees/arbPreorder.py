# Easy problem 589: N-ary Tree Preorder Traversal

# Given an n-ary tree, return the preorder traversal of its nodes' values.

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    # Recursive
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        output = []

        def traverse(node):
            output.append(node.val)
            for child in node.children:
                traverse(child)

        if root:
            traverse(root)
        else:
            return []
        return output

    # Iterative
    def iter_preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return []

        stack, output = [root], []

        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
        return output
