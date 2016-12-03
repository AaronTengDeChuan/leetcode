#!usr/bin/env python
import sys
class ClassName(object):
    """docstring for ClassName"""
        
class Solution(object):

    def backtracking(self, visited, board, word, row, col, rows, cols):
        if len(word) == 0:
            return True
        direct = [[-1,0],[0,1],[1,0],[0,-1]]
        visited[row][col] = True
        # for i in visited:
        #     print i
        # print 
        for direction in direct:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if 0 <= new_row < rows and 0 <= new_col < cols and visited[new_row][new_col] == False and board[new_row][new_col] == word[0]:
                if(self.backtracking(visited, board, word[1:], new_row, new_col, rows, cols)):
                    return True
        visited[row][col] = False
        return False


    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])
        visited = []
        for i in xrange(rows):
            visited.append([False] * cols)
        for i in xrange(rows):
            for j in xrange(cols):
                if board[i][j] == word[0] and self.backtracking(visited, board, word[1:], i, j, rows, cols):
                    return True
        return False

solution = Solution()
word = raw_input("word:")
board = [
['A', 'B', 'C', 'E'],
['S', 'F', 'C', 'S'],
['A', 'D', 'E', 'E']
]
print solution.exist(board, word)