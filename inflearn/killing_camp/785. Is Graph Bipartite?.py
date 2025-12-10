from typing import List
from collections import deque


def isBipartite(graph: List[List[int]]) -> bool:
    visited = [-1 for _ in range(len(graph))]
    for i, c in enumerate(visited):
        if c == -1:
            queue = deque([i])
            visited[i] = 0

            while queue:
                cur_v = queue.popleft()
                for next_v in graph[cur_v]:
                    if visited[next_v] == visited[cur_v]:
                        return False
                    elif visited[next_v] == -1:
                        visited[next_v] = visited[cur_v] ^ 1
                        queue.append(next_v)

    return True


print(isBipartite([[4,1],[0,2],[1,3],[2,4],[3,0]]))


def isBipartite(self, graph: List[List[int]]) -> bool:
    # ✅ color의 모든 요소를 -1로 초기화한다.
    color = [-1 for _ in range(len(graph))]
    # ✅ 모든 노드에 대해 반복한다.
    for i, c in enumerate(color):
        # ✅ 만약 color[i] == -1 이라면 탐색을 시작한다.
        if c == -1:
            # ✅ 첫 노드를 0으로 표시하고 큐에 집어넣는다. BFS를 시작한다.
            queue = deque([i])
            color[i] = 0
            while queue:
                cur_v = queue.popleft()
                # ✅ 현재 노드와 연결된 다른 노드들에 대해 반복한다.
                for next_v in graph[cur_v]:
                    # ✅ 만약 color[next] == -1 이라면,
                    if color[next_v] == -1:
                        # ✅ 다음 노드를 현재 노드와 다른 집합에 넣는다.
                        color[next_v] = color[cur_v] ^ 1
                        # ✅ 다음 노드를 큐에 추가한다.
                        queue.append(next_v)
                    # ✅ 아닐 때, 만약 다음 노드가 현재 노드와 같은 집합에 이미 포함되어있으면 false를 리턴한다.
                    elif color[next_v] == color[cur_v]:
                        return False
    return True
