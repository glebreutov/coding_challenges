import sys
from functools import cache
from typing import List, Tuple


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        @cache
        def dfs(i, j, d):

            if d == 1:
                return max(jobDifficulty[i:j])

            if d > len(jobDifficulty[i:j]):
                return -1

            min_val = sys.maxsize

            for s in range(i+1, j - (d - 1) + 1):
                min_val = min(min_val, max(jobDifficulty[i:s]) + dfs(s, j, d - 1))

            return min_val

        return dfs(0, len(jobDifficulty), d)


def test_case1():
    jobDifficulty = [6, 5, 4, 3, 2, 1]
    d = 2
    exp = 7

    assert Solution().minDifficulty(jobDifficulty, d) == exp


def test_case2():
    jobDifficulty = [1, 1, 1]
    d = 3
    exp = 3
    assert Solution().minDifficulty(jobDifficulty, d) == exp


def test_case3():
    jobDifficulty = [9, 9, 9]
    d = 4
    exp = -1
    assert Solution().minDifficulty(jobDifficulty, d) == exp
