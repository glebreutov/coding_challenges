from typing import List


class Solution:

    @staticmethod
    def can_be_next(g: str, next: str):
        diff = 0
        for a, b in zip(g, next):
            if a != b:
                diff += 1
            if diff > 1:
                return False

        return diff == 1

    @staticmethod
    def match(s: str, e: str, bank: str, mut: int = 0, acc=[]):
        if s == e:
            return mut

        possible = [b for b in bank if Solution.can_be_next(s, b) and b not in acc]

        if not possible:
            return -1
        nl = [Solution.match(n, e, bank, mut + 1, acc + [s]) for n in possible]

        return min([n for n in nl if n > -1], default=-1)


    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        return Solution.match(startGene, endGene, bank)


def matched_gene(first: str, diff: List[int], second: str):
    for i, (a, b) in enumerate(zip(first, second)):
        if a != b and i not in diff:
            return False

    return True


def test_case1():
    startGene = "AACCGGTT"
    endGene = "AACCGGTA"
    bank = ["AACCGGTA"]

    exp = 1
    assert Solution().minMutation(startGene, endGene, bank) == exp


def test_case2():
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    exp = 2

    assert Solution().minMutation(startGene, endGene, bank) == exp


def test_case3():
    startGene = "AAAACCCC"
    endGene = "CCCCCCCC"
    bank = ["AAAACCCA", "AAACCCCA", "AACCCCCA", "AACCCCCC", "ACCCCCCC", "CCCCCCCC", "AAACCCCC", "AACCCCCC"]
    exp = 4

    assert Solution().minMutation(startGene, endGene, bank) == exp
