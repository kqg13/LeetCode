# Easy problem 234: Palindrome Linked List


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# O(1) space
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True

        # Get the middle node
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse first half of linked list
        prev = None
        curr = head
        while curr is not slow:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # Skip middle node if odd # of nodes
        if fast:
            slow = slow.next

        # Check first half and second half
        while prev and slow:
            if prev.val != slow.val:
                return False
            prev = prev.next
            slow = slow.next
        return True


# O(N) space
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst == lst[::-1]
