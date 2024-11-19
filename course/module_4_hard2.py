# Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

def signal(prices, metric, StartTime):
    for i in range(StartTime, len(prices) - 1):
        if metric(prices[i + 1], prices[i]):
            return i
    return -1


def make_signaller(metric):
    return lambda prices, StartTime: signal(prices, metric, StartTime)


up_trend_signal = make_signaller(lambda next_price, past_price: next_price > past_price)
down_trend_signal = make_signaller(lambda next_price, past_price: next_price < past_price)


def max_profit(prices):
    profit = 0
    current_day = 0
    buy_on = []
    sell_on = []
    while current_day < len(prices) - 1:
        buy_day = up_trend_signal(prices, current_day)
        if buy_day >= 0:
            buy_on.append(buy_day)
            current_day = down_trend_signal(prices, buy_day + 1)
            if current_day < 0:
                current_day = len(prices) - 1
            sell_on.append(current_day)
            profit += prices[current_day] - prices[buy_day]
            current_day += 1
        else:
            # not shorting yet :( but not longing either already :)))
            break

    return profit, buy_on, sell_on


def print_profit(prices, should_be, should_buy_on=None, should_sell_on=None):
    if not should_buy_on:
        should_buy_on = []
    if not should_sell_on:
        should_sell_on = []
    profit, buy_on, sell_on = max_profit(prices)
    print(f'Maximum profit for stock prices {prices} was {profit} ',
          (profit, buy_on, sell_on) == (should_be, should_buy_on, should_sell_on))
    if profit:
        for i in range(len(buy_on)):
            beg_str = "The"
            if i:
                beg_str = "Then the"
            print(beg_str,
                  f'best time to buy was on day {buy_on[i] + 1} (price = {prices[buy_on[i]]}),')
            print(f'and to sell on day {sell_on[i] + 1} (price = {prices[sell_on[i]]}), '
                  f'profit = {prices[sell_on[i]]}-{prices[buy_on[i]]} = '
                  f'{prices[sell_on[i]] - prices[buy_on[i]]}')
    else:
        print('In this case, the best choice was not to make any transactions')
    print()


print_profit((7, 1, 5, 3, 6, 4), 7, [1, 3], [2, 4])
print_profit((1, 2, 3, 4, 5), 4, [0], [4])
print_profit((7, 6, 4, 3, 1), 0)
print_profit((7, 8), 1, [0], [1])
print_profit((7, 8, 7, 8), 2, [0, 2], [1, 3])
print_profit((7, 8, 7, 8, 7), 2, [0, 2], [1, 3])
print_profit((8, 7), 0)
print_profit((7,), 0)
