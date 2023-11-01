from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        pv = nums[0]
        while i < len(nums):
            if pv == nums[i]:
                del nums[i]
            else:
                pv = nums[i]
                i += 1

        return len(nums)


def test_case1():
    nums = [1, 1, 2]
    exp_len = 2
    exp_res = [1, 2]

    uq_len = Solution().removeDuplicates(nums)
    assert uq_len == exp_len
    assert nums == exp_res