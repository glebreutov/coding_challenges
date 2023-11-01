from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        pv = nums[0]
        repeats = 1
        while i < len(nums):
            if pv == nums[i]:
                repeats += 1
                if repeats > 2:
                    end_val = nums[-1]
                    nums[i] = end_val
                else:
                    i += 1
            else:
                pv = nums[i]
                i += 1
                repeats = 1

        return len(nums)


def test_case1():
    nums = [1, 1, 1, 2, 2, 3]
    exp_len = 2
    exp_res = [1, 1, 2, 2, 3]

    uq_len = Solution().removeDuplicates(nums)
    # assert uq_len == exp_len
    assert nums == exp_res


def test_case2():
    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    exp_len = 2
    exp_res = [0, 0, 1, 1, 2, 3, 3]

    uq_len = Solution().removeDuplicates(nums)
    # assert uq_len == exp_len
    assert nums == exp_res
