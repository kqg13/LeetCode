# Easy problem 876: Middle of the Linked List


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val, next=None):
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
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        A = [head]

        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) // 2]


s = Solution()
l1 = ListNode(3, ListNode(2, ListNode(2, ListNode(1, ListNode(3, ListNode(2, ListNode(4)))))))
print(l1)

