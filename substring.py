import sys


class Solution:

    # returns position of a duplicate symbol
    def find_limit(self, seq, char):
        for i in range(len(seq)):
            if char == seq[i]:
                return i

        return len(seq)

    # returns length of unique sequence
    def unique_length(self, s: str):
        p1 = 0
        seg_len = len(s)
        while p1 < seg_len:
            a = s[p1]
            seg_len = p1 + 1 + self.find_limit(s[p1 + 1:seg_len], a)
            p1 += 1

        return seg_len

    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        start = 0
        while len(s) > start:
            segment_len = self.unique_length(s[start:])
            max_length = max(max_length, segment_len)
            start += 1

        return max_length


def test_cases_limit():
    assert Solution().find_limit("a", "a") == 0
    assert Solution().find_limit("aa", "a") == 0
    assert Solution().find_limit("aaa", "a") == 0
    assert Solution().find_limit("ba", "a") == 1
    assert Solution().find_limit("cba", "a") == 2
    assert Solution().find_limit("dcba", "a") == 3


def test_cases_segment():
    assert Solution().unique_length("a") == 1
    assert Solution().unique_length("aa") == 1
    assert Solution().unique_length("aaa") == 1
    assert Solution().unique_length("ba") == 2
    assert Solution().unique_length("cba") == 3
    assert Solution().unique_length("dcba") == 4
    assert Solution().unique_length("ddcba") == 1




def test_case8():
    i = "abcabcbb"
    exp = 3
    assert Solution().lengthOfLongestSubstring(i) == exp


def test_case9():
    i = "bbbbb"
    exp = 1
    assert Solution().lengthOfLongestSubstring(i) == exp


def test_case10():
    i = "pwwkew"
    exp = 3
    assert Solution().lengthOfLongestSubstring(i) == exp


def test_case11():
    i = "dvdf"
    exp = 3
    assert Solution().lengthOfLongestSubstring(i) == exp