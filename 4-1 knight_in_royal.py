here = input()
count = 0
knight_x = [2,1,2,1,-2,-1,-2,-1]
knight_y = [1,2,-1,-2,-1,-2,1,2]

for i in range(8):
    x, y = here[1], here[0]
    if 0 < int(x) + knight_x[i] < 8 and ord('a') <= ord(y) + knight_y[i] <= ord('h') :
        count += 1

print(count)