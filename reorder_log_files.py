from typing import List


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        digit_const = [str(i) for i in range(0, 9)]

        def contains_digit(arr):
            for el in arr:
                for l in el:
                    if l in digit_const:
                        return True
            return False

        def comp_key(s):
            parts = s.split(" ")

            log_type = 1 if contains_digit(parts[1:]) else 0
            if log_type == 1:
                return 1, None
            else:
                return 0, parts[1:], parts[0]

        return sorted(logs, key=comp_key)


def test_case1():
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    exp = ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]

    assert Solution().reorderLogFiles(logs) == exp
