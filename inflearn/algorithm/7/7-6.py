def dfs(idx, solv):
    if secret[idx] == '0':
        return
    if idx > len(secret) - 1:
        return
    if idx == len(secret) - 1:
        if solv not in result:
            result.append(solv)
    else:
        dfs(idx + 1, solv + d[int(secret[idx])])
        if secret[idx + 1] != '.' and int(secret[idx] + secret[idx + 1]) <= 26:
            dfs(idx + 2, solv + d[int(secret[idx] + secret[idx + 1])])


secret = input() + '.'
d = [''] + [chr(i) for i in range(ord('A'), ord('Z') + 1)]
result = []
dfs(0, '')

result.sort()
for x in result:
    print(x)
print(len(result))