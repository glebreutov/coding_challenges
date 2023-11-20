from typing import List, Optional


class Solution:

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        if len(nums) == 1:
            return [str(nums[0])]

        stack = [[nums[0], nums[0]]]
        i = 1
        while i < len(nums):
            cv = nums[i]
            _, int_end = stack[-1]

            if cv - int_end == 1:
                stack[-1][1] = cv
            else:
                stack.append([cv, cv])
            i += 1

        return [str(a) if a == b else f"{a}->{b}" for a, b in stack]


def test_case1():
    nums = [0, 1, 2, 4, 5, 7]
    exp = ["0->2", "4->5", "7"]
    assert Solution().summaryRanges(nums) == exp


def test_case2():
    nums = [0, 2, 3, 4, 6, 8, 9]
    exp = ["0", "2->4", "6", "8->9"]
    assert list(Solution().summaryRanges(nums)) == exp
