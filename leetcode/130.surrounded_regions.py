#!usr/bin/env python
import sys

class Solution(object):
	def bfs(self, row, col, board):
		m = len(board)
		n = len(board[0])
		#Array:direct represent four diections:up, right, down, left.
		direct = [[-1, 0],[0, 1],[1, 0],[0, -1]]
		queue = [(row, col)]
		while queue:
			temp = queue[0]
			del queue[0]
			if board[temp[0]][temp[1]] == 'O':
				board[temp[0]][temp[1]] = 'E'
			else:
				continue
			for vector in direct:
				row_ex = temp[0] + vector[0]
				col_ex = temp[1] + vector[1]
				if 0 <= row_ex < m and 0 <= col_ex < n and board[row_ex][col_ex] == 'O':
					queue.append((row_ex, col_ex))


	def solve(self, board):
		"""
		:type board: List[List[str]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		m = len(board)
		if m == 0:
			return
		n = len(board[0])
		for i in xrange(n):
			if board[0][i] == 'O':
				self.bfs(0, i, board)
			if board[m - 1][i] == 'O':
				self.bfs(m - 1, i, board)
		for i in xrange(m):
			if board[i][0] == 'O':
				self.bfs(i, 0, board)
			if board[i][n - 1] == 'O':
				self.bfs(i, n - 1, board)
		for i in xrange(m):
			for j in xrange(n):
				if board[i][j] == 'O':
					board[i][j] = 'X'
				elif board[i][j] == 'E':
					board[i][j] = 'O'

solution = Solution()
board = [
['O', 'X', 'X', 'X'],
['X', 'O', 'O', 'X'],
['X', 'X', 'O', 'X'],
['O', 'O', 'X', 'X']
]
solution.solve(board)
for line in board:
	print line
