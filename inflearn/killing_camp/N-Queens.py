# https://leetcode.com/problems/n-queens/description/
from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    arrows = [[-1, 1], [0, 1], [1, 1],
              [-1, 0],         [1, 0],
              [-1, -1], [0, -1], [1, -1]]

    answer = []
    board = [['.' for _ in range(n)] for _ in range(n)]

    def possible_here(new_board, x, y):
        for i, j in arrows:
            nx, ny = x + i, y + j
            while 0 <= nx < n and 0 <= ny < n:
                if new_board[nx][ny] != 'Q':
                    nx += i
                    ny += j
                    continue

                return False
        return True

    def backtrack(new_board, index):
        if index == n:
            answer.append([''.join(arr) for arr in new_board])
            return

        for i in range(n):
            new_board[index][i] = 'Q'
            if possible_here(new_board, index, i):
                backtrack(new_board, index + 1)
            new_board[index][i] = '.'

    backtrack(board[:], 0)

    return answer


print(solveNQueens(8))
