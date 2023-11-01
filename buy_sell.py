from typing import List


class Solution:

    def maxProfit(self, prices: List[int]) -> int:
        final_profit = 0

        min_buy = 9999
        max_sell = 0
        for price in prices:
            if price < min_buy:
                min_buy = price
                max_sell = 0
            elif price > max_sell:
                max_sell = price

            profit = max_sell - min_buy
            if profit > final_profit:
                final_profit = profit

        return final_profit


def test_case1():
    prices = [7, 1, 5, 3, 6, 4]

    assert Solution().maxProfit(prices) == 5


def test_case2():
    prices = [7, 6, 4, 3, 1]

    assert Solution().maxProfit(prices) == 0


def test_case3():

    prices = [7, 1, 5, 3, 6, 4, 0, 0, 0, 0, 0, 0, 0, 0]

    assert Solution().maxProfit(prices) == 5


