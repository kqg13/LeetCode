# 2807:  Insert Greatest Common Divisors in Linked List
# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

import math


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


class Solution:
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy_node = ListNode(-1)
        dummy_node.next = head

        while head.next:
            first_val = head.val
            second_val = head.next.val if head.next else first_val
            gcd = self.getGcd(first_val, second_val)
            gcd_node = ListNode(gcd)
            # insert
            next_node = head.next
            gcd_node.next = next_node
            head.next = gcd_node
            # advance
            head = next_node
        return dummy_node.next

    def getGcd(self, num1, num2):
        if not num2:
            num2 = num1
        return math.gcd(num1, num2)


s = Solution()
l1 = ListNode(18, ListNode(6, ListNode(10, ListNode(3))))
l2 = ListNode(7)
print(s.insertGreatestCommonDivisors(l2))
