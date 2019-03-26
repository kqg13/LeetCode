# Medium linked list problem 142: Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/

# Given a linked list, return the node where the cycle begins. If there is no
# cycle, return null.  Note: Do not modify the linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution(object):
    def get_intersect(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return fast
        return None

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = self.get_intersect(head)
        if not head or not head.next or not fast:
            return None

        slow = head

        while slow is not fast:
            slow = slow.next
            fast = fast.next
        return fast


# Test
s = Solution()
h = ListNode(1)
h.next = ListNode(2)
h.next.next = h
print(s.detectCycle(h))
