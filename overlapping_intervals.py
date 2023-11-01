# https://leetcode.com/problems/merge-intervals/?envType=study-plan-v2&envId=top-interview-150
from typing import List


class Solution:

    def within_range(self, a, b, c):
        return a <= c <= b

    def overlap(self, a, b, c, d):
        return self.within_range(a, b, c) or self.within_range(a, b, d) \
            or self.within_range(c, d, a) or self.within_range(c, d, b)

    def merge_once(self, intervals: List[List[int]]) -> List[List[int]]:
        p0 = 0
        p1 = 1
        while p0 + 1 < len(intervals) and p1 < len(intervals):
            i1 = intervals[p0]
            i2 = intervals[p1]

            if self.overlap(i1[0], i1[1], i2[0], i2[1]):
                intervals[p0][0] = min(i1[0], i2[0])
                intervals[p0][1] = max(i1[1], i2[1])

                del intervals[p1]

            elif p1 + 1 < len(intervals):
                p1 += 1
            else:
                p0 += 1
                p1 = p0 + 1

        return intervals

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        return self.merge_once(self.merge_once(intervals))


def test_case1():
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    exp = [[1, 6], [8, 10], [15, 18]]
    assert Solution().overlap(1, 3, 2, 100)
    assert Solution().overlap(1, 3, 2, 6)

    assert not Solution().overlap(1, 6, 10, 15)
    assert not Solution().overlap(1, 6, 8, 20)

    assert not Solution().overlap(1, 6, 8, 10)
    # assert Solution().overlap_left(1, 3, 2)
    res = Solution().merge(intervals)
    assert res == exp


def test_case2():
    intervals = [[1, 4], [4, 5]]
    exp = [[1, 5]]

    assert Solution().merge(intervals) == exp


def test_case3():
    intervals = [[1, 4], [0, 4]]
    exp = [[0, 4]]

    assert Solution().merge(intervals) == exp


def test_case4():
    inp = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]

    assert Solution().merge(inp) is not None


def test_case5():
    inp = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    exp = [[1, 10]]
    res = Solution().merge(inp)

    assert res == exp
