from typing import List, Tuple, Set


class Solution:
    def min_dist(self, i1: Set[Tuple[int, int]], i2: Set[Tuple[int, int]]):
        min_dist = 9999999
        for first_row_idx, first_cell_idx in i1:
            for second_row_idx, second_cell_idx in i2:
                row_dist = abs(first_row_idx - second_row_idx)
                cell_dist = abs(first_cell_idx - second_cell_idx)
                dist = row_dist + cell_dist - 1
                if dist == 1:
                    return dist

                min_dist = min(dist, min_dist)

        return min_dist

    def check_neighbours(self, graph: List[Tuple[int, int]], row_idx: int, cell_idx: int):
        combs = [(row_idx - 1, cell_idx), (row_idx + 1, cell_idx), (row_idx, cell_idx - 1), (row_idx, cell_idx + 1)]
        return [(row, cell) for row, cell in combs if (row, cell) in graph]

    def find_island_rec(self, graph: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
        acc = [graph[0]]
        lim = 0

        while lim < len(acc):
            p = acc[lim]
            neighbours = self.check_neighbours(graph, p[0], p[1])
            for n in neighbours:
                if n not in acc:
                    acc.append(n)
            lim += 1

        return set(acc)

    def grid_to_graph(self, grid):
        return [(row_index, cell_index) for row_index, row in enumerate(grid)
                for cell_index, cell in enumerate(row)
                if cell == 1
                ]

    def find_islands(self, grid: List[List[int]]) -> Tuple[Set[Tuple[int, int]], Set[Tuple[int, int]]]:
        graph = list(self.grid_to_graph(grid))
        i1: Set[Tuple[int, int]] = self.find_island_rec(graph)
        i2: Set[Tuple[int, int]] = set(graph).difference(i1)

        return i1, i2

    def shortestBridge(self, grid: List[List[int]]) -> int:
        i1, i2 = self.find_islands(grid)

        return self.min_dist(i1, i2)


def test_case1():
    tc = [
        [0, 1],
        [1, 0]
    ]
    s = Solution()
    i1, i2 = s.find_islands(tc)
    assert i1 == {(0, 1)}

    assert i2 == {(1, 0)}
    assert s.min_dist(i1, i2) == 1


def test_case2():
    tc = [
        [0, 1, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]
    s = Solution()
    i1, i2 = s.find_islands(tc)
    assert i1 == {(0, 1)}

    assert i2 == {(2, 2)}
    assert s.min_dist(i1, i2) == 2


def test_case3():
    tc = [
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1]
    ]
    s = Solution()

    i1, i2 = s.find_islands(tc)
    assert len(i1) == 16
    assert i2 == {(2, 2)}
    assert s.min_dist(i1, i2) == 1


def test_case4():
    tc = [
        [0, 0, 1, 0, 1],
        [0, 1, 1, 0, 1],
        [0, 1, 0, 0, 1],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    s = Solution()
    i1, i2 = s.find_islands(tc)
    assert i1 == {(0, 2), (1, 1), (1, 2), (2, 1)}
    assert i2 == {(0, 4), (1, 4), (2, 4)}
    assert s.min_dist(i1, i2) == 1


def test_case5():
    tc = [
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0]
    ]

    s = Solution()
    i1, i2 = s.find_islands(tc)
    assert s.min_dist(i1, i2) == 1
