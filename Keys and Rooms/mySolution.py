def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    l = [0 for i in range(len(rooms))]
    l[0] = 1

    def dfs(rooms, i, l):
        l[i] = 1
        for key in rooms[i]:
            if(l[key] == 0):
                dfs(rooms, key, l)
        return
    dfs(rooms, 0, l)
    if 0 in l:
        return False
    return True
