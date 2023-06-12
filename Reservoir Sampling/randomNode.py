# 382: Linked List Random Node
# https://leetcode.com/problems/linked-list-random-node/

import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        n = 1
        curr_selection = self.head.val
        curr = self.head.next
        while curr is not None:
            n += 1
            if self.doSelection(n):
                curr_selection = curr.val
            curr = curr.next
        return curr_selection

    def doSelection(self, n):
        rnd = random.randint(1, n)
        return rnd == 1


# Your Solution object will be instantiated and called as such:
head = ListNode(10, ListNode(1, ListNode(10, ListNode(20, ListNode(100)))))
obj = Solution(head)

for _ in range(50):
    param_1 = obj.getRandom()
    print(param_1)
