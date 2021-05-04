def dfs(string):
    cnt1 = 0
    cnt2 = 0

    idx = 0
    result = ''

    while cnt1 != cnt2:
        if idx == len(string):
            break

        if string[idx] == '(':
            cnt1 += 1
        else:
            cnt2 += 1
        idx += 1

    return string[:idx], string[idx:]


def solution(p):
    answer = ''

    u, v = dfs(p)

    stack = [u[0]]
    for i in range(1, len(u)):
        stack.append(u[i])
        if stack[-1] == ')' and stack[-2] == '(':
            stack = stack[:-2]

    if len(stack) == 0:
        answer += u
        while len(v) != 0:
            dfs(v)
    else:
        temp = '('
        temp += dfs(v)

    return answer
