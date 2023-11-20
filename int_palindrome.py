from typing import List


class Solution:

    @staticmethod
    def reduce_left(left_arr: List[int]):
        i = len(left_arr) - 1
        while i > -1:
            if i > 0 and left_arr[i] > 0:
                left_arr[i] = left_arr[i] - 1
                return left_arr
            if i == 0 and left_arr[i] > 1:
                left_arr[i] = left_arr[i] - 1
                return left_arr
            i -= 1

        return [9] * (len(left_arr) - 1)



    def nearestPalindromic(self, n: str) -> str:
        side = int(len(n) / 2)
        is_even = len(n) % 2 == 0
        if is_even:
            left_side = n[:side]
            right_side = n[side:]
            center = ""
        else:
            left_side = n[:side]
            right_side = n[1+side:]
            center = n[side]

        if not left_side:
            return str(int(center) - 1)

        int_left = list(map(int, list(left_side)))
        int_right = list(map(int, list(right_side)))

        rev_left = list(reversed(int_left))
        diff = min([a - b for a, b in zip(int_right, rev_left)])

        if diff >= 0:
            return left_side + center + "".join([str(x) for x in rev_left])
        else:
            new_left = [str(x) for x in Solution.reduce_left(int_left)]
            return "".join(new_left) + center + "".join(reversed(new_left))

def test_case1():
    n = "123"
    e = "121"

    assert Solution().nearestPalindromic(n) == e

def test_case2():
    n = "1"
    e = "0"
    assert Solution().nearestPalindromic(n) == e

def test_case3():
    n = "1213"
    e = "1111"
    assert Solution().nearestPalindromic(n) == e