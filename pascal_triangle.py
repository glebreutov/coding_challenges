from typing import List


class Solution:

    def next_row(self, input: List[int]) -> List[int]:
        if not input:
            return [1]
        acc = []
        last_value = input[0]

        for val in input[1:]:
            acc.append(last_value + val)
            last_value = val

        return [1] + acc + [1]

    def getRow(self, rowIndex: int) -> List[int]:
        prev_value = []
        value = None
        for _ in range(rowIndex + 1):
            value = self.next_row(prev_value)
            prev_value = value
        return value


# row = 0, cells = 0
# row = 1, cells = 1
# row = 2, cells = 2

def test1():
    s = Solution()

    assert (s.next_row([]) == [1])

    assert (s.next_row([1]) == [1, 1])

    assert (s.next_row([1, 1]) == [1, 2, 1])

    assert (s.next_row([1, 2, 1]) == [1, 3, 3, 1])


def test2():
    s = Solution()

    assert (s.getRow(3) == [1, 3, 3, 1])
