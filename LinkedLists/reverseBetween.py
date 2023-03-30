# LeetCode 92: Reverse Linked List II

# Given the head of a singly linked list and 2 integers left and right where left <= right,
# reverse the nodes of the list from position left to position right, and return the reversed list.

# Examples:
# head = [1, 2, 3, 4, 5], left = 2, right = 4 ---> [1, 4, 3, 2, 5]
# head = [5], left = 1, right = 1 ---> [5]


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Time: O(N) Space: O(1)
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :param head: ListNode
        :param left: int
        :param right: int
        :return: ListNode
        """
        i, j = 1, 1
        prev, current = None, head

        # Step 1: Move to the correct start position
        while i != left:
            prev = current
            current = current.next
            i += 1
            j += 1

        # Step 2: Lock in the two nodes that will require adjustments
        front, back = prev, current

        # Step 3: Reverse list iteratively
        while j <= right:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            j += 1

        # Step 3: Adjust front and back
        if front:
            front.next = prev
        else:
            head = prev
        back.next = current  # avoid cycle
        return head


# Demo: reference semantics in Java and Python work the same way
list_a = [3, 4, 5]
list_b = list_a
list_b.append(6)
print('list_a: ', list_a, 'list_b: ', list_b)
