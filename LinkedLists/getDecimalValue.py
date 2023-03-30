# LeetCode LinkedList problem #1290: Convert Binary Number in a Linked List to Int

# Given head which is a reference node to a singly-linked list. The value of each
# node in the linked list is either 0 or 1. The linked list holds the binary
# representation of a number. Return the decimal value of the # in the linked list.

# Examples:
# head1 = [1, 0, 1] --> 5
# head2 = [0] --> 0
# head3 = [1] ---> 1


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseLinkedList(self, head: ListNode) -> ListNode:
        result = None
        while head:
            current = head
            head = head.next
            current.next = result
            result = current
        return result

    def getDecimalValue(self, head: ListNode) -> int:
        reversedHead = self.reverseLinkedList(head)
        result, exp = 0, 0
        while reversedHead is not None:
            result += (2 ** exp) * reversedHead.val
            exp += 1
            reversedHead = reversedHead.next
        return result


s = Solution()
head1 = ListNode(0)
head1.next = ListNode(1)
head1.next.next = ListNode(1)
print(s.getDecimalValue(head1))
