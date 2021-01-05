def dfs(n, result):
    result = str(n % 2) + result
    n = n // 2

    if n < 2:
        result = str(n) + result
        print(result)
    else:
        dfs(n, result)


n = int(input())
dfs(n, '')