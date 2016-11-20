#!usr/bin/env python
#-*-coding:utf-8-*-
import sys

class Solution(object):
    def candy(self, ratings):
        prev = 1
        total = 1
        countDown = 0
        for i in range(1, len(ratings)):
            if ratings[i] >= ratings[i - 1]:
                if countDown > 0:
                    total += countDown * (1 + countDown) / 2
                    if prev <= countDown:
                        total += countDown - prev + 1
                    countDown = 0
                    prev = 1
                if ratings[i] == ratings[i - 1]:
                    prev = 1
                else:
                    prev += 1
                total += prev
            else:
                countDown += 1
        if countDown > 0:
            total += countDown * (1 + countDown) / 2
            if countDown >= prev:
                total += countDown - prev + 1
        return total

    def candy_n_space(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(len(ratings) - 2, -1 , -1):
            if ratings[i] > ratings[i + 1] and candies[i] <= candies[i + 1]:
                candies[i] = candies[i + 1] + 1
        sum = 0
        for i in candies:
            sum += i
        return sum

solution = Solution()
ratings = [4,2,3,4,1]
print solution.candy(ratings)
