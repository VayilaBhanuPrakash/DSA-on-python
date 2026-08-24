class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visit = []
        next = []
        next.extend(rooms[0])

        i = 0
        while i <= len(next) - 1:
            visit.append(next[i])
            curr = next[i]
            for j in rooms[curr]:
                if j not in visit:
                    next.append(j)
            i += 1
        for i in range(1,len(rooms)):
            if i not in visit:
                return False
        return True
        