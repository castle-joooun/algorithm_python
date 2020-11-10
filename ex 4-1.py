num = int(input())
move = list(input().split())
x, y = 1, 1

for arrow in move:
    if arrow == "U" and y != 1:
        y -= 1
    if arrow == "D" and y != num:
        y += 1
    if arrow == "L" and x != 1:
        x -= 1
    if arrow == "R" and x != num:
        x += 1

print(y, x)