# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return str(self.val)


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        tail = head

        list_len = 1

        while tail.next:
            tail = tail.next
            list_len += 1

        tail.next = head

        steps_ahead = list_len * (1 + int(k / list_len)) - k
        tail = head
        for i in range(steps_ahead):
            if i == steps_ahead - 1:
                tmp = tail.next
                tail.next = None
                tail = tmp
            else:
                tail = tail.next

        return tail


def list_to_linked_list(arr) -> Optional[ListNode]:
    head: Optional[ListNode] = None
    current: Optional[ListNode] = None
    for i in arr:
        el = ListNode(i)
        if not head:
            head = el
            current = el
        else:
            current.next = el
            current = el

    return head


def test_case1():
    head = [1, 2, 3, 4, 5]
    k = 2
    exp = [4, 5, 1, 2, 3]
    res = Solution().rotateRight(list_to_linked_list(head), k)
    assert res == list_to_linked_list(exp)


def test_case2():
    head = [0, 1, 2]
    k = 4
    exp = [2, 0, 1]
    res = Solution().rotateRight(list_to_linked_list(head), k)
    assert res == list_to_linked_list(exp)
