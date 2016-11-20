#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            tmp = []
            for j in range(9):
                if board[i][j] != '.' and board[i][j] in tmp:
                    return False
                else:
                    tmp.append(board[i][j])
            tmp = []
            for j in range(9):
                if board[j][i] != '.' and board[j][i] in tmp:
                    return False
                else:
                    tmp.append(board[j][i])
            tmp = []
            row = i / 3
            row *= 3
            col = i % 3
            col *= 3
            for j in range(3):
                for k in range(3):
                    if board[row + j][col + k] != '.' and board[row + j][col + k] in tmp:
                        return False
                    else:
                        tmp.append(board[row + j][col + k])
        return True

solution = Solution()
board = [['5','3','.','.','7','.','.','.','.'],
         ['6','.','.','8','9','5','.','.','.'],
         ['.','9','8','.','.','.','.','6','.'],
         ['8','.','.','.','6','.','.','.','3'],
         ['4','.','.','8','.','3','.','.','1'],
         ['7','.','.','.','2','.','.','.','6'],
         ['.','6','.','.','.','.','2','8','.'],
         ['.','.','.','4','1','9','.','.','5'],
         ['.','.','.','.','8','.','.','7','9']]
print solution.isValidSudoku(board)
