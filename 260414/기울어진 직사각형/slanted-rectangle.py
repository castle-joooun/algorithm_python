n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
"""
일단 n이 20이하니까 20^6까지 가능함
2중 반복문으로 풀어야하고, 각 값을 돌면서 브루트포스처럼 모든 경우의 수를 검증.
대각선으로 도는 메소드 있고, 중간에 벗어나면 continue 식으로 진행
최대값 비교하면 끝
"""

arrows = [(-1, 1), (-1, -1), (1, -1), (1, 1)]
result = 0

for i in range(n):
    for j in range(n):
        # 한 변(k, m)은 같아야 함
        for k in range(1, n):
            for m in range(1, n):
                total = grid[i][j]
                is_valid = True
                x, y = i, j

                lengths = [k, m, k, m]
                for d in range(4):
                    dx, dy = arrows[d]
                    steps = lengths[d]

                    for s in range(steps):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < n:
                            if not (d == 3 and s == steps - 1):
                                total += grid[nx][ny]
                            x, y = nx, ny
                        else:
                            is_valid = False
                            break

                    if not is_valid:
                        break
                if is_valid and x == i and y == j:
                    result = max(result, total)
print(result)
