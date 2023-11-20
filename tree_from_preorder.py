# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = preorder[0]
        root_pos = inorder.index(root)

        left_inord = inorder[:root_pos]
        right_inord = inorder[1+root_pos:]

        left_pre = preorder[1:1 + len(left_inord)]
        right_pre = preorder[1+len(left_inord):]
        return TreeNode(root, self.buildTree(left_pre, left_inord), self.buildTree(right_pre, right_inord))



def test_case1():
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    # Output: [3, 9, 20, null, null, 15, 7]
    v = Solution().buildTree(preorder, inorder)
    assert v
