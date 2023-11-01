from collections import defaultdict
from typing import List
from pytest_unordered import unordered

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        acc = defaultdict(lambda: [])
        for s in strs:
            sorted_s = "".join(sorted(list(s)))
            acc[sorted_s].append(s)
        return list(acc.values())


def test_case1():
    inp = ["eat","tea","tan","ate","nat","bat"]
    exp = [["bat"],["nat","tan"],["ate","eat","tea"]]

    assert [1, 2, 3] == unordered([3, 2, 1])
    assert exp == unordered(Solution().groupAnagrams(inp))