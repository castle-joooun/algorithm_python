import sys
input = sys.stdin.readline

n = int(input())
d = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
rotate = [list(map(int, input().split())) for _ in range(m)]


def rotation(x, d):
    row, arrow, num = x
    row -= 1

    for i in range(num):
        temp = d[row][0]
        for j in range(n - 1):
            if arrow == 1:
                d[row][-j] = d[row][-(j + 1)]
            else:
                d[row][j] = d[row][j + 1]
        if arrow == 1:
            d[row][1 - n] = temp
        else:
            d[row][n - 1] = temp
    return d


def isResult(d):
    result = 0
    avg = len(d) // 2
    for i in range(avg + 1):
        arr1 = d[i]
        arr2 = d[n - i - 1]

        if i == 0:
            result += sum(arr1) + sum(arr2)
        elif i == avg:
            result += d[i][avg]
        else:
            result += sum(arr1[i:n - i]) + sum(arr2[i:n - i])

    return result


for x in rotate:
    d = rotation(x, d)

print(isResult(d))