class Solution:

    @staticmethod
    def trim(head, t):
        head = head[1:]
        i = 0
        while i < len(head):
            c = head[i]
            if c not in t:
                i += 1
            else:
                break

        return head[i:]

    def minWindow(self, s: str, t: str) -> str:

        acc = []

        head = ""
        head_included = 0
        for i, sym in enumerate(s):
            part_of_the_key = sym in t
            if not head and not part_of_the_key:
                continue

            if part_of_the_key and head.startswith(sym) and head_included == len(t):
                head = Solution.trim(head, t) + sym
            elif part_of_the_key:
                head += sym
                head_included += 1
            else:
                head += sym

            if head_included == len(t):
                acc.append(head)
                head = Solution.trim(head, t)
                head_included -= 1

        return min(acc, key=lambda x: len(x), default="")



def test_case1():
    s = "ADOBECODEBANC"
    t = "ABC"

    exp = "BANC"

    assert Solution().minWindow(s, t) == exp


def test_case2():
    s = "a"
    t = "a"

    exp = "a"

    assert Solution().minWindow(s, t) == exp


def test_case3():
    s = "a"
    t = "aa"

    exp = ""

    assert Solution().minWindow(s, t) == exp

def test_case4():
    s = "aa"
    t = "aa"

    exp = "aa"

    assert Solution().minWindow(s, t) == exp


def test_case5():
    s = "aab"
    t = "aab"

    exp = "aab"

    assert Solution().minWindow(s, t) == exp


def test_case5():
    s = "bba"
    t = "ab"

    exp = "ba"

    assert Solution().minWindow(s, t) == exp