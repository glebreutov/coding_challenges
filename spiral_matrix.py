from typing import List


class Solution:

    @staticmethod
    def next_step(row_num, col_num, row=0, col=0, offset=0, op_counter=1):

        if row_num <= 0 or col_num <= 0:
            return

        yield offset + row, offset + col

        if op_counter >= row_num * col_num:
            return

        if row == 0 and col < col_num - 1:
            yield from Solution.next_step(row_num, col_num, row, col + 1, offset, op_counter + 1)
        elif col == col_num - 1 and row < row_num - 1:
            yield from Solution.next_step(row_num, col_num, row + 1, col, offset, op_counter + 1)
        elif col > 0 and row == row_num - 1:
            yield from Solution.next_step(row_num, col_num, row, col - 1, offset, op_counter + 1)
        elif col == 0 and row == 1:
            yield from Solution.next_step(row_num - 2, col_num - 2, 0, 0, offset + 1)
        elif col == 0 and row > 0:
            yield from Solution.next_step(row_num, col_num, row - 1, 0, offset, op_counter + 1)



    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        return [matrix[r][c] for r, c in Solution.next_step(rows, cols)]


def test_case1():
    assert not list(Solution.next_step(0, 0))


def test_case2():
    assert list(Solution.next_step(1, 1)) == [(0, 0)]


def test_case3():
    assert list(Solution.next_step(1, 2)) == [(0, 0), (0, 1)]


def test_case4():
    assert list(Solution.next_step(2, 2)) == [(0, 0), (0, 1), (1, 1), (1, 0)]


def test_case5():
    assert list(Solution.next_step(3, 3)) == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0), (1, 1)]


def test_case6():
    assert list(Solution.next_step(3, 2)) == [(0, 0), (0, 1), (1, 1), (2, 1), (2, 0), (1, 0)]
