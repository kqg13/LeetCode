# Medium LinkedList problem 19: Remove Nth Node from End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.value = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, k):
        """
        :param head: ListNode
        :param k: int
        :return: ListNode
        """
        first = head
        second = head
        i = 1
        while i <= k:
            second = second.next
            i += 1
        if second is None:
            head = head.next
            return head
        else:
            while second.next is not None:
                second = second.next
                first = first.next
            first.next = first.next.next
        return head


s = Solution()
ll = ListNode(1).next = ListNode(2).next = ListNode(3).next = ListNode(4).next = ListNode(5)
print(s.removeNthFromEnd(ll, 2))
