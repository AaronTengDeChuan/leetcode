#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        result = []
        if n == 0:
            return result
        for i in range(n + 1):
            result.append([None])
        for i in range(n + 1):
            result[0].append([None])
        for i in range(1, n + 1):
            result[1].append([TreeNode(i)])
        for i in range(2, n + 1):
            for j in range(1, n + 2 - i):
                tmp = []
                for k in range(j, j + i ):
                    for l in result[k - j][j]:
                        for m in result[j + i - 1 - k][k + 1]:
                            root = TreeNode(k)
                            root.left = l
                            root.right = m
                            tmp.append(root)
                result[i].append([item for item in tmp])
        return result[n][1]
        
solution = Solution()
result = solution.generateTrees(int(raw_input("n = ")))
print len(result)
