from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"({self.val})"

    def __repr__(self):
        return f"({self.val})"


class Solution:

    @staticmethod
    def fold_tree(root: Optional[TreeNode]):
        if not root:
            return []
        else:
            left = Solution.fold_tree(root.left)
            center = [root.val]

            right = Solution.fold_tree(root.right)

            return left + center + right

    @staticmethod
    def traverse_stack(root: TreeNode, d: int):
        left = root
        left_stack = deque([left])

        while left.left:
            left = left.left
            left_stack.append(left)

        min_stack = []

        buf = []
        while d > 0:
            el = left_stack.pop()
            right_side = [el.val] + Solution.fold_tree(el.right)
            buf = buf + right_side
            d -= len(right_side)

        return buf

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        b = Solution.traverse_stack(root, k)

        return b[k-1]


def to_graph_level(arr: List[int]):
    node_arr = [TreeNode(x) if x else None for x in arr]

    root = node_arr.pop(0)
    stack = deque()
    stack.append(root)

    while node_arr:
        left = node_arr.pop(0)
        right = node_arr.pop(0) if node_arr else None

        local_root = stack.popleft()
        if local_root:
            local_root.left = left
            local_root.right = right

        stack.append(left)
        stack.append(right)

    return root


def test_case1():
    root_arr = [3, 1, 4, None, 2]
    k = 1

    root = to_graph_level(root_arr)
    assert Solution().kthSmallest(root, k) == 1


def test_case2():
    root_arr = [3, 1, 4, None, 2]
    k = 2

    root = to_graph_level(root_arr)
    assert Solution().kthSmallest(root, k) == 2


def test_case3():
    root_arr = [3, 1, 4, None, 2]
    k = 3

    root = to_graph_level(root_arr)
    assert Solution().kthSmallest(root, k) == 3


def test_case4():
    root_arr = [5, 3, 6, 2, 4, None, None, 1]
    k = 3
    exp = 3

    root = to_graph_level(root_arr)
    assert Solution().kthSmallest(root, k) == exp