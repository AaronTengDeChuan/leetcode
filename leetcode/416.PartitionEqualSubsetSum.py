#!usr/bin/env python
import sys

class Solution(object):
	def canPartition(self, nums):
		"""
		:type nums:List[int]
		:rtype: bool
		"""
		sum = 0
		for i in nums:
			sum += i
		if sum % 2 == 1:
			return False
		sum = sum / 2
		dp = [False] * (sum + 1)
		dp[0] = True
		for i in nums:
			for j in xrange(sum, i - 1 , -1):
				dp[j] |= dp[j - i]
			if dp[sum]:
				return True
		return False

solution = Solution()
nums = [1, 5, 11, 5]
print solution.canPartition(nums)
