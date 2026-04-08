n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
# 최대가 20이하니까, 20^6 이하로 풀면 되겠음.
# N^6.
# 2중 For 돌면서 0-2까지 도는 2중 for를 만듬.
# 0인 경우를 다 찾으면 그게 max이고, 전역변수에 max_count랑 비교하면 될듯
answer = 0
def check(x, y):
    temp = 0

    for i in range(3):
        for j in range(3):
            if grid[x + i][y + j] == 0:
                temp += 1
    return temp
            


for i in range(n - 2):
    for j in range(n - 2):
        answer = max(check(i, j), answer)

if n == 3:
    print(check(0, 0))
else:
    print(answer)


