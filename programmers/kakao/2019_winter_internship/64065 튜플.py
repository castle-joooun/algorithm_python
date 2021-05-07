def solution(s):
    answer = []

    d = [0] * 100001

    arr = list(filter(None, s.split('{')))
    for x in arr:
        num = ''
        for string in x:
            if string in [',', '}']:
                if num != '':
                    d[int(num)] += 1
                    num = ''
                continue

            num += string

    while max(d) != 0:
        max_num = d.index(max(d))
        d[max_num] = 0
        answer.append(max_num)

    return answer


print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
