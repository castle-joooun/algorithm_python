map_size = list(map(int, input().split()))
x, y, arrow = map(int, input().split())
move_map = []
move_x = [0, -1, 0, 1]
move_y = [-1, 0, 1, 0]
count = 0
arrow_count = 0

# map_size[0] is row, map_size[1] is column
for i in range(map_size[0]):
    move_map.append(list(map(int, input().split())))

# start spot
count += 1

while arrow_count != 4:
    if 0 == move_map[y + move_y[arrow]][x + move_x[arrow]]:
        count += 1
        x += move_x[arrow]
        y += move_y[arrow]
    else:
        if arrow >= 1:
            arrow -= 1
        else:
            arrow = 3
        arrow_count += 1

print(count)
