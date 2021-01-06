import sys

def dfs(v, boll):
    for _ in range(1):
        if v == n + 1:
            result1 = []
            result2 = []
            for i in range(1, n + 1):
                if do_or_not[i] == 1:
                    result1.append(d[i - 1])
                else:
                    result2.append(d[i - 1])

            if sum(result1) == sum(result2):
                print('YES')
                sys.exit(0)
        else:
            do_or_not[v] = 1
            dfs(v + 1, boll)
            do_or_not[v] = 0
            dfs(v + 1, boll)
    else:
        if v == 1 and do_or_not[v] == 0:
            print('NO')


n = int(input())
d = list(map(int, input().split()))
do_or_not = [0] * (n + 1)
check = 0
dfs(1, check)

print('YES' if check == 1 else 'NO')
