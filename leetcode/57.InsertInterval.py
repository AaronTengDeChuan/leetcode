#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Interval(object):
    def __init__(self, s = 0, e = 0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        i = 0
        results = []
        while i < len(intervals) and intervals[i].start < newInterval.start:
            results.append(intervals[i])
            i += 1
        intervals.insert(i, newInterval)
        for j in range(i, len(intervals)):
            if len(results) == 0:
                results.append(intervals[i])
            elif intervals[j].start > results[len(results) - 1].end:
                results.append(intervals[j])
            elif intervals[j].end <= results[len(results) - 1].end:
                continue
            else:
                results[len(results) - 1].end = intervals[j].end
        return results


solution = Solution()
newInterval = Interval(0,0)
intervals = [Interval(1,3), Interval(4,6), Interval(8,10), Interval(15,18)]
for i in solution.insert(intervals, newInterval):
    print i.start,i.end

