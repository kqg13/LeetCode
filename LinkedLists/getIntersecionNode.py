# Easy problem 160: Intersection of Two Linked Lists

# Write a program to find the node at which the intersection of two singly
# linked lists begins.


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        a = headA
        b = headB

        while a is not b:
            if a:
                a = a.next
            else:
                a = headB

            if b:
                b = b.next
            else:
                b = headA
        return a  # b can also be returned
