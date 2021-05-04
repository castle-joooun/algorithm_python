import copy


def solution(key, lock):
    answer = True

    new_lock = [[0] * len(lock) ** 2 for _ in range(len(lock) ** 2)]
    for i in range(len(lock)):
        for j in range(len(lock)):
            new_lock[len(lock) + i][len(lock) + j] = lock[i][j]

    check = True
    while check:
        copy_lock = copy.deepcopy(new_lcok)
        for i in range(1, len(key) * 2):
            for j in range(1, len(key) * 2):
                copy_lock[i][j] += key[i][j]

    return answer


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))
