# 2019 카카오 개발자 겨울 인턴쉽

def solution(board, moves):
    answer = 0

    bucket = []

    for m in moves:
        for b in board:
            if b[m - 1] != 0:
                bucket.append(b[m - 1])
                b[m - 1] = 0
                break

        for j in range(len(bucket) - 1):
            if len(bucket) > 1:
                length = len(bucket) - 1
                print(bucket[length], bucket[length - 1])
                if bucket[length] == bucket[length - 1]:
                    bucket = bucket[:length - 1]
                    print(bucket)
                    answer += 2

    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print('result', solution(board, moves) * 2)
