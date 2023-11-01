from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Node:
    num: int
    left: Optional
    right: Optional


def print_binary_tree_inorder(root: Node):
    if root:
        # Recursively print the left subtree
        print_binary_tree_inorder(root.left)

        # Print the current node's value
        print(root.num, end=" ")

        # Recursively print the right subtree
        print_binary_tree_inorder(root.right)


class Solution:

    def test_len(self, nodes, n):
        return len(set(nodes)) == len(nodes) and len(nodes) == n - 1

    def test_connectivity(self, nodes):
        prev_val = 0
        for n in nodes:
            if n - prev_val != 1:
                return False
            prev_val = n
        return True

    def children(self, i: int, left_children: List[int], right_children: List[int]):
        left_child = left_children[i]
        right_child = right_children[i]

        return left_child if left_child > -1 else None, right_child if right_child > -1 else None

    def build_graph(self, i: int, left_children: List[int], right_children: List[int]):
        root = Node(i, None, None)
        left_child, right_child = self.children(i, left_children, right_children)
        lc = None
        if left_child is not None:
            lc = self.build_graph(left_child, left_children, right_children)

        rc = None
        if right_child is not None:
            rc = self.build_graph(right_child, left_children, right_children)

        root.left = lc
        root.right = rc
        return root

    def find_root(self, n, leftChild, rightChild):
        children = set(leftChild) | set(rightChild)

        for i in range(n):
            if i not in children:
                return i

        return -1

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root = self.find_root(n, leftChild, rightChild)

        # nodes = self.build_graph(root, leftChild, rightChild)

        nodes = sorted([x for x in leftChild + rightChild + [root] if x >= 0])
        one_parent = len(set(nodes)) == len(nodes)

        are_connected = self.test_connectivity(nodes)
        return root > -1 and one_parent and are_connected


def test_case1():
    n = 4
    left_child = [1, -1, 3, -1]
    right_child = [2, -1, -1, -1]

    s = Solution()
    root = s.build_graph(0, left_child, right_child)
    print_binary_tree_inorder(root)
    assert s.validateBinaryTreeNodes(n, left_child, right_child)


def test_case2():
    n = 4
    left_child = [1, -1, 3, -1]
    right_child = [2, 3, -1, -1]

    s = Solution()
    root = s.build_graph(0, left_child, right_child)

    assert not s.validateBinaryTreeNodes(n, left_child, right_child)


def test_case3():
    n = 4
    left_child = [3, -1, 1, -1]
    right_child = [-1, -1, 0, -1]
    s = Solution()

    assert s.validateBinaryTreeNodes(n, left_child, right_child)
