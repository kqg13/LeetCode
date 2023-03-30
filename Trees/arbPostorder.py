# Easy problem 590: N-ary Tree Postorder Traversal


# Given an n-ary tree, return the postorder traversal of its nodes' values.

# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    # Recursive
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        output = []

        def traverse(node):
            for child in node.children:
                traverse(child)
            output.append(node.val)

        if root:
            traverse(root)
        else:
            return []
        return output

    # Iterative
    def iter_postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root], []

        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
            stack.extend(root.children)

        return output[::-1]
