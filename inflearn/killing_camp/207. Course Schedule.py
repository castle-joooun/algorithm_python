# https://leetcode.com/problems/course-schedule/description/
from typing import List
from collections import deque

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    visited = []
    graph = [[] for _ in range(numCourses)]
    indegree = [0] * numCourses

    for v, u in prerequisites:
        graph[u].append(v)
        indegree[v] += 1

    q = deque()
    for v in range(numCourses):
        if indegree[v] == 0:
            q.append(v)

    while q:
        cur_v = q.popleft()
        visited.append(cur_v)

        for next_v in graph[cur_v]:
            indegree[next_v] -= 1

            if indegree[next_v] == 0:
                q.append(next_v)

    return len(visited) == numCourses


print(canFinish(2, [[1, 0]]))
