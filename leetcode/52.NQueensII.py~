#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def check(self, k, j, board):
        for i in range(k):
            if board[i] == j or k-i == abs(board[i] - j):
                return False
        return True


    def backtracking(self, result, depth, board, n):
        if n == depth:
            result[0] +=1
            return 
        for i in range(n):
            if self.check(depth,i, board):
                board[depth] = i
                self.backtracking(result, depth + 1, board, n)

        
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [0]
        board = [-1 for i in range(n)]
        self.backtracking(result, 0, board, n)
        return result[0]
        

solution = Solution()
n = 4
print solution.totalNQueens(n)

