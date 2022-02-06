"""
### 💡 풀이 순서

> 연속되어 연결된 숫자들을 찾아 카운트하고 단지수도 늘려가면 될 것  같다.
>

### 🏭 알고리즘

> DFS
> BFS는 한 번 해봤으니 DFS로 도전해보았다
>

### ⚙️ 시간 복잡도 분석

> n^2...
n은 최대 25, 25^2는 625
625^2니까 대략 40만이라 가능하다.
>

### ‼️ 문제에서 중요한 부분

> 방문여부를 체크해가면서 단지수를 세고, 단지가 끝나면 append하여 리스트로 나타내기 or 바로 print로 출력하기
>
"""


from sys import stdin


def dfs(x, y, cnt):
    visited[x][y] = True
    global nums
    if d[x][y] == 1:
        nums += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and d[nx][ny] == 1:
                dfs(nx, ny, cnt)


n = int(input())
d = [[0] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

for i in range(n):
    line = stdin.readline().strip()
    for j, b in enumerate(line):
        d[i][j] = int(b)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
nums = 0
cnt = 1
numlist = []
for a in range(n):
    for b in range(n):
        if d[a][b] == 1 and not visited[a][b]:
            dfs(a, b, cnt)
            numlist.append(nums)
            nums = 0

print(len(numlist))
for x in sorted(numlist):
    print(x)
