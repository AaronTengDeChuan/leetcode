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
		for cur in prices:
			if cur - min_price > max_profit:
				max_profit = cur - min_price
			else:
				if min_price > cur:
					min_price = cur
		return max_profit

solution = Solution()
prices = [7, 6, 4, 3, 1]
print solution.maxProfit(prices)