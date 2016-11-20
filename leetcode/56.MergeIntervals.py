#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Interval(object):
    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        results = []
        if len(intervals) == 0:
            return results
        intervals.sort(key = lambda x:x.start)
        results.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i].start > results[len(results) - 1].end:
                results.append(intervals[i])
            elif intervals[i].end <= results[len(results) - 1].end:
                continue
            else:
                results[len(results) - 1].end = intervals[i].end
        return results

solution = Solution()
intervals = [Interval(2,6),Interval(8,10),Interval(15,18),Interval(1,3)]
for i in solution.merge(intervals):
    print i.start,i.end


