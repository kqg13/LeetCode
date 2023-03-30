# 1836: Remove Duplicates From an Unsorted Linked List
from collections import defaultdict


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
    def deleteDuplicatesUnsorted(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d = defaultdict(lambda: 0)
        current = head
        while current:
            d[current.val] += 1
            current = current.next

        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        current = head

        while current:
            if d[current.val] > 1:
                current = current.next
                prev.next = current
            else:
                current = current.next
                prev = prev.next
        return dummy.next


s = Solution()
l1 = ListNode(3, ListNode(2, ListNode(2, ListNode(1, ListNode(3, ListNode(2, ListNode(4)))))))
print(s.deleteDuplicatesUnsorted(l1))
# dummy = ListNode(None)
# dummy.next = head
# prev = dummy
# curr = dummy.next
