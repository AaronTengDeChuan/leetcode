#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:
            return None
        queue = [node]
        dict = {}
        while len(queue) > 0:
            tmp = queue[0]
            del queue[0]
            if tmp.label not in dict:
                dict[tmp.label] = UndirectedGraphNode(tmp.label)
            if len(dict[tmp.label].neighbors) == 0:
                for w in tmp.neighbors:
                    if w.label not in dict:
                        dict[w.label] = UndirectedGraphNode(w.label)
                        queue.append(w)
                    dict[tmp.label].neighbors.append(dict[w.label])
        return dict[node.label]

    def printGraph(self, node):
        result = []
        if node == None:
            return result
        queue = [node]
        dict = []
        while len(queue) > 0:
            tmp = queue[0]
            del queue[0]
            dict.append(tmp.label)
            value = [tmp.label]
            for w in tmp.neighbors:
                value.append(w.label)
                if w.label not in dict:
                    dict.append(w.label)
                    queue.append(w)
            result.append(value)
        return result

solution = Solution()
node = UndirectedGraphNode(0)
p = node 
p.neighbors = [UndirectedGraphNode(1), UndirectedGraphNode(2)]
p.neighbors[0].neighbors = [p.neighbors[1]]
p.neighbors[1].neighbors = [p.neighbors[1]]
node = solution.cloneGraph(node)
result = solution.printGraph(node)
for i in result:
    print i

                


        
