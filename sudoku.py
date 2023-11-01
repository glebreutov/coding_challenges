from typing import List


class Solution:

    def slice(self, a: List[str], row_slice: slice, col_slice: slice):
        acc = []
        for row in a[row_slice]:
            for cell in row[col_slice]:
                if cell != ".":
                    acc.append(cell)

        return acc

    def seq_is_valid(self, a: List[str]):
        return len(set(a)) == len(a)

    def rows_are_valid(self, a):
        return all([
            self.seq_is_valid(
                self.slice(a, slice(row, row + 1), slice(0, len(a)))
            ) for row in range(len(a))])

    def cols_are_valid(self, a):
        return all([
            self.seq_is_valid(
                self.slice(a, slice(0, len(a)), slice(col, col + 1))
            ) for col in range(len(a))])

    def squares_are_valid(self, a):
        squares = int(len(a) / 3)

        seq = [(x, y) for x in range(squares) for y in range(squares)]

        slices = [(slice(3 * a, 3 * (a + 1)), slice(3 * b, 3 * (b + 1))) for a, b in seq]

        return all([
            self.seq_is_valid(
                self.slice(a, s1, s2)
            ) for s1, s2 in slices])

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        return self.rows_are_valid(board) and self.cols_are_valid(board) and self.squares_are_valid(board)


def test_case1():
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    exp = True

    assert Solution().rows_are_valid(board)

    assert Solution().isValidSudoku(board)


def test_case2():
    board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    exp = True

    assert not Solution().cols_are_valid(board)

    assert not Solution().isValidSudoku(board)
