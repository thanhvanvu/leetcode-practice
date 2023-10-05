def maxProfit(prices):
    maxProf = 0

    # loop through prices
    # check if i > i-1
    # calculate prices[i] - prices[i-1] and add to maxProf
    for i in range(1, len(prices)):
        if prices[i] >= prices[i - 1]:
            maxProf = maxProf + (prices[i] - prices[i - 1])

    return maxProf


prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))
