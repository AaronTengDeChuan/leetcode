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
        while i < len(intervals):
            if newInterval.end < intervals[i].start:
                intervals.insert(i, newInterval)
                return intervals
            elif newInterval.start > intervals[i].end:
                i += 1
                continue
            else:
                if newInterval.start > intervals[i].start:
                    newInterval.start = intervals[i].start
                if newInterval.end < intervals[i].end:
                    newInterval.end = intervals[i].end
                intervals.remove(intervals[i])

        intervals.append(newInterval)
        return intervals
        


solution = Solution()
newInterval = Interval(19,19)
intervals = [Interval(1,3), Interval(4,6), Interval(8,10), Interval(15,18)]
for i in solution.insert(intervals, newInterval):
    print i.start,i.end

