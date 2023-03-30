# LeetCde 24: Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem w/o modifying the vals in the list's nodes (only nodes themselves may be changed)


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
    def swapPairs(self, head):
        pass


s = Solution()
l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
