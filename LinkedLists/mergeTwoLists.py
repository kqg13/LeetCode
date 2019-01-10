# Easy problem 21: Merge Two Sorted Lists


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        merged = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                merged.next = l1
                l1 = l1.next
            else:
                merged.next = l2
                l2 = l2.next
            merged = merged.next
        if l1:
            merged.next = l1
        if l2:
            merged.next = l2
        return dummy.next
