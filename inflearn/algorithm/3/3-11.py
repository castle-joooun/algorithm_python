def check_ho(i, j):
    if j > 2:
        return False
    check = []
    for m in range(j, j + 5):
        check.append(d[i][m])
    reverse = check[::-1]
    if check == reverse:
        return True
    else:
        return False


def check_ver(i, j):
    if i > 2:
        return False
    check = []
    for n in range(i, i + 5):
        check.append(d[n][j])
    reverse = check[::-1]
    if check == reverse:
        return True
    else:
        return False


d = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for i in range(7):
    for j in range(7):
        if check_ver(i, j):
            cnt += 1
        if check_ho(i, j):
            cnt += 1

print(cnt)