841  Keys and Rooms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # N = len(rooms)
        # room = [-1]*N
        # queue = [0]
        # while queue:
        #     x = queue.pop()
        #     if room[x] == 1:
        #         continue
        #     room[x] = 1
        #     queue.extend(rooms[x])
        # return sum(room) == N
        N = len(rooms)
        room = [-1]*N
        queue = [0]
        while queue:
            x = queue.pop()
            if room[x] == 1:
                continue
            room[x] = 1
            for r in rooms[x]:
                if room[r] == -1:
                    queue.append(r)
        # print(room)
        return sum(room) == N