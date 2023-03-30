# 2: Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        first_num = self.parseNum(l1)
        second_num = self.parseNum(l2)
        int_sum = first_num + second_num
        sum_list = self.createLL(int_sum)
        self.parseNum(sum_list)
        return sum_list

    def parseNum(self, ll):
        """
        :type ll: ListNode
        :rtype: Integer
        """
        s_num = ""
        while ll:
            s_num += str(ll.val)
            ll = ll.next
        return int(s_num[::-1])

    def createLL(self, num):
        str_sum = str(num)[::-1]
        ll = ListNode(int(str_sum[0]))
        dummy = ll
        for i in range(1, len(str_sum)):
            ll.next = ListNode(int(str_sum[i]))
            ll = ll.next
        return dummy


s = Solution()
ll1 = ListNode(2, ListNode(4, ListNode(9)))
ll2 = ListNode(5, ListNode(6, ListNode(4, ListNode(9))))
s.addTwoNumbers(ll1, ll2)
