from dataclasses import dataclass
from typing import Optional
from ascii_tree import make_and_print_tree


@dataclass
class AVLNode:
    val: int
    height: int
    left: Optional = None
    right: Optional = None


class AVLUtil:

    @staticmethod
    def find_value(root: Optional[AVLNode], key: int) -> Optional[AVLNode]:
        if not root:
            return None
        elif root.val == key:
            return root
        elif root.val > key:
            return AVLUtil.find_value(root.left, key)
        else:
            return AVLUtil.find_value(root.right, key)

    @staticmethod
    def get_height(root: AVLNode) -> int:
        if not root:
            return 0
        else:
            return root.height

    @staticmethod
    def get_balance(root: AVLNode) -> int:
        return AVLUtil.get_height(root.left) - AVLUtil.get_height(root.right)

    @staticmethod
    def rotate_left(root: AVLNode) -> AVLNode:
        if not root.left:
            return root

        # define new root
        new_root = root.left
        left_right = new_root.right

        new_root.right = root
        root.left = left_right

        return new_root

    @staticmethod
    def rotate_right(root: AVLNode) -> AVLNode:
        if not root.right:
            return root

        # define new root
        new_root = root.right
        right_left = new_root.left

        new_root.left = root
        root.right = right_left

        return new_root

    @staticmethod
    def insert(root: Optional[AVLNode], key: int) -> AVLNode:
        if not root:
            return AVLNode(key, 1)
        elif root.val == key:
            return root

        if root.val > key:
            root.left = AVLUtil.insert(root.left, key)
        else:
            root.right = AVLUtil.insert(root.right, key)

        root.height = 1 + max(AVLUtil.get_height(root.right), AVLUtil.get_height(root.left))
        balance = AVLUtil.get_balance(root)
        if balance < -1:
            return AVLUtil.rotate_right(root)
        elif balance > 1:
            return AVLUtil.rotate_left(root)
        else:
            return root


def test_case1():
    values = [8, 5, 4, 2, 10, 15,1 ,2, 3]
    root = None
    for v in values:
        root = AVLUtil.insert(root, v)

    make_and_print_tree(root, lambda x: f"v={x.val}, h={x.height}, b={AVLUtil.get_balance(x)}",
                        lambda x: [x for x in [x.left, x.right] if x])
