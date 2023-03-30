# Graph Problem 841: Keys and Rooms


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        nRooms = len(rooms)
        visited = [False] * nRooms
        self.canVisitHeloer(rooms, 0, visited)
        return all(visited)

    def canVisitHeloer(self, rooms, roomNode, visited):
        visited[roomNode] = True
        for room in rooms[roomNode]:
            if not visited[room]:
                self.canVisitHeloer(rooms, room, visited)


rooms = [[1, 3], [3, 0, 1], [2], [0]]
s = Solution()
print(s.canVisitAllRooms(rooms))
