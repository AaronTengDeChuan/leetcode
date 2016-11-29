#!usr/bin/env python
import sys 

class Solution(object):
	"""docstring for Solution"""
	def maxProfit(self, prices):
		"""
		:type prices: List[int]
		:rtype: int
		"""
		max_profit = 0
		if len(prices) == 0:
			return max_profit
		min_price = prices[0]
		for i in xrange(len(prices)):
			if i + 1 < len(prices) and prices[i] <= prices[i + 1]:
				continue
			elif prices[i] > min_price:
				max_profit += prices[i] - min_price
			if i + 1 < len(prices):
				min_price = prices[i + 1]
		return max_profit

solution = Solution()
prices = [1, 2, 3, 7, 9, 8]
print solution.maxProfit(prices)