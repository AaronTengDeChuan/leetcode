#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def check(self, k, j, board):
        for i in range(k):
            if board[i] == j or k-i == abs(board[i] - j):
                return False
        return True

    def totalNQueens(self, n):
        row = 0
        col = 0
        result = 0
        board = [-1 for i in range(n)]
        while row < n:
            while col < n:
                if self.check(row, col, board):
                    board[row] = col
                    col = 0
                    break
                else:
                    col += 1
            if board[row] == -1:
                if row == 0:
                    break
                row -= 1
                col = board[row] + 1
                board[row] = -1
                continue
            if row == n-1:
                result += 1
                col = board[row] + 1
                board[row] = -1
                continue
            row += 1
        return result

solution = Solution()
n = 4
print solution.totalNQueens(n)
