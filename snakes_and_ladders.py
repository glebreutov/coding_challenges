import functools
from typing import List


class Solution:

    # def cv(self, row, n, i):

    def num_board(self, n):
        res = []
        for i in range(n * n, 0, -1):

            reminder = i % n

            if reminder == 0:
                if len(res) % 2 == 0 and len(res) > 0:
                    res[-1].reverse()
                row = []
                res.append(row)

            row.append(i)

        if len(res) % 2 == 0 and len(res) > 0:
            res[-1].reverse()

        return res

    def board_dict(self, board_numbers: List[List[int]]):
        n = len(board_numbers)
        d = [None for _ in range(n * n + 1)]

        for i in range(n):
            for j in range(n):
                idx = board_numbers[i][j]
                d[idx] = (i, j)

        return d

    def dice(self, curr, n):
        return range(curr + 1, 1 + min(curr + 6, n * n))

    def board_value(self, board, board_dict, cell_label):
        row, cell = board_dict[cell_label]
        val = board[row][cell]
        if val == -1:
            return cell_label
        else:
            return val

    def possible_moves(self, board, d, n, start):
        return [self.board_value(board, d, cell) for cell in self.dice(start, n)]

    def print_board(self, board, board_nums):
        print()
        for row in range(len(board)):
            for cell in range(len(board)):
                val = board[row][cell] if board[row][cell] != -1 else board_nums[row][cell]
                print(val, end="\t")
            print()


    def norm_board(self, board: List[List[int]]):
        for i, row in enumerate(board):
            if i % 2 != 0:
                row.reverse()

    def snakesAndLadders(self, board: List[List[int]]) -> int:

        n = len(board)
        dest = n * n
        # self.norm_board(board)
        board_numbers = self.num_board(n)
        d = self.board_dict(board_numbers)

        self.print_board(board, board_numbers)

        fx_next = functools.partial(self.possible_moves, board, d, n)
        num = 0
        moves = {1}
        while True:

            next_moves = {next_pos for current_pos in moves for next_pos in fx_next(current_pos)}
            num += 1
            if next_moves == moves:
                return -1

            moves = next_moves
            if dest in moves:
                # print(f"Win on turn {num}!")
                return num

            # start = min(moves, key=lambda x: dest - x)
            # print(f"Turn: {num}. Moving on cell {start}")


def test_case1():
    print()
    b = Solution().num_board(6)
    for r in b:
        print(r)

    print(Solution().board_dict(b))


def test_case11():
    print()
    b = Solution().num_board(5)
    for r in b:
        print(r)

    print(Solution().board_dict(b))


def test_case2():
    assert list(Solution().dice(1, 6)) == list(range(2, 8))


def test_case_r1():
    board = [[-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, -1, -1, -1, -1, -1], [-1, 35, -1, -1, 13, -1],
             [-1, -1, -1, -1, -1, -1], [-1, 15, -1, -1, -1, -1]]

    exp = 4

    assert Solution().snakesAndLadders(board) == exp


def test_case_r2():
    board = [[-1, -1], [-1, 3]]

    exp = 1

    assert Solution().snakesAndLadders(board) == exp


def test_case_r3():
    board = [[1, 1, -1], [1, 1, 1], [-1, 1, 1]]

    exp = -1

    assert Solution().snakesAndLadders(board) == exp


def test_case_r4():
    board = [
        [-1, -1, 19, 10, -1],
        [2, -1, -1, 6, -1],
        [-1, 17, -1, 19, -1],
        [25, -1, 20, -1, -1],
        [-1, -1, -1, -1, 15]
    ]

    exp = 2

    assert Solution().snakesAndLadders(board) == exp
