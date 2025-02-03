# Graph Problem 133: Clone Graph

from __future__ import annotations
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: Node) -> Node:
        visited = {}
        if node is None:
            return None
        self.cloneGraphHelper(node, visited)
        return visited[node]

    def cloneGraphHelper(self, node, visited):
        visited[node] = Node(node.val, [])  # key is original node, value is cloned node
        for neighbor in node.neighbors:
            if neighbor not in visited:
                self.cloneGraphHelper(neighbor, visited)
            visited[node].neighbors.append(visited[neighbor])

    def cloneGraphImproved(self, node: Node) -> Node:
        if node is None:
            return None
        visited = {}
        return self.cloneGraphImprovedHelper(node, visited)

    def cloneGraphImprovedHelper(self, node: Node, visited) -> Node:
        if node in visited:
            return visited[node]

        cloned_node = Node(node.val, [])

        visited[node] = cloned_node

        for neighbor in node.neighbors:
            cloned = self.cloneGraphImprovedHelper(neighbor, visited)
            cloned_node.neighbors.append(cloned)

        return cloned_node

    def cloneGraphBfs(self, node: Node) -> Node:
        if node is None:
            return None

        visited = {node: Node(node.val, [])}
        queue = deque([node])

        while queue:
            original_node = queue.popleft()
            cloned_node = visited[original_node]
            for neighbor in original_node.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    queue.append(neighbor)
                # I am not sure what to do here
                cloned_node.neighbors.append(visited[neighbor])

        return visited[node]


nodes = [Node(1, []), Node(2, []), Node(3, []), Node(4, []), Node(5, [])]
nodes[0].neighbors.extend([nodes[1], nodes[3]])
nodes[1].neighbors.extend([nodes[0], nodes[2]])
nodes[2].neighbors.extend([nodes[1], nodes[3], nodes[4]])
nodes[3].neighbors.extend([nodes[0], nodes[2]])

