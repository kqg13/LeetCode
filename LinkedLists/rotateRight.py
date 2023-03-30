# LeetCde 61: Rotate List

# Given the head of a linked list, rotate the list to the right by k places.


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
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None: return None
        if k == 0: return head
        # Get length of linked list
        runner, n = head, 1
        while runner.next:
            runner = runner.next
            n += 1
        # runner now points to end of list
        # adjust k
        k %= n
        # Adjust tail pointer
        runner.next = head
        runner = head
        # Find n - k - 1 node
        for i in range(n - k - 1):
            runner = runner.next
        # Reattach head
        head = runner.next
        # Set middle node to None
        runner.next = None
        return head


s = Solution()
l1, k1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))), 2
l2, k2 = ListNode(0, ListNode(1, ListNode(2))), 4
l3, k3 = ListNode(0, ListNode(1)), 2
l4, k4 = ListNode(0), 0
print(s.rotateRight(l1, k1))
print(s.rotateRight(l2, k2))
print(s.rotateRight(l3, k3))
print(s.rotateRight(l4, k4))
