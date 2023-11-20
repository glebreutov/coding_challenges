from typing import List


class Solution:
    @staticmethod
    def int_overlap(s1: int, e1: int, s2: int, e2: int):
        return e1 >= s2 >= s1 or e1 >= e2 >= s1

    @staticmethod
    def int_overlap_sym(s1: int, e1: int, s2: int, e2: int):
        return Solution.int_overlap(s1, e1, s2, e2) or Solution.int_overlap(s2, e2, s1, e1)

    @staticmethod
    def first_is_left_to_second(s1, e1, s2, e2):
        return e1 < s2

    @staticmethod
    def add_intervals(s1: int, e1: int, s2: int, e2: int):
        return [min(s1, s2), max(e1, e2)]

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        target = newInterval
        acc = []
        i = 0
        while i < len(intervals):
            ival = intervals[i]
            is_intersect = Solution.int_overlap_sym(ival[0], ival[1], target[0], target[1])

            if is_intersect:
                target = Solution.add_intervals(ival[0], ival[1], target[0], target[1])
            elif not Solution.first_is_left_to_second(ival[0], ival[1], target[0], target[1]):
                acc.append(target)
                acc.extend(intervals[i:])
                return acc
            else:
                acc.append(ival)
            i += 1
        return acc + [target]

def test_case1():
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    exp = [[1, 5], [6, 9]]

    assert Solution().insert(intervals, newInterval) == exp

def test_case2():
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    exp = [[1,2],[3,10],[12,16]]

    assert Solution().insert(intervals, newInterval) == exp




