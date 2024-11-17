# Best Time to Buy and Sell Stock


def profit(*prices):
    profits = [0]
    for i in range(len(prices) - 1):
        profit = max(prices[i + 1:len(prices)]) - prices[i]
        if not profit > 0:
            profit = 0
        profits.append(profit)
    return max(profits)


def print_profit(prices, should_be):
    prft = profit(*prices)
    print(f'Maximum profit for stock prices {prices} is {prft}', prft == should_be)


print_profit((7, 1, 5, 3, 6, 4), 5)
print_profit((7, 6, 4, 3, 1), 0)
print_profit((7,), 0)
print_profit((), 0)
print(f'Maximum profit for empty stock prices is {profit()}')
