def check_sdoku(d):
    for n in range(3):
        for m in range(3):
            check = [False for _ in range(10)]
            check[0] = True

            for i in range(n * 3, (n + 1) * 3):
                for j in range(m * 3, (m + 1) * 3):
                    if check[d[i][j]]:
                        return False
                    check[d[i][j]] = True
    return True


d = [list(map(int, input().split())) for _ in range(9)]

if check_sdoku(d):
    print('YES')
else:
    print('NO')