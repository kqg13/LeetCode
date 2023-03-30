# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head):
        if head is None:
            return None

        dummy = head
        self.flatten_dfs(dummy)
        return dummy

    def flatten_dfs(self, node):
        current = node.next
        temp = current.next

        # Case 1: if no child, but we have a next
        if not current.child and current.next:
            return self.flatten_dfs(temp)
        # Case 2: if no child, no next
        elif not current.child and not current.next:
            return current
        # Case 3: we have a child, but no next
        elif current.child and not current.next:
            current.child.prev = current
            current.next = current.child
            current.child = None
            return self.flatten_dfs(current.next)
        # Case 4: we have a child, we have a next
        elif current.child and current.next:
            current.child.prev = current
            last_next = self.flatten_dfs(temp)
            last_child = self.flatten_dfs(current.child)
            current.next.prev = last_child
            last_child.next = temp
            current.next = current.child
            current.child = None
            return last_next


s = Solution()

