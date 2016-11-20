#usr/bin/env python
#-*-coding":utf-8-*-
import sys

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        results = []
        for i in range(n):
            result = []
            for j in range(n):
                result.append(0)
            results.append(result)
        direct = 0
        r = [0,1,0,-1]
        c = [1,0,-1,0]
        cur = 1
        visitedRows = 0
        visitedCols = 0
        startr = 0
        startc = 0
        cur_step = 0
        while True:
            step = 0
            if r[direct] != 0:
                step = n - visitedRows
            else:
                step = n - visitedCols
            if step == 0:
                break
            print startr,startc
            results[startr][startc] = cur
            cur += 1
            cur_step += 1
            if cur_step == step:
                if r[direct] != 0:
                    visitedCols += 1
                else:
                    visitedRows += 1
                direct += 1
                direct %= 4
                cur_step = 0
            startr += r[direct]
            startc += c[direct]
            
        return results
solution = Solution()
n = 4
for i in solution.generateMatrix(n):
    print i

