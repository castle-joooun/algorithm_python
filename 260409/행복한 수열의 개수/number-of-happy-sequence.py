n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 시간복잡도는 N^2가 될듯
# 2중 for 돌면서 각 원소 확인하고, 자기 자신과 연속으로 나오면 그 개수를 카운팅,
# 그 카운팅이 m보다 크면 answer + 1 해주자.

answer = 0
for i in range(n):
    row_count = [1]
    col_count = [1]

    before_row = grid[i][0]
    before_col = grid[0][i]
    # check row
    for j in range(1, n):
        if m - row_count[-1] <= n - j + 1:
            if before_row == grid[i][j]:
                row_count[-1] += 1
            else:
                before_row = grid[i][j]
                row_count.append(1)

        if m - col_count[-1] <= n - j + 1:
            if before_col == grid[j][i]:
                col_count[-1] += 1
            else:
                before_col = grid[j][i]
                col_count.append(1)

    if max(row_count) >= m:
        answer += 1
    if max(col_count) >= m:
        answer += 1

print(answer)