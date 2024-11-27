# https://leetcode.com/problems/online-stock-span/description/
# https://www.youtube.com/watch?v=slYh0ZNEqSw

class StockSpanner(object):

    def __init__(self):
        self.stack = []  # store pair: (price, span)

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        span = 1

        while self.stack and self.stack[-1][0] < price:
            span += self.stack[-1][1]
            self.stack.pop()

        self.stack.append([price, span])

        return span


# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
param_1 = obj.next(100)
