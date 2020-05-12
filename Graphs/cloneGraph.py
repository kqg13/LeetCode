# Graph Problem 133: Clone Graph


# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}
        if node is None: return None
        self.cloneGraphHelper(node, visited)
        return visited[node]

    def cloneGraphHelper(self, node, visited):
        visited[node] = Node(node.val, [])  # key is original node, value is cloned node
        for neighbor in node.neighbors:
            if neighbor not in visited:
                self.cloneGraphHelper(neighbor, visited)
            visited[node].neighbors.append(visited[neighbor])


nodes = [Node(1, []), Node(2, []), Node(3, []), Node(4, []), Node(5, [])]
nodes[0].neighbors.extend([nodes[1], nodes[3]])
nodes[1].neighbors.extend([nodes[0], nodes[2]])
nodes[2].neighbors.extend([nodes[1], nodes[3], nodes[4]])
nodes[3].neighbors.extend([nodes[0], nodes[2]])
s = Solution()
print(s.cloneGraph(nodes[0]))
