#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def searchValidNumber(self, board,position):
        tmp = ['1','2','3','4','5','6','7','8','9']
        for i in range(9):
            if board[position[0]][i] != '.':
                tmp.remove(board[position[0]][i])
        for i in range(9):
            if board[i][position[1]] != '.' and board[i][position[1]] in tmp:
                tmp.remove(board[i][position[1]])
        row = position[0] - position[0] % 3
        col = position[1] - position[1] % 3
        for i in range(3):
            for j in range(3):
                if board[row + i][col + j] != '.' and board[row + i][col + j] in tmp:
                    tmp.remove(board[row + i][col + j])
        return tmp

    def solveSudoku(self, board):
        self.solve(board)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        flag = False
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    flag = True
                    break
            if flag:
                break
        if not flag:
            return True

        tmp = self.searchValidNumber(board,[i,j])
        if len(tmp) == 0:
            return False
        else:
            for k in tmp:
                board[i][j] = k
                if not self.solve(board):
                    board[i][j] = '.'
                else:
                    return True
            return False


        

solution = Solution()
board = [['5','3','.','.','7','.','.','.','.'],
         ['6','.','.','1','9','5','.','.','.'],
         ['.','9','8','.','.','.','.','6','.'],
         ['8','.','.','.','6','.','.','.','3'],
         ['4','.','.','8','.','3','.','.','1'],
         ['7','.','.','.','2','.','.','.','6'],
         ['.','6','.','.','.','.','2','8','.'],
         ['.','.','.','4','1','9','.','.','5'],
         ['.','.','.','.','8','.','.','7','9']]
solution.solveSudoku(board)
print board
