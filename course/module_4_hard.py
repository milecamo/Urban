# Best Time to Buy and Sell Stock


def profit(*prices):
    profits = [0]
    for i in range(len(prices) - 1):
        profit = max(prices[i + 1:len(prices)]) - prices[i]
        if profit < 0:
            profit = 0
        profits.append(profit)
    profit = max(profits) # not recursive
    buy_on = 0
    sell_on = 0
    if profit:
        buy_on = profits.index(profit)
        sell_on = prices.index(prices[buy_on - 1] + profit, buy_on) + 1
    return profit, buy_on, sell_on


def print_profit(prices, should_be):
    prft, buy_on, sell_on = profit(*prices)
    if prft:
        print(f'Maximum profit for stock prices {prices} is {prft}', prft == should_be,
              f'The best time to buy was on day {buy_on}, and to sell on day {sell_on}')
    else:
        print(f'Maximum profit for stock prices {prices} is {prft}', prft == should_be,
              "In this case, the best choice was not to make any transactions")


print_profit((7, 1, 5, 3, 6, 4), 5)
print_profit((7, 6, 4, 3, 1), 0)
print_profit((7, 8), 1)
print_profit((7,), 0)
print_profit((), 0)
print(f'Maximum profit for empty stock prices is {profit()[0]}')
