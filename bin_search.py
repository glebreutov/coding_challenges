from typing import List


class Solution:
    def check_bounds(self, nums: List[int], target: int):
        lb = nums[0]
        ub = nums[-1]

        if lb > target:
            return 0

        if lb == target:
            return 0

        if ub < target:
            return len(nums)

        if ub == target:
            return len(nums) - 1

        return None

    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = self.check_bounds(nums, target)
        if idx is not None:
            return idx

        p = int(len(nums) / 2)
        if nums[p] == target:
            return p
        if abs(nums[p] - target) == 1:
            return p - nums[p] + target

        if nums[p] > target:
            return self.searchInsert(nums[:p], target)
        else:
            return p + self.searchInsert(nums[p:], target)


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
