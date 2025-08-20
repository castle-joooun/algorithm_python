# https://leetcode.com/problems/sudoku-solver/description/
from typing import List


def solveSudoku(board: List[List[str]]) -> None:
    col_set = [set() for _ in range(9)]
    row_set = [set() for _ in range(9)]
    box_set = [set() for _ in range(9)]

    def board_insert(point, str_num):
        i, j = point
        row_set[i].add(str_num)
        col_set[j].add(str_num)
        box_set[(i // 3) + (j // 3 * 3)].add(str_num)

    def board_delete(point, str_num):
        i, j = point
        row_set[i].remove(str_num)
        col_set[j].remove(str_num)
        box_set[(i // 3) + (j // 3 * 3)].remove(str_num)

    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                board_insert([i, j], board[i][j])

    def back(point, new_board):
        x, y = point

        for i in range(9):
            if len(row_set[i]) == 9:
                continue

            for j in range(9):
                current_box_set = box_set[(i // 3) + (j // 3 * 3)]
                if len(col_set[j]) == 9:
                    continue
                if len(current_box_set) == 9:
                    continue
                if board[i][j] != '.':
                    continue

                for num in range(1, 10):
                    str_num = str(num)
                    if str_num not in row_set[i] and \
                            str_num not in col_set[j] and \
                            str_num not in current_box_set:
                        new_board[i][j] = str_num
                        board_insert([i, j], str_num)
                        back([i, j], new_board[:])
                        board_delete([i, j], str_num)
                        new_board[i][j] = '.'

        print(new_board[:])

    back([0, 0], board[:])


print(solveSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                   ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                   [".", "9", "8", ".", ".", ".", ".", "6", "."],
                   ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                   ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                   ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                   [".", "6", ".", ".", ".", ".", "2", "8", "."],
                   [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                   [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
