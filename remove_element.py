from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            cv = nums[i]
            if cv == val:
                del nums[i]
            else:
                i += 1

        return len(nums)


def test_case1():
    nums = [3, 2, 2, 3]
    val = 3
    expected = [2, 2]
    removals = Solution().removeElement(nums, val)

    assert nums == expected


def test_case2():
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    expected = [0, 1, 3, 0, 4]
    removals = Solution().removeElement(nums, val)

    assert nums == expected
