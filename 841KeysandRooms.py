841  Keys and Rooms

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = [0]
        i = 0
        cache = []
        while queue:
            key = queue.pop()
            if key not in cache:
                cache.append(key)
            else:
                continue
            while rooms[key]:
                keyNew = rooms[key].pop()
                queue.append(keyNew)
        # print(cache)
        return len(cache) == len(rooms)
                