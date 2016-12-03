#!usr/bin/env python
import sys

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
	"""
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        queue = [beginWord]
        layer_size = 1
        layer_num = 1
        str_len = len(beginWord)
        wordList_size = len(wordList)
        while queue:
            tmp = queue[0]
            del queue[0]
            layer_size -= 1
            similar_word_num = 0
            for i in xrange(str_len):
                for j in xrange(26):
                    next_word = tmp[:i] + chr(ord('a') + j) + tmp[i + 1:]
                    if next_word == endWord:
                        return layer_num + 1
                    if next_word in wordList:
                        queue.append(next_word)
                        wordList.remove(next_word)
            if layer_size == 0:
                layer_size = len(queue)
                layer_num += 1
        return 0

solution = Solution()
beginWord = "hit"
endWord = "abc"
wordList = ["hot", "dot", "dog", "lot", "log"]
print solution.ladderLength(beginWord, endWord, wordList)
