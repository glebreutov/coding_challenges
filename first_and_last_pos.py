# [5,7,7,8,8,10]
# [5,7,7,_8_,8,10]
from typing import List


# [5,7,7,8,8,10]
# [5,7,7,_8_,8,10]

# [5,_7_,7]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        st = 0
        end = len(nums) - 1
        median = 0

        while st <= end and st > -1 and end < len(nums):
            median = st + (end - st) // 2
            median_value = nums[median]
            if median_value > target:
                end = median - 1
            elif median_value < target:
                st = median + 1
            elif median_value == target and len(nums) > median + 1 and nums[median + 1] > target:
                break
            else:
                st = median + 1

        target_end = median

        st = 0
        end = target_end

        while st <= end and st > -1 and end < len(nums):
            median = st + (end - st) // 2
            median_value = nums[median]
            if median_value > target:
                end = median - 1
            elif median_value < target:
                st = median + 1

            elif median_value == target and median - 1 >= 0 and nums[median - 1] < target:
                break
            else:
                end = median - 1

        target_st = median

        if nums[target_st] != target:
            return [-1, -1]
        else:
            return [target_st, target_end]


def test_case1():
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    exp = [3, 4]

    assert Solution().searchRange(nums, target) == exp

def test_case2():
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    exp = [-1, -1]

    assert Solution().searchRange(nums, target) == exp


def test_case3():
    nums = [1]
    target = 1
    exp = [0, 0]

    assert Solution().searchRange(nums, target) == exp