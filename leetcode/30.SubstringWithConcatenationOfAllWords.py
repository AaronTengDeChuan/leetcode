#!/usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        word_len = len(words[0])
        words_size = len(words)
        words_dict = {}
        result = []
        for word in words:
            words_dict[word] = 0
	for word in words:
            words_dict[word] += 1
	#print words_dict
        counting = {}
        for i in range(0,len(s) - words_size*word_len + 1):
            counting.clear()
            for j in range(0,words_size):
		word = s[i + j*word_len:i + j*word_len+word_len]
                if not words_dict.has_key(word):
                    break
                elif counting.has_key(word):
		    if counting[word] >= words_dict[word]:
                        break
	 	    else:
                        counting[word] += 1
                else:
                    counting[word] = 1
            else:
                #如果for循环未被break终止，则执行else块中的语句
                result.append(i)
        return result

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","good"]
solution = Solution()
print solution.findSubstring(s,words)







