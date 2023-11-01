class Solution:

    def isValid(self, s: str) -> bool:

        opening = []

        for c in s:
            if c in ["(", "{", "["]:
                opening.append(c)
            else:
                if not opening:
                    return False
                op = opening.pop()
                if op + c not in ["{}", "()", "[]"]:
                    return False

        return True


def tests():
    assert Solution().isValid("({[]})")
    assert Solution().isValid("[()]")
    assert Solution().isValid("[()]{}")
    assert not Solution().isValid("[)]{}")
    assert not Solution().isValid(")()]{}")


