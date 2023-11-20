from typing import List


class Solution:

    def check_tails(self, nums: List[int], target: int):
        last_idx = len(nums) - 1
        a = nums[0]
        if a == target:
            return 0
        if a > target:
            return -1

        b = nums[last_idx]
        if b == target:
            return last_idx
        if target > b:
            return last_idx + 1

        return None

    def searchInsert(self, nums: List[int], target: int) -> int:
        lb = 0
        if not nums:
            return 0

        # one and more
        if target <= nums[lb]:
            return lb

        rb = len(nums) - 1

        if nums[rb] == target:
            return rb

        if nums[rb] < target:
            return rb + 1

        dist = rb - lb

        if dist == 1:
            return 1
        elif dist == 2:








def test_c1():
    nums = []
    target = 5
    exp = 0
    assert Solution().searchInsert(nums, target) == exp


def test_c2():
    nums = [6]
    target = 5
    exp = 0
    assert Solution().searchInsert(nums, target) == exp


def test_c3():
    nums = [5]
    target = 5
    exp = 0
    assert Solution().searchInsert(nums, target) == exp


def test_c3():
    nums = [4]
    target = 5
    exp = 1
    assert Solution().searchInsert(nums, target) == exp


def test_case1():
    nums = [1, 3, 5, 6]
    target = 5

    assert Solution().searchInsert(nums, target) == 2


def test_case2():
    nums = [1, 3, 5, 6]
    target = 2

    assert Solution().searchInsert(nums, target) == 1


def test_case3():
    nums = [1, 3, 5, 6]
    target = 7

    assert Solution().searchInsert(nums, target) == 4


def test_case4():
    nums = [1, 3, 5, 6]
    target = 0

    assert Solution().searchInsert(nums, target) == 0


def test_case5():
    nums = [1, 3, 5]
    target = 4

    assert Solution().searchInsert(nums, target) == 2


def test_case6():
    nums = [1, 3, 5, 7, 11, 14, 20, 50]
    target = 13

    assert Solution().searchInsert(nums, target) == 5
