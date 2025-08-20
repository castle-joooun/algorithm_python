# https://leetcode.com/problems/keys-and-rooms/description/
from typing import List


def canVisitAllRooms(rooms: List[List[int]]) -> bool:
    keys = [0]
    visited = [False] * len(rooms)

    while len(keys) != 0:
        key = keys.pop()
        if visited[key]:
            continue

        visited[key] = True
        keys += rooms[key]

    return all(visited)


print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))

