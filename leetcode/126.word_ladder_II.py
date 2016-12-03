#usr/bin/env python
import sys

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordlist: Set[str]
        :rtype: List[List[int]]
        """
        results = [[beginWord]]
        results_real = []
        queue = [(beginWord, 0)]
        queue_single = [beginWord]
        layer_size = 1
        str_len = len(beginWord)
        last_layer = False
        while queue:
            tmp = queue[0]
            del queue[0]
            del queue_single[0]
            if tmp[0] in wordList:
                wordList.remove(tmp[0])
            layer_size -= 1
            for i in xrange(str_len):
                for j in xrange(26):
                    tmp_ele = chr(ord('a') + j)
                    if tmp[0][i] == tmp_ele:
                        continue
                    next_word = tmp[0][:i] + tmp_ele + tmp[0][i + 1:]
                    if next_word == endWord:
                        results[tmp[1]].append(endWord)
                        results_real.append(results[tmp[1]])
                        last_layer = True
                    if next_word in wordList and next_word not in queue_single:
                        new_path = [k for k in results[tmp[1]]]
                        new_path.append(next_word)
                        results.append(new_path)
                        queue.append((next_word, len(results) - 1))
            # print "Begin:"
            # for i in results:
            #     print i
            # print "End"
            if layer_size == 0:
                if last_layer:
                    break
                layer_size = len(queue)
                queue_single = [k for k in queue]
        return results_real

solution = Solution()
beginWord = "red"
endWord = "tax"
wordList = ["ted", "tad", "tex", "rex"]
for i in solution.findLadders(beginWord, endWord, wordList):
    print i