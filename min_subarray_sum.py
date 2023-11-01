import sys
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target == 0:
            return 0
        p1 = 0
        p2 = 0
        min_elements = sys.maxsize
        arr_len = len(nums)
        # iter = 0
        s = nums[p1]
        while p1 < arr_len:
            # iter += 1

            if s >= target:
                min_elements = min(min_elements, 1 + p2 - p1)
                s -= nums[p1]
                p1 += 1
            elif p2 < arr_len - 1:
                p2 += 1
                s += nums[p2]
            elif s < target:
                break
            # print(p1, p2)
            if min_elements == 1:
                break

        # print("loops")
        # print(iter)
        # print(f"{iter} / {arr_len}")
        return 0 if min_elements > len(nums) else min_elements


def test_case1():
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    exp = 2
    assert Solution().minSubArrayLen(target, nums) == exp


def test_case2():
    target = 4
    nums = [1, 4, 4]
    exp = 1
    assert Solution().minSubArrayLen(target, nums) == exp


def test_case3():
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    exp = 0
    assert Solution().minSubArrayLen(target, nums) == exp