# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/
# https://www.youtube.com/watch?v=1pkOgXD63yU

def maxProfit(prices):
    i = 0
    j = 1
    max_profit = 0
    while j < len(prices):
        if prices[j] <= prices[i]:
            i = j
            j += 1
        else:
            max_profit = max(max_profit, prices[j] - prices[i])
            j += 1

    return max_profit


prices = [7, 2, 5, 3, 1, 4, 6]
print(maxProfit(prices))
