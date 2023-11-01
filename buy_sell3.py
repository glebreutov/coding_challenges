import sys
from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        profit_left = [0 for _ in range(len(prices))]

        min_buy = sys.maxsize
        for i in range(0, len(prices)):
            min_buy = min(prices[i], min_buy)
            max_sell = prices[i]
            profit_left[i] = max(profit_left[i - 1], max_sell - min_buy)

        profit_right = [0 for _ in range(len(prices))]

        max_sell = 0
        total_profit = 0

        for i in range(len(prices) - 1, -1, -1):
            max_sell = max(prices[i], max_sell)
            min_buy = prices[i]
            if i + 1 >= len(prices):
                profit_right[i] = max_sell - min_buy
            else:
                profit_right[i] = max(profit_right[i + 1], max_sell - min_buy)

            total_profit = max(total_profit, profit_right[i] + profit_left[i])

        return total_profit


def test_case1():
    prices = [3, 3, 5, 0, 0, 3, 1, 4]
    exp = 6
    assert Solution().maxProfit(prices) == exp


def test_case2():
    prices = [1, 2, 3, 4, 5]
    exp = 4
    # assert Solution().maxProfitGrad(prices) == exp
    assert Solution().maxProfit(prices) == exp


def test_case3():
    prices = [7, 6, 4, 3, 1]
    exp = 0
    assert Solution().maxProfit(prices) == exp


def test_case4():
    prices = [1, 2]
    exp = 1
    assert Solution().maxProfit(prices) == exp


def test_case5():
    prices = [2, 1]
    exp = 0
    assert Solution().maxProfit(prices) == exp


def test_case6():
    prices = [2, 1, 4, 5, 2, 9, 7]
    exp = 11
    assert Solution().maxProfit(prices) == exp
