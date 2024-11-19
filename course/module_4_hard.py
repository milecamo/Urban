# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

def profit(prices):
    profits = [0]
    for i in range(len(prices) - 1):
        profits.append(max(prices[i + 1:len(prices)]) - prices[i])
    max_profit = max(profits)
    buy_on = -1
    sell_on = -1
    if max_profit:
        buy_on = profits.index(max_profit) - 1
        sell_on = prices.index(prices[buy_on] + max_profit, buy_on)
    return max_profit, buy_on, sell_on


def print_profit(prices, should_be, should_buy_on=-1, should_sell_on=-1):
    max_profit, buy_on, sell_on = profit(prices)
    print(f'Profit for stock prices {prices} was {max_profit} ',
          (max_profit, buy_on, sell_on) == (should_be, should_buy_on, should_sell_on))
    if max_profit:
        print(f'The best time to buy was on day {buy_on + 1} (price = {prices[buy_on]}),')
        print(f'and to sell on day {sell_on + 1} (price = {prices[sell_on]}), '
              f'profit = {prices[sell_on]}-{prices[buy_on]} = '
              f'{prices[sell_on] - prices[buy_on]}')
    else:
        print('In this case, the best choice was not to make any transactions')
    print()


print_profit((7, 1, 5, 3, 6, 4), 5, 1, 4)
print_profit((7, 6, 4, 3, 1), 0)
print_profit((7, 8), 1, 0, 1)
print_profit((8, 7), 0)
print_profit((7,), 0)

# !!!
# And module_4_hard2.py Best Time to Buy and Sell Stock II
# https://github.com/milecamo/Urban/blob/master/course/module_4_hard2.py
