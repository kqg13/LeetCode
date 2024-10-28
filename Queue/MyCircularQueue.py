# 622: Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/?envType=company&envId=citadel&favoriteSlug=citadel-three-months

class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next


class MyCircularQueue(object):
    def __init__(self, k):
        """
        :type k: int
        """
        self.capacity = k
        self.count = 0
        self.queue = ListNode()
        self.head = self.queue
        self.last = self.queue
        self.initCircularQueue()

    def initCircularQueue(self):
        current = self.head
        for _ in range(self.capacity - 1):
            node = ListNode()
            current.next = node
            current = current.next
        current.next = self.head

    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.count += 1
        self.last.val = value
        self.last = self.last.next
        return True

    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.count -= 1
        self.head.val = -1
        self.head = self.head.next
        return True

    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.head.val

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        current = self.head
        for i in range(self.count - 1):
            current = current.next
        return current.val

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.count == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.count == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
k1 = 3
obj = MyCircularQueue(k1)
