#usr/bin/env python
import sys

class Solution(object):
    def generatePaths(self, dict, beginWord, endWord, results, result):
        if beginWord == endWord:
            results.append(result)
        if beginWord not in dict:
            return 
        for cur in dict[beginWord]:
            self.generatePaths(dict, cur, endWord, results, [cur] + result)



    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        results = []
        str_len = len(beginWord)
        cur_layer = set([beginWord])
        wordList.add(endWord)
        if beginWord in wordList:
            wordList.remove(beginWord)
        dict = {}
        next_layer = set([])
        while endWord not in cur_layer or wordList:
            for cur in cur_layer:
                for i in xrange(str_len):
                    for j in "abcdefghijklmnopqrstuvwxyz":
                        if cur[i] == j:
                            continue
                        tmp = cur[:i] + j + cur[i + 1:]
                        if tmp in wordList:
                            next_layer.add(tmp)
                            if tmp in dict:
                                dict[tmp].append(cur)
                            else:
                                dict[tmp] = [cur]
            for cur in next_layer:
                wordList.remove(cur)
            cur_layer = next_layer
            next_layer = set([])
            if len(cur_layer) == 0:
                break
        self.generatePaths(dict, endWord, beginWord, results, [endWord])
        return results

solution = Solution()
beginWord = "a"
endWord = "c"
wordList = set(["a", "b", "c"])
for i in solution.findLadders(beginWord, endWord, wordList):
    print i

        