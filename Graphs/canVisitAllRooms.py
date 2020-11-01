# Graph Problem 841: Keys and Rooms


class Solution:
    def canVisitAllRooms(self, rooms):
        visited = [False] * len(rooms)
        self.dfs(rooms, 0, visited)
        return all(visited)

    def dfs(self, rooms, node, visited):
        visited[node] = True
        for room in rooms[node]:
            if not visited[room]:
                self.dfs(rooms, room, visited)


rooms = [[1, 3], [3, 0, 1], [2], [0]]
s = Solution()
print(s.canVisitAllRooms(rooms))
