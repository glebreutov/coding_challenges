import dataclasses
import string
from collections import deque, defaultdict
from dataclasses import dataclass
from typing import List, Set


@dataclass
class StrPointer:
    char: str
    repl_count: int
    len: int


class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return 0
        if len(s) <= k + 1:
            return k + 1

        heads = [StrPointer(x, 0, 0) for x in string.ascii_uppercase]
        max_len = 0

        for i, c in enumerate(s):
            for h in heads:
                if h.char == c:
                    h.len += 1
                elif h.repl_count < k:
                    h.repl_count += 1
                    h.len += 1
                else:
                    max_len = max(max_len, h.len)
                    h.len = min(1, k)
                    h.repl_count = min(1, k)

        return max(max_len, max([h.len for h in heads]))


def test_case1():
    s = "ABAB"
    k = 2
    assert Solution().characterReplacement(s, k) == 4


def test_case2():
    s = "AABABBA"
    k = 1

    assert Solution().characterReplacement(s, k) == 4


def test_case3():
    s = "DBEEEEE"
    k = 2

    assert Solution().characterReplacement(s, k) == 7


def test_case4():
    s = "BEEEEED"
    k = 2

    assert Solution().characterReplacement(s, k) == 7


def test_case5():
    s = "BEEEEEDE"
    k = 2

    assert Solution().characterReplacement(s, k) == 8


def test_case6():
    s = "BEEEEEDEE"
    k = 2

    assert Solution().characterReplacement(s, k) == 9


def test_case7():
    s = "AABA"
    k = 0

    assert Solution().characterReplacement(s, k) == 2

def test_case9():
    s = "ABAA"
    k = 0

    assert Solution().characterReplacement(s, k) == 2


def test_case8():
    s = "KRSCDCSONAJNHLBMDQGIFCPEKPOHQIHLTDIQGEKLRLCQNBOHNDQGHJPNDQPERNFSSSRDEQLFPCCCARFMDLHADJADAGNNSBNCJQOF"
    k = 4

    assert Solution().characterReplacement(s, k) == 7


def test_case10():
    s = "IMNJJTRMJEGMSOLSCCQICIHLQIOGBJAEHQOCRAJQMBIBATGLJDTBNCPIFRDLRIJHRABBJGQAOLIKRLHDRIGERENNMJSDSSMESSTR"
    k = 2

    assert Solution().characterReplacement(s, k) == 6