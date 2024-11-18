# 109: Convert Sorted List to Binary Search Tree
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        self.tree_list = self.convertLinkedList(head)
        root = self.sortedListToBSTHelper(0, len(self.tree_list) - 1)
        return root

    def sortedListToBSTHelper(self, lo, hi):
        if lo > hi:
            return None

        mid = (lo + hi) // 2
        mid_val = self.tree_list[mid]

        left = self.sortedListToBSTHelper(lo, mid - 1)
        right = self.sortedListToBSTHelper(mid + 1, hi)
        root = TreeNode(mid_val, left, right)
        return root

    def convertLinkedList(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        converted = list()
        current = head
        while current:
            converted.append(current.val)
            current = current.next
        return converted


s = Solution()
head1 = ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
head2 = None

t1 = s.sortedListToBST(head1)
print(t1.val)

