def maxProfit(prices):
    maxProf = 0

    # loop through prices
    # check if i > i-1
    # calculate prices[i] - prices[i-1] and add to maxProf
    for i in range(1, len(prices)):
        if prices[i] >= prices[i - 1]:
            maxProf = maxProf + (prices[i] - prices[i - 1])

    return maxProf


def maxProfit_practice(prices):
    # do not need 2 pointers
    # just loop through prices
    # check if i > i-1
    # calculate prices[i] - prices[i-1] and add to maxProf
    maxPro = 0
    for i in range(1, len(prices)):
        if prices[i] >= prices[i - 1]:
            profit = prices[i] - prices[i - 1]
            maxPro += profit

    return maxPro


prices = [7, 1, 5, 3, 6, 4]
print(maxProfit_practice(prices))
