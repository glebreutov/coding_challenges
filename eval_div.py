from collections import defaultdict
from typing import List, Tuple, Any, Optional

import pytest


class Solution:
    def build_graph(self, equations: List[List[str]], values: List[float]):
        ineq = defaultdict(dict)
        for (v1, v2), ans in zip(equations, values):
            # v1 / v2 = ans
            # v1 = ans * v2
            # v2 = v1 / ans
            # v2 = v1 * (1 / ans)

            ineq[v1][v2] = ans
            ineq[v2][v1] = 1 / ans

        return ineq

    def express_var(self, g, required, available) -> Optional[float]:

        children = list(g[available].items())
        visited = set()
        children_next = []
        while True:
            if not children:
                return None

            for c, num in children:
                if c == required:
                    return num
                if c not in visited:
                    next_gen = [(k, v * num) for k, v in g[c].items()]
                    children_next.extend(next_gen)
                    visited.add(c)

            children = children_next
            children_next = []

    def calc_eq(self, g, v1, v2):
        if v1 not in g or v2 not in g:
            return -1.0

        if v1 == v2:
            return 1

        if v1 in g[v2]:
            return 1 / g[v2][v1]

        for top_var, top_val in g[v1].items():
            bottom_val = self.express_var(g, top_var, v2)
            if not bottom_val:
                return -1
            return top_val / bottom_val

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[
        float]:

        g = self.build_graph(equations, values)

        return [self.calc_eq(g, a, b) for a, b in queries]


def test_case1():
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    exp = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]

    assert Solution().calcEquation(equations, values, queries) == exp


def test_case2():
    equations = [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]]
    values = [3.0, 4.0, 5.0, 6.0]
    queries = [["x1", "x5"], ["x5", "x2"], ["x2", "x4"], ["x2", "x2"], ["x2", "x9"], ["x9", "x9"]]

    exp = [360.00000, 0.00833, 20.00000, 1.00000, -1.00000, -1.00000]
    res = Solution().calcEquation(equations, values, queries)
    assert all([(x - y) * (x - y) < 0.0001 for x, y in zip(res, exp)])


def test_case3():
    equations = [["a", "b"], ["c", "d"]]
    values = [1.0, 1.0]
    queries = [["a", "c"], ["b", "d"], ["b", "a"], ["d", "c"]]

    res = Solution().calcEquation(equations, values, queries)
    # assert [(x - y) * (x - y) < 0.0001 for x, y in zip(res, exp)]
