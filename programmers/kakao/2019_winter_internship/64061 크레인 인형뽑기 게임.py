def solution(board, moves):
    answer = 0

    stack = []
    for x in moves:
        for i in range(len(board)):
            if board[i][x - 1] == 0:
                continue

            if len(stack) > 0 and board[i][x - 1] == stack[-1]:
                answer += 1
                stack.pop()
                board[i][x - 1] = 0
                break

            stack.append(board[i][x - 1])
            board[i][x - 1] = 0
            break

    return answer * 2


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))
