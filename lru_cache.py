from collections import defaultdict, deque
from typing import Optional, Dict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.stack = deque()
        self.dict: Dict[int, int] = defaultdict(lambda: -1)
        self.lru = deque()

    def update_lru(self, key) -> None:
        if key in self.lru:
            self.lru.remove(key)
            self.lru.appendleft(key)
        elif len(self.lru) + 1 > self.capacity:
            rem = self.lru.pop()
            del self.dict[rem]
            self.lru.appendleft(key)
        else:
            self.lru.appendleft(key)

    def evict_lru(self) -> int:
        return self.lru.pop()

    def get(self, key: int) -> int:
        # set key to the last position of lru array
        if key in self.dict:
            self.update_lru(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.stack) < self.capacity:
            self.update_lru(key)
            self.stack.append(key)
        else:
            remove = self.evict_lru()
            del self.dict[remove]
            self.update_lru(key)

        self.dict[key] = value


def test_case1():
    ops = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    vals = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    exp = [None, None, None, 1, None, -1, None, -1, 3, 4]

    cache = None
    for op, val, ex in zip(ops, vals, exp):
        match op:
            case "LRUCache":
                cache = LRUCache(val[0])
            case "put":
                cache.put(val[0], val[1])
            case "get":
                res = cache.get(val[0])
                assert res == ex


def test_case2():
    ops = ["LRUCache", "get", "put", "get", "put", "put", "get", "get"]
    vals = [[2], [2], [2, 6], [1], [1, 5], [1, 2], [1], [2]]

    exp = [None, -1, None, -1, None, None, 2, 6]

    cache = None
    print()
    for op, val, ex in zip(ops, vals, exp):
        print(op, val)
        match op:
            case "LRUCache":
                cache = LRUCache(val[0])
            case "put":
                cache.put(val[0], val[1])
            case "get":
                res = cache.get(val[0])
                assert res == ex
