from typing import List


class Solution:
    def should_not_flip(self, board: List[List[str]], i, j):
        if j < 0 or j >= len(board[0]):
            return

        if i < 0 or i >= len(board):
            return

        cv = board[i][j]
        on_the_edge = (i == 0 or i == len(board) - 1) or (j == 0 or j == len(board[0]) - 1)

        adjacent_no_flip = (i + 1 < len(board) and board[i + 1][j] == "N") \
                           or (i - 1 >= 0 and board[i - 1][j] == "N") \
                           or (j + 1 < len(board[0]) and board[i][j + 1] == "N") \
                           or (j - 1 >= 0 and board[i][j - 1] == "N")

        if cv == "O" and (on_the_edge or adjacent_no_flip):
            board[i][j] = "N"
            self.should_not_flip(board, i + 1, j)
            self.should_not_flip(board, i - 1, j)
            self.should_not_flip(board, i, j + 1)
            self.should_not_flip(board, i, j - 1)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.should_not_flip(board, i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                cv = board[i][j]
                if cv == "N":
                    board[i][j] = "O"
                if cv == "O":
                    board[i][j] = "X"

def test_case1():
    inp = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    exp = [["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "X", "X", "X"], ["X", "O", "X", "X"]]

    Solution().solve(inp)
    assert inp == exp


def test_case2():
    inp = [["O", "X", "X", "O", "X"], ["X", "O", "O", "X", "O"], ["X", "O", "X", "O", "X"], ["O", "X", "O", "O", "O"],
           ["X", "X", "O", "X", "O"]]
    exp = [["O", "X", "X", "O", "X"], ["X", "X", "X", "X", "O"], ["X", "X", "X", "O", "X"], ["O", "X", "O", "O", "O"],
           ["X", "X", "O", "X", "O"]]

    Solution().solve(inp)
    assert inp == exp
