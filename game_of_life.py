from typing import List


class Solution:

    def count_alive(self, board: List[List[int]], row, col):
        center_value = board[row][col]
        res = 0
        for r in range(row - 1, row + 2):
            if r < 0:
                continue
            if r >= len(board):
                continue
            rs = sum(board[r][max(0, col - 1):col + 2])
            if r == row:
                rs -= center_value

            res += rs

        return center_value, res

    def rules_of_life(self, is_alive, alive_neighbours):
        if is_alive == 1 and alive_neighbours < 2:
            return 0
        elif is_alive == 1 and alive_neighbours < 4:
            return 1
        elif is_alive == 1 and alive_neighbours > 3:
            return 0
        elif is_alive == 0 and alive_neighbours == 3:
            return 1
        else:
            return is_alive

    def gameOfLife(self, board: List[List[int]]) -> None:
        rows = len(board)
        cols = len(board[0])
        nboard = []

        for row_idx in range(rows):
            for cell_idx in range(cols):
                is_alive, alive_neighbours = self.count_alive(board, row_idx, cell_idx)
                if len(nboard) < row_idx + 1:
                    nboard.append([])
                will_be_alive = self.rules_of_life(is_alive, alive_neighbours)
                nboard[row_idx].append(will_be_alive)

        for row_idx in range(rows):
            for cell_idx in range(cols):
                board[row_idx][cell_idx] = nboard[row_idx][cell_idx]


def test_case1():
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    exp = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
    assert Solution().count_alive(board, 1, 0) == (0, 3)
    Solution().gameOfLife(board)

    assert board == exp


def test_case2():
    board = [[1, 1], [1, 0]]
    exp = [[1, 1], [1, 1]]
    Solution().gameOfLife(board)

    assert board == exp
