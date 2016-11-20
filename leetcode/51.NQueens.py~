#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def check(self, k, j, board):
        for i in range(k):
            if board[i] == j or k-i == abs(board[i] - j):
                return False
        return True


    def backtracking(self, results, valuelist, depth, board, n):
        if n == depth:
            results.append(valuelist)
            return 
        for i in range(n):
            if self.check(depth,i, board):
                tmp = '.'*n
                board[depth] = i
                self.backtracking(results, valuelist + [tmp[:i] + 'Q' + tmp[i + 1:]], depth + 1, board, n)

        
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        results = []
        board = [-1 for i in range(n)]
        self.backtracking(results, [], 0, board, n)
        return results
        

solution = Solution()
n = 2
results = solution.solveNQueens(n)
for i in results:
    for j in i:
        print j
    print 

