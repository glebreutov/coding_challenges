from collections import defaultdict
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3:
            return len(points)

        x_count = defaultdict(lambda: 0)
        y_count = defaultdict(lambda: 0)
        for x, y in points:
            x_count[x] += 1
            y_count[y] += 1

        # line eq:
        equations = set()
        for x1, y1 in points:
            for x2, y2 in points:
                if x2 != x1:
                    a = (y2 - y1) / (x2 - x1)
                    b = y1 - a * x1
                else:
                    a = 0
                    b = y1 - a * x1

                equations.add((a, b))

        max_val = max(max(x_count.values()), max(y_count.values()))
        point_count = 0
        for a, b in equations:
            point_count = 0
            for x, y in points:
                if abs(x * a + b - y) < 0.00001:
                    point_count += 1

            if point_count > max_val:
                max_val = point_count

        return max_val


def test_case0():
    points = [[1, 1], [2, 2], [3, 3]]
    assert Solution().maxPoints(points) == 3


def test_case1():
    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    assert Solution().maxPoints(points) == 4


def test_case2():
    points = [[4, 5], [4, -1], [4, 0]]
    assert Solution().maxPoints(points) == 3


def test_case3():
    points = [[-6, -1], [3, 1], [12, 3]]
    assert Solution().maxPoints(points) == 3


def test_case4():
    points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    assert Solution().maxPoints(points) == 4