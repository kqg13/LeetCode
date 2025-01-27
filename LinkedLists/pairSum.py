# 2130: Maximum Twin Sum of a Linked List
# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        current = head
        stack = list()
        half_length = self.getLength(head) // 2

        # Build stack first half of list
        for _ in range(half_length):
            stack.append(current.val)
            current = current.next

        max_result = -1

        # Pop stack
        for _ in range(half_length):
            stack_val = stack.pop()
            max_result = max(stack_val + current.val, max_result)
            current = current.next

        return max_result

    def getLength(self, head) -> int:
        length = 0
        current = head
        while current:
            current = current.next.next
            length += 2
        return length

    def reverseLinkedList(self, head) -> ListNode:
        prev = None
        current = head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev


s = Solution()
l1 = ListNode(3, ListNode(2, ListNode(2, ListNode(1, ListNode(3, ListNode(2))))))
l2 = ListNode(3, ListNode(2))
