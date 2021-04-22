n = int(input())
arr = input().split()
data = [[0] for i in range(n)] * n

x = 0
y = 0

for arrow in arr:
    if arrow == 'U' and y - 1 >= 0:
        y -= 1
    if arrow == 'D' and y + 1 <= n:
        y += 1
    if arrow == 'L' and x - 1 >= 0:
        x -= 1
    if arrow == 'R' and x + 1 <= n:
        x += 1

print(y + 1, x + 1)
