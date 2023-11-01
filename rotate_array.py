from typing import List


class Solution:

    def shift_right(self, nums, st, end):
        p_val = nums[st]
        for t in range(st + 1, min(end, len(nums))):
            tmp = nums[t]
            nums[t] = p_val
            p_val = tmp

    def rotate_slow(self, nums: List[int], k: int) -> None:
        if len(nums) < 2:
            return
        head_idx = 0
        ops = k % len(nums)
        while head_idx < ops:
            tail_idx = len(nums) - ops + head_idx

            tail = nums[tail_idx]

            for t in range(tail_idx, head_idx, -1):
                nums[t] = nums[t-1]

            nums[head_idx] = tail

            head_idx += 1

    def rotate(self, nums: List[int], k: int) -> None:
        if len(nums) < 2:
            return

        ops = k % len(nums)
        cache = nums[-ops:]

        for t in range(len(nums)-1, ops-1, -1):
            nums[t] = nums[t - ops]

        i = 0
        for c in cache:
            nums[i] = c
            i += 1


def test_case1():
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    Solution().rotate(nums, k)
    assert nums == [5, 6, 7, 1, 2, 3, 4]


def test_case2():
    nums = [-1, -100, 3, 99]
    k = 2
    Solution().rotate(nums, k)
    assert nums == [3, 99, -1, -100]


def test_case3():
    nums = [1]
    k = 1
    Solution().rotate(nums, k)
    assert nums == [1]


def test_case4():
    nums = [1,2]
    k = 1
    Solution().rotate(nums, k)
    assert nums == [2, 1]


def test_case5():
    nums = [1, 2]
    k = 3
    Solution().rotate(nums, k)
    assert nums == [2, 1]

