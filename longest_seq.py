from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        memo_last = [nums[0]]
        memo_length = [1]
        for next_num in nums[1:]:
            updated = False
            for i in range(len(memo_last)):
                if next_num > memo_last[i]:
                    memo_last[i] = next_num
                    memo_length[i] = memo_length[i] + 1
                    updated = True
            if not updated:
                memo_last.append(next_num)
                memo_length.append(1)

        return max(memo_length)


def test_case1():
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    exp = 4

    assert Solution().lengthOfLIS(nums) == exp


def test_case2():
    nums = [0, 1, 0, 3, 2, 3]
    exp = 4

    assert Solution().lengthOfLIS(nums) == exp

def test_case3():
    nums = [7,7,7,7,7,7,7]
    exp = 1

    assert Solution().lengthOfLIS(nums) == exp