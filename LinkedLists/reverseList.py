# LeetCode #206: Reverse Linked List


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        prev = None
        curr = head
        while curr:
            nexttemp = curr.next
            curr.next = prev
            prev = curr
            curr = nexttemp
        return prev

    def reverseListRecursive(self, head):
        if not head:
            return None
        if not head.next:
            return head

        lst_node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return lst_node
