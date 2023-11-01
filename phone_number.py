from typing import List


class Solution:
    def __init__(self):
        self.db = {
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        acc = self.db[digits[0]]

        tail = digits[1:]

        for d in tail:
            n_acc = []
            for l in self.db[d]:
                for s in acc:
                    n_acc.append(s + l)

            acc = n_acc

        return acc


def test_case1():
    s = Solution().letterCombinations("23")

    assert s


def test_case2():
    s = Solution().letterCombinations("")

    assert not s