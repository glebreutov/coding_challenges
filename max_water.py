from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_w = 0
        for x1, y1 in enumerate(height):
            for x2, y2 in enumerate(height):
                max_w = max(min(y1, y2) * abs(x1 - x2), max_w)

        x1 = 0
        x2 = 1
        while True:
            y1 = height[x1]
            y2 = height[x2]

            vol = min(y1, y2) * abs(x1 - x2)
            max_w = max(vol, max_w)

            if y1 > y2:
                (new_x2, new_y2) = max([(i, h) for i, h in enumerate(height)], key=lambda x: x[1])



