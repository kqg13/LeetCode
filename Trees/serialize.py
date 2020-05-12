from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return 'null'
        q = deque()
        lst = []
        q.append(root)
        while q:
            node = q.popleft()
            if node is None:
                lst.append('null')
            else:
                lst.append(node.val)
                q.append(node.left)
                q.append(node.right)
        self.stripNulls(lst)
        sequence = self.ListToString(lst)
        return sequence

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data == 'null':
            return None
        sequence = self.stringToList(data)
        q = deque()
        root = TreeNode(sequence[0])
        q.append(root)
        sequence_length = len(sequence)
        idx = 1

        while q:
            currentTree = q.popleft()
            if idx == sequence_length:
                continue
            if sequence[idx] != 'null':
                newLeftTree = TreeNode(sequence[idx])
                currentTree.left = newLeftTree
                q.append(newLeftTree)
            idx += 1
            if idx == sequence_length:
                continue
            if sequence[idx] != 'null':
                newRightTree = TreeNode(sequence[idx])
                currentTree.right = newRightTree
                q.append(newRightTree)
            idx += 1
        return root

    def stringToList(self, data):
        lst = list(map(lambda s: 'null' if s == 'null' else int(s), data.split(', ')))
        return lst

    def ListToString(self, lst):
        str_list = ', '.join(map(str, lst))
        return str_list

    def stripNulls(self, lst):
        i = len(lst) - 1
        while lst[i] == 'null':
            del lst[i]
            i -= 1


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.right.left = TreeNode(4)
t.right.right = TreeNode(5)

codec = Codec()
data = codec.serialize(t)
print(data)
# print(codec.stringToList(data))
T = codec.deserialize(data)
print(T.val, T.left.val, T.right.val, T.right.left.val, T.right.right.val)
print(codec.serialize(T))
