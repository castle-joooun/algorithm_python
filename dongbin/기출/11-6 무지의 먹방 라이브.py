def solution(foods, k):
    idx = 0

    while k != 0:
        if foods[idx] != 0:
            foods[idx] -= 1
            k -= 1
        idx = 0 if idx == len(foods) - 1 else idx + 1

    return -1 if max(foods) == 0 else idx + 1


foods = [3, 1, 2]
k = 5
print(solution(foods, k))
