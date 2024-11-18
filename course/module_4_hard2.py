# Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

def up_trend(prices, index=0):
    for i in range(index, len(prices) - 1):
        if prices[i] < prices[i + 1]:
            return i
    return -1


def down_trend(prices, index=0):
    for i in range(index, len(prices) - 1):
        if prices[i] > prices[i + 1]:
            return i
    return -1


prices = [7, 1, 5, 3, 6, 4]
prices = [1, 2, 3, 4, 5]
prices = [7, 6, 4, 3, 1]
