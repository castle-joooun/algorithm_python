point = input()
x, y = ord(point[0]), int(point[1])

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

result = 0
for i in range(8):
    xx = x + dx[i]
    yy = y + dy[i]

    if ord('a') <= xx <= ord('h') and 1 <= yy <= 8:
        result += 1

print(result)
