# 138: Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

    def __str__(self):
        res = f"val: {str(self.val)} / random: {str(self.random.val)}, "
        ptr = self.next
        while ptr:
            res += f"val: {str(ptr.val)} / random: {str(ptr.random.val)}, "
            ptr = ptr.next
        res = res.strip(", ")
        return res


class Solution:
    def copyRandomList(self, head):
        """
        type head: Node
        :rtype: Node
        """
        if not head: return None

        node_dict = dict()

        first_node_id = id(head)
        copied_node = Node(head.val, None, None)
        node_dict[first_node_id] = copied_node

        while head:
            node_id = id(head)
            copied_node = node_dict[node_id]
            # set next pointer
            if head.next:
                copied_node.next = self.setPointer(node_dict, head.next)
            # set random pointer
            if head.random:
                copied_node.random = self.setPointer(node_dict, head.random)
            # advance
            head = head.next

        return node_dict[first_node_id]

    def setPointer(self, node_dict, node):
        node_id = id(node)
        if node_id in node_dict:
            next_or_random_node = node_dict[node_id]
        else:
            next_or_random_node = Node(node.val, None, None)
            node_dict[node_id] = next_or_random_node
        return next_or_random_node

