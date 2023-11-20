from typing import List

class Solution:

    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev = 0
        for s in bank:
            count = s.count("1")
            if count:
                res += count * prev
                prev = count

        return res


def test_case1():
    bank = ["011001", "000000", "010100", "001000"]
    exp = 8
    assert Solution().numberOfBeams(bank) == exp


def test_case2():
    bank = ["000","111","000"]
    exp = 0
    assert Solution().numberOfBeams(bank) == exp
