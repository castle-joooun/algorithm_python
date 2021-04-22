# 2019 카카오 개발자 겨울 인턴쉽

def solution(s):
    answer = []

    s = s[1: len(s) - 1]
    check = []
    t = []
    for x in s:
        if x in ['{', ',']:
            continue
        elif x == '}':
            check.append(t)
            t = []
        else:
            t.append(x)

    for i in range(len(check)):
        t_len = len(check[i]) - 1
        check[t_len], check[i] = check[i], check[t_len]

    for x in check:
        for y in x:
            if y not in answer:
                answer.append(y)

    return answer


s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
print(solution(s))
# print(solution(s) == [2, 1, 3, 4])
