def dfs(num):
    if num in d:
        if d[-1] == num:
            return
        d.remove(num)
    else:
        d.append(num)

    result = 0
    str_num = str(num)
    for x in str_num:
        result += (int(x) ** p)
    dfs(result)


a, p = map(int, input().split())
d = []

dfs(a)
del d[-1]
print(len(d))
