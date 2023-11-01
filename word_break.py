from typing import List


class Solution:
    def wordBreak(self, s: str, word_dict: List[str]):
        stack = [s]
        visited = {s}
        while stack:
            s = stack.pop()
            for w in word_dict:
                if s.startswith(w):
                    new_s = s.removeprefix(w)
                    if not new_s:
                        return True
                    if new_s not in visited:
                        stack.append(new_s)
                    visited.add(new_s)

        return False

def test_case1():
    s = "leetcode"
    word_dict = ["leet", "code"]

    assert Solution().wordBreak(s, word_dict)


def test_case2():
    s = "applepenapple"
    word_dict = ["apple", "pen"]

    assert Solution().wordBreak(s, word_dict)


def test_case3():
    s = "catsandog"
    word_dict = ["cats", "dog", "sand", "and", "cat"]

    assert not Solution().wordBreak(s, word_dict)


def test_case4():
    s = "bb"
    word_dict = ["a", "b", "bbb", "bbbb"]

    assert Solution().wordBreak(s, word_dict)


def test_case5():
    s = "aaaaaaa"
    word_dict = ["aaaa", "aaa"]

    assert Solution().wordBreak(s, word_dict)
