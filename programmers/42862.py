def solution(n, lost, reserve):
    answer = n
    num = []

    for i in range(len(lost)):
        if lost[i] in reserve:
            reserve.remove(lost[i])
            lost[i] = 0

    for x in lost:
        if (x - 1) in reserve:
            reserve.remove(x - 1)
        elif (x + 1) in reserve:
            reserve.remove(x + 1)
        elif 1 <= x <= n:
            num.append(x)
    return answer - len(num)