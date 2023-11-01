from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        if goal < 1:
            return True

        for pos in range(goal-1, -1, -1):
            max_jump = nums[pos]
            if goal - pos <= max_jump:
                goal = pos
                if goal == 0:
                    return True

        return False


def test_case1():
    nums = [2, 3, 1, 1, 4]
    assert Solution().canJump(nums)


def test_case2():
    nums = [3, 2, 1, 0, 4]
    assert not Solution().canJump(nums)


def test_case3():
    nums = [0, 1]
    assert not Solution().canJump(nums)