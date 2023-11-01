import string


class Solution:

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alpabet_length = 27
        cache_counter = [0 for _ in range(alpabet_length)]
        cache_alphabet = [False for _ in range(alpabet_length)]
        sym_counter = 0

        ransom_alphabet_len = 0
        iter = 0
        for c in ransomNote:
            sym_idx = ord(c) - 97
            iter += 1
            if cache_counter[sym_idx] == 0:
                ransom_alphabet_len += 1
                cache_alphabet[sym_idx] = True

            cache_counter[sym_idx] -= 1

        for c in magazine:
            iter += 1
            sym_idx = ord(c) - 97
            if not cache_alphabet[sym_idx]:
                continue

            cache_counter[sym_idx] += 1

            if cache_counter[sym_idx] == 0:
                sym_counter += 1

            if sym_counter == ransom_alphabet_len:
                print()
                print(f"{iter} / {len(ransomNote)} / {len(magazine)}")
                return True

        print()
        print(f"{iter} / {len(ransomNote)} / {len(magazine)}")
        return sym_counter == ransom_alphabet_len


def test_case1():
    ransomNote = "a"
    magazine = "b"

    assert not Solution().canConstruct(ransomNote, magazine)


def test_case2():
    ransomNote = "aa"
    magazine = "ab"

    assert not Solution().canConstruct(ransomNote, magazine)

def test_case3():
    ransomNote = "aa"
    magazine = "aab"

    assert Solution().canConstruct(ransomNote, magazine)


def test_case4():
    ransomNote = "givusthemoney"
    magazine = ransomNote + string.ascii_lowercase + string.ascii_lowercase


    assert Solution().canConstruct(ransomNote, magazine)