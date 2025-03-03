# 2181: Merge Nodes in Between Zeros
# https://leetcode.com/problems/merge-nodes-in-between-zeros/description/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        res = str(self.val) + ", "
        ptr = self.next
        while ptr:
            res += str(ptr.val) + ", "
            ptr = ptr.next
        res = res.strip(", ")
        return res


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ptr = head
        last_node = ListNode(-1)
        dummy = last_node
        while ptr.next:
            current_sum = 0
            ptr = ptr.next
            while ptr.val != 0:
                current_sum += ptr.val
                ptr = ptr.next
            ptr.val = current_sum
            last_node.next = ptr
            last_node = ptr
        return dummy.next


s = Solution()
l1 = ListNode(0, ListNode(3, ListNode(1, ListNode(0, ListNode(4, ListNode(5, ListNode(2, ListNode(0))))))))
l2 = ListNode(0, ListNode(1, ListNode(0, ListNode(3, ListNode(0, ListNode(2, ListNode(2, ListNode(0))))))))
