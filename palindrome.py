class Solution:
    def isPalindrome(self, s: str) -> bool:

        p1 = 0
        p2 = len(s) - 1
        while p1 < p2:
            a = s[p1].lower()
            b = s[p2].lower()

            if not (a.isalpha() or a.isalnum()):
                p1 += 1
                continue

            if not (b.isalpha() or b.isalnum()):
                p2 -= 1
                continue

            if a != b:
                return False

            p1 += 1
            p2 -= 1

        return True


def test_case1():
    assert Solution().isPalindrome("A man, a plan, a canal: Panama")


def test_case2():
    assert not Solution().isPalindrome("1race a car1")


def test_case3():
    assert Solution().isPalindrome(" ")


def test_case4():
    assert Solution().isPalindrome("aa")
