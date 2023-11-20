# Given an array of integers nums and an integer limit,
# return the size of the longest non-empty subarray such that the absolute difference
# between any two elements of this subarray is less than or equal to limit.
from collections import deque
from dataclasses import dataclass
from typing import List, Optional




class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0

        st = 0
        end = 1

        min_queue = deque()
        max_queue = deque()

        longset_seq = 1
        for seq_num in nums:

            while max_queue and max_queue[-1] < seq_num:
                max_queue.pop()

            max_queue.append(seq_num)

            while min_queue and min_queue[-1] > seq_num:
                min_queue.pop()

            min_queue.append(seq_num)

            for i in range(end - 1, st - 1, -1):
                if abs(nums[i] - seq_num) > limit:
                    st = i + 1
                    break

            end += 1
            longset_seq = max(end - st, longset_seq)

        return max(longset_seq, end - st)


def test_case1():
    nums = [8, 2, 4, 7]
    limit = 4

    assert Solution().longestSubarray(nums, limit) == 2


def test_case2():
    nums = [10, 1, 2, 4, 7, 2]
    limit = 5

    assert Solution().longestSubarray(nums, limit) == 4


def test_case3():
    nums = [4, 2, 2, 2, 4, 4, 2, 2]
    limit = 0

    assert Solution().longestSubarray(nums, limit) == 3

def test_case4():
    nums = [24,12,71,33,5,87,10,11,3,58,2,97,97,36,32,35,15,80,24,45,38,9,22,21,33,68,22,85,35,83,92,38,59,90,42,64,61,15,4,40,50,44,54,25,34,14,33,94,66,27,78,56,3,29,3,51,19,5,93,21,58,91,65,87,55,70,29,81,89,67,58,29,68,84,4,51,87,74,42,85,81,55,8,95,39]
    limit = 87

    assert Solution().longestSubarray(nums, limit) == 25
