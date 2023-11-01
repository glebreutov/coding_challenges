# https://leetcode.com/problems/climbing-stairs/?envType=study-plan-v2&envId=top-interview-150
class Solution:

    def climbStairs(self, n: int) -> int:
        minus_two_steps = 1
        minus_one_step = 1

        j = 1

        while j < n:
            current_step = minus_two_steps + minus_one_step
            minus_two_steps = minus_one_step
            minus_one_step = current_step
            j += 1
        return minus_one_step

