from typing import List


class Solution:


    @staticmethod
    def set_t(matrix: List[List[int]], row, col):
        # setting col
        for r in range(0, row):
            matrix[r][col] = 0

        for r in range(row, len(matrix)):
            if matrix[r][col] != 0:
                matrix[r][col] = 'T'

        # setting row
        for c in range(0, len(matrix[0])):
            cv = matrix[row][c]
            if cv != 0:
                matrix[row][c] = 'T'

    def setZeroes(self, matrix: List[List[int]]) -> None:
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    Solution.set_t(matrix, row, col)
                else:
                    t_above = row > 0 and matrix[row - 1][col] == 'T'
                    t_at_left = col > 0 and matrix[row][col - 1] == 'T'

                    if t_above:
                        matrix[row - 1][col] = 0

                    if t_at_left:
                        matrix[row][col - 1] = 0

        for c in range(0, len(matrix[0])):
            if matrix[-1][c] == 'T':
                matrix[-1][c] = 0





def test_case1():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    exp = [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
    Solution().setZeroes(matrix)
    assert matrix == exp


def test_case2():
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    exp = [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
    Solution().setZeroes(matrix)
    assert matrix == exp

def test_case3():
    matrix = [[1,0]]
    exp = [[0, 0]]
    Solution().setZeroes(matrix)
    assert matrix == exp