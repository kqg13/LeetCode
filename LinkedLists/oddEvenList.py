# LeetCde 328: Odd Even Linked List

# Given the head of a singly linked list, group all the nodes with odd indices together
# followed by the nodes with even indices, and return the reordered list.
#
# The first node is considered odd, and the second node is even, and so on.
#
# Note that the relative order inside both the even and odd groups should remain as it was in the input.


# Definition for singly-linked list.
class ListNode(object):
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


class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return None
        odd = head
        even = head.next
        even_head = head.next  # Note: head is changing in line 34
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = head.next  # Note: this will give you an infinite loop because head has moved because odd has moved (reference)
        print(head.next.val)
        # odd.next = even_head
        return head

    def reverseList(self, head):
        if head is None: return None
        prev, current = None, head
        while current:
            temp = current.next
            # prev = current
            current.next = prev
            prev = current
            current = temp
        return prev


s = Solution()
l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print(s.oddEvenList(l1))
# l2 = ListNode(0, ListNode(1, ListNode(2)))
# print(l2)
# print(s.reverseList(l2))
