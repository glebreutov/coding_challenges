# https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=top-interview-150

from typing import List


class Solution:
    def __init__(self):
        self.ops = 0
        self.cache = {}

    def rob(self, nums: List[int]) -> int:
        rob1 = 0
        rob2 = 0

        for n in nums:
            temp = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = temp

        return max(rob1, rob2)


def test_case1():
    nums = [1, 2, 3, 1]
    exp = 4

    assert Solution().rob(nums) == exp


def test_case2():
    nums = [2, 7, 9, 3, 1]
    exp = 12

    assert Solution().rob(nums) == exp


def test_case3():
    nums = [226, 174, 214, 16, 218, 48, 153, 131, 128, 17, 157, 142, 88, 43, 37, 157, 43, 221, 191, 68, 206, 23, 225,
            82, 54, 118, 111, 46, 80, 49, 245, 63, 25, 194, 72, 80, 143, 55, 209, 18, 55, 122, 65, 66, 177, 101, 63,
            201, 172, 130, 103, 225, 142, 46, 86, 185, 62, 138, 212, 192, 125, 77, 223, 188, 99, 228, 90, 25, 193, 211,
            84, 239, 119, 234, 85, 83, 123, 120, 131, 203, 219, 10, 82, 35, 120, 180, 249, 106, 37, 169, 225, 54, 103,
            55, 166, 124]
    assert Solution().rob(nums) > 0


