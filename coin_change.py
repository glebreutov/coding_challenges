import sys
from typing import List, Tuple, Optional


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo: List[Optional[int]] = [None for _ in range(amount + 1)]
        memo[0] = 0

        for cv in range(1, amount + 1):
            min_coins = None
            for c in coins:
                if c > cv:
                    continue

                if memo[cv - c] is not None:
                    new_amount = memo[cv - c] + 1
                    if min_coins is None or new_amount < min_coins:
                        min_coins = new_amount

            if min_coins is not None:
                memo[cv] = min_coins

        return memo[-1] if memo[-1] is not None else -1


def test_case1():
    coins = [1, 2, 5]

    amount = 11

    assert Solution().coinChange(coins, amount) == 3


def test_case2():
    coins = [2]
    amount = 3

    assert Solution().coinChange(coins, amount) == -1


def test_case3():
    coins = [1]
    amount = 0

    assert Solution().coinChange(coins, amount) == 0


def test_case4():
    coins = [2, 5, 10, 1]
    amount = 27

    assert Solution().coinChange(coins, amount) == 4


def test_case5():
    coins = [1, 3, 5]
    amount = 5

    assert Solution().coinChange(coins, amount) == 1


def test_case6():
    coins = [1, 2, 5]
    amount = 11

    assert Solution().coinChange(coins, amount) == 3


def test_case7():
    coins = [186,419,83,408]
    amount = 6249

    assert Solution().coinChange(coins, amount) == 20