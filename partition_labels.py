from collections import defaultdict
from typing import List


class Solution:

    def intersects_right(self, left_int, right_int):
        return left_int[1] > right_int[0]

    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return []
        letter_map = defaultdict(lambda : set())

        for i, letter in enumerate(s):
            letter_map[letter].add(i)

        intervals = [(min(occurances), max(occurances)) for occurances in letter_map.values()]

        prev = intervals[0]
        acc = []
        for i in range(1, len(intervals)):
            if self.intersects_right(prev, intervals[i]):
                prev = (min(prev[0], intervals[i][0]), max(prev[1], intervals[i][1]))
            else:
                acc.append(1 + prev[1] - prev[0])
                prev = intervals[i]

        acc.append(1 + prev[1] - prev[0])
        return acc


def test_case1():
    s = "abacabchijhij"
    res = [7, 6]

    assert Solution().partitionLabels(s) == res

def test_case0():
    s = ""
    res = []

    assert Solution().partitionLabels(s) == res

def test_case2():
    s = "ababcbacadefegdehijhklij"
    res = [9,7,8]
    assert Solution().partitionLabels(s) == res


def test_case3():
    s = "eccbbbbdec"
    res = [10]
    assert Solution().partitionLabels(s) == res
