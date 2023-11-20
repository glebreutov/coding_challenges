import functools
from collections import namedtuple
from typing import List

Vector = namedtuple("Vector", ["x", "y"])


class Solution:

    @staticmethod
    def addr_to_vector(n, row, col) -> Vector:
        half = (n - 1) / 2
        return Vector(x=col - half, y=half-row)

    @staticmethod
    def vector_to_addr(n, v: Vector):
        half = (n - 1) / 2
        return int(half - v.y), int(half + v.x)

    # y=half-row
    # row = half - y

    # x = col - half
    # col = x + half

    @staticmethod
    def rotate_vec(v: Vector):
        return Vector(x=v.y, y=-v.x)

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        addr_to_vector = functools.partial(Solution.addr_to_vector, n)
        vector_to_addr = functools.partial(Solution.vector_to_addr, n)

        def rotate_four(row, cell):
            buf = []
            for _ in range(4):
                val = matrix[row][cell]
                v = addr_to_vector(row, cell)
                v1 = Solution.rotate_vec(v)
                row, cell = vector_to_addr(v1)
                buf.append((row, cell, val))

            for row, cell, v in buf:
                matrix[row][cell] = v

        for row in range(int(n / 2) + n % 2):
            for cell in range(row, int(n / 2) + n % 2):

                rotate_four(row, cell)


def test_c1():
    n = 3
    row = 0
    col = 2
    v = Solution.addr_to_vector(n, row, col)
    assert v.y == 1
    assert v.x == 1
    assert Solution.vector_to_addr(n, v) == (row, col)


def test_c2():
    assert Solution.rotate_vec(Vector(1, 1)) == Vector(1, -1)
    assert Solution.rotate_vec(Vector(1, -1)) == Vector(-1, -1)
    assert Solution.rotate_vec(Vector(-1, -1)) == Vector(-1, 1)
    assert Solution.rotate_vec(Vector(-1, 1)) == Vector(1, 1)


def test_c3():
    assert Solution.rotate_vec(Vector(0, 1)) == Vector(1, 0)
    assert Solution.rotate_vec(Vector(1, 0)) == Vector(0, -1)
    assert Solution.rotate_vec(Vector(0, -1)) == Vector(-1, 0)
    assert Solution.rotate_vec(Vector(-1, 0)) == Vector(0, 1)


def test_c4():
    n = 3
    row = 0
    col = 0
    v = Solution.addr_to_vector(n, row, col)
    assert v.x == -1.0
    assert v.y == 1.0
    # x1, y1 = Solution.rotate_vec(x, y)
    #
    # assert Solution.coord_to_addr(n, x, y) == (row, col)
    #


def test_case1():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    exp = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

    Solution().rotate(matrix)

    assert matrix == exp
