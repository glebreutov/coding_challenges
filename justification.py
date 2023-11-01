from typing import List


class Solution:

    def justify_left(self, max_width, str_acc):
        res = str_acc[0]
        for w in str_acc[1:]:
            res += " " + w

        return res + " " * (max_width - len(res))

    def justify(self, max_width, str_acc, str_acc_len):
        if len(str_acc) == 1:
            return self.justify_left(max_width, str_acc)
        else:
            return self.justify_even(max_width, str_acc, str_acc_len)

    def space_calc2(self, spaces_amount, word_count, word_idx):
        spaces_per_word = int(spaces_amount / (word_count - 1))
        reminder = spaces_amount - (word_count - 1) * spaces_per_word

        return spaces_per_word + (1 if word_idx < reminder else 0)

    __cache = [" " * i for i in range(100)]

    def spacer_cache(self, size):
        if size < len(self.__cache):
            return self.__cache[size]
        else:
            return " " * size

    def justify_even(self, max_width, str_acc, str_acc_len):
        spaces_amount = max_width - str_acc_len
        res = str_acc[0]
        word_num = 0

        for w in str_acc[1:]:
            spacer = self.spacer_cache(1 + self.space_calc2(spaces_amount, len(str_acc), word_num))
            res += spacer + w

            word_num += 1
        return res

    def fullJustify(self, words: List[str], max_width: int) -> List[str]:
        res = []
        st = 0
        end = 0
        c_len = -1
        for w in words:
            if c_len + 1 + len(w) > max_width:
                res.append(self.justify(max_width, words[st:end], c_len))
                c_len = len(w)
                st = end
            else:
                c_len += len(w) + 1
            end += 1

        res.append(self.justify_left(max_width, words[st:]))
        return res


def test_case1():
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    maxWidth = 16
    exp = [
        "This    is    an",
        "example  of text",
        "justification.  "
    ]

    assert Solution().fullJustify(words, maxWidth) == exp


def test_case2():
    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    maxWidth = 16
    exp = [
        "What   must   be",
        "acknowledgment  ",
        "shall be        "
    ]

    assert Solution().fullJustify(words, maxWidth) == exp


def test_case3():
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
             "Art", "is", "everything", "else", "we", "do"]
    maxWidth = 20

    exp = [
        "Science  is  what we",
        "understand      well",
        "enough to explain to",
        "a  computer.  Art is",
        "everything  else  we",
        "do                  "
    ]

    assert Solution().fullJustify(words, maxWidth) == exp


def test_case4():
    words = ["The", "important", "thing", "is", "not", "to", "stop", "questioning.", "Curiosity", "has", "its", "own",
             "reason", "for", "existing."]
    maxWidth = 17

    exp = ["The     important",
           "thing  is  not to",
           "stop questioning.",
           "Curiosity has its",
           "own   reason  for",
           "existing.        "]

    assert Solution().fullJustify(words, maxWidth) == exp


def test_case_spacer1():
    inp = 'example  of text'

    assert Solution().space_calc2(spaces_amount=1, word_count=3, word_idx=0) == 1
    assert Solution().space_calc2(spaces_amount=1, word_count=3, word_idx=1) == 0


def test_case_spacer3():
    inp = 'Science  is  what we'

    assert Solution().space_calc2(spaces_amount=1, word_count=3, word_idx=0) == 1


def test_case_spacer2():
    inp = 'own   reason  for',
    assert Solution().space_calc2(spaces_amount=3, word_count=3, word_idx=0) == 2
    assert Solution().space_calc2(spaces_amount=3, word_count=3, word_idx=1) == 1
