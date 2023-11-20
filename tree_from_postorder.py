# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @staticmethod
    def fold_right(inorder: List[int], postorder: List[int]):
        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])

        left = inorder[0]
        top_node = inorder[1]

        next_postord = postorder[1]
        if top_node == next_postord:

            right_node = None
            return TreeNode(top_node, TreeNode(left), right_node), inorder[2:], postorder[2:]
        else:
            right_node = postorder[2]
            return TreeNode(top_node, TreeNode(left), TreeNode(right_node)), inorder[3:], postorder[3]


    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        while inorder:
            left_node, inorder, postorder = Solution.fold_right(inorder, postorder)
            i = 0
        pass







def test_case1():
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    # Output: [3, 9, 20, null, null, 15, 7]
    v = Solution().buildTree(inorder, postorder)
    assert v
