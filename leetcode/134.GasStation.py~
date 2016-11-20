#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def canCompleteCircuit(self, gas , cost):
        if len(gas) == 0 or len(cost) == 0:
            return -1
        total = 0
        sum = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total += diff
            if sum < 0:
                sum = diff
                start = i
            else:
                sum += diff
        if total < 0:
            return -1
        else:
            return start

    def canCompleteCircuit_origin(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        remain = []
        for i in range(len(gas)):
            remain.append(gas[i] - cost[i])
        dict = {}
        i = 0
        j = 0
        sum = 0
        while j < len(remain):
            if i in dict:
                sum += dict[i][1]
                i = dict[i][0]
            else:
                sum += remain[i]
            if sum < 0:
                dict[j] = [i, sum]
                if len(dict) == len(remain):
                    return -1
                j = i + 1
                sum = 0
                i = (i + 1) % len(remain)
            else:
                i = (i + 1) % len(remain)
                if j == i:
                    return j
        return -1

solution = Solution()
gas = [2,4]
cost = [3,4]
print solution.canCompleteCircuit(gas, cost)

        
        
