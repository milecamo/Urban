# Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

def up_trend(prices, index=0):
    for i in range(index, len(prices) - 1):
        if prices[i] < prices[i + 1]:
            return i + 1
    return 0


def down_trend(prices, index=0):
    for i in range(index, len(prices) - 1):
        if prices[i] > prices[i + 1]:
            return i + 1
    return 0


def max_profit(*prices):
    profit = 0
    index = 0
    buy_on = []
    sell_on = []
    while index < len(prices):
        up_day = up_trend(prices, index)
        if up_day:
            buy_on.append(up_day)
            down_day = down_trend(prices, up_day - 1)
            if down_day:
                sell_on.append(down_day)
                profit += prices[down_day - 1] - prices[up_day - 1]
                index = down_day
            else:
                sell_on.append(len(prices))
                profit += prices[len(prices) - 1] - prices[up_day - 1]
                index = len(prices)
        else:
            index = len(prices)

    return profit, buy_on, sell_on


def print_profit(prices, should_be, should_buy_on=None, should_sell_on=None):
    if not should_buy_on:
        should_buy_on = []
    if not should_sell_on:
        should_sell_on = []
    result = profit, buy_on, sell_on = max_profit(*prices)
    # print(should_buy_on, should_sell_on)
    # print(buy_on, sell_on)
    qa_result = result == (should_be, should_buy_on, should_sell_on)
    print(f'Maximum profit for stock prices {prices} was {profit} ', qa_result)
    if profit:
        for i in range(len(buy_on)):
            beg_str = "Then the"
            if not i:
                beg_str = "The"
            print(beg_str,
                  f'best time to buy was on day {buy_on[i]} (price = {prices[buy_on[i] - 1]}), '
                  f'and to sell on day {sell_on[i]} (price = {prices[sell_on[i] - 1]}), '
                  f'profit = {prices[sell_on[i] - 1]}-{prices[buy_on[i] - 1]} = '
                  f'{prices[sell_on[i] - 1] - prices[buy_on[i] - 1]}')
    else:
        print('In this case, the best choice was not to make any transactions')
    print()


print_profit((7, 1, 5, 3, 6, 4), 7, [2, 4], [3, 5])
print_profit((1, 2, 3, 4, 5), 4, [1], [5])
print_profit((7, 6, 4, 3, 1), 0)
print_profit((7, 8), 1, [1], [2])
print_profit((8, 7), 0)
print_profit((7,), 0)
print_profit((), 0)
print(f'Maximum profit for empty stock prices was {max_profit()[0]}')
