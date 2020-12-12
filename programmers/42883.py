def solution(number, k):
    answer = ''
    idx = []
    sn = str(number)

    for i in range(k):
        idx.append(i)

    for i in range(len(sn)):
        for j in range(k):
            if i not in idx and int(sn[i]) < int(idx[j]):
                idx[j] = i

    for i in range(len(sn)):
        if i not in idx:
            answer += sn[i]

    return answer