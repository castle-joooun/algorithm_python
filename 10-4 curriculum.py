from collections import deque
import copy

# lecture
lec = int(input())
indegree = [0] * (lec + 1)
time = [0] * (lec + 1)
d = [[] for i in range(lec + 1)]

for i in range(1, lec + 1):
    num = list(map(int, input().split()))

    time[i] = num[0]
    for x in num[1:-1]:
        indegree[i] += 1
        d[x].append(i)


def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    for i in range(1, lec + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in d[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, lec + 1):
        print(result[i])

topology_sort()