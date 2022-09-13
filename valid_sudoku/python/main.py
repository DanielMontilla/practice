from typing import List

# https://leetcode.com/problems/product-of-array-except-self/


def isValidSudoku(board: List[List[str]]) -> bool:

    # checking rows
    for row in board:
        nums = set()
        for n in row:
            if n != '.':
                if n in nums:
                    return False
                else:
                    nums.add(n)

    # checking columns
    for col in range(9):
        nums = set()
        for row in range(9):
            n = board[row][col]
            if n != '.':
                if n in nums:
                    return False
                else:
                    nums.add(n)

    # checking sub matrix
    for col in range(3):
        for row in range(3):
            nums = set()

            for i in range(3):
                for j in range(3):
                    n = board[row * 3 + j][col * 3 + i]
                    if n != '.':
                        if n in nums:
                            return False
                        else:
                            nums.add(n)

    return True

"""
    Runtime: 115 ms, faster than 61.09% of Python3 online submissions for Valid Sudoku.
    Memory Usage: 13.9 MB, less than 35.48% of Python3 online submissions for Valid Sudoku.
"""

# Inputs:
board_1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

board_2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

if __name__ == '__main__':
    res = isValidSudoku(board_2)
    print(res)
