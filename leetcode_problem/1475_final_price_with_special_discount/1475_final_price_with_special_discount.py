# https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/description/
# this problem is similar to 739: daily temperature

def finalPrices(prices):
    stack = []  # pair: [price, index]

    for i, price in enumerate(prices):
        while stack and price <= stack[-1][0]:
            pr, index = stack.pop()
            pr = pr - price

            prices[index] = pr

        stack.append([price, i])

    return prices


prices = [10, 1, 1, 6]
print(finalPrices(prices))
