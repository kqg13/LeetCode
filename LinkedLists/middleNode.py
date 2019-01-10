# Easy problem 876: Middle of the Linked List


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        A = [head]

        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) // 2]

