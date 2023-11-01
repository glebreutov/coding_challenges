from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0
        end_of_array = False

        while p2 < n:
            if p1 < m:
                a = nums1[p1]
                end_of_array = False
            else:
                end_of_array = True

            b = nums2[p2]
            if end_of_array or b <= a:
                print(nums1)
                nums1.insert(p1, b)
                p1 += 1
                print("...", nums1[p1:])
                del nums1[-1]
                p2 += 1

            else:
                p1 += 1



def test_case1():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    Solution().merge(nums1, m, nums2, n)

    assert nums1 == [1, 2, 2, 3, 5, 6]


def test_case2():
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0

    Solution().merge(nums1, m, nums2, n)

    assert nums1 == [1]


def test_case3():
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1

    Solution().merge(nums1, m, nums2, n)

    assert nums1 == [1]