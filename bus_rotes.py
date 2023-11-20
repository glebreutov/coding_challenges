from collections import defaultdict
from dataclasses import dataclass
from typing import List, Dict, Set


class Solution:

    @staticmethod
    def build_graph(routes: List[List[int]]):
        stop_map = defaultdict(set)
        exchange_map = defaultdict(set)

        for i, stops in enumerate(routes):
            if len(stops) == 1:
                continue
            for stop in stops:
                stop_map[stop].add(i)


        for _, bus_nums in stop_map.items():
            if len(bus_nums) > 1:
                for a in bus_nums:
                    for b in bus_nums:
                        if a != b:
                            exchange_map[a].add(b)
                            exchange_map[b].add(a)

        return stop_map, exchange_map

    @staticmethod
    def bfs(bus_exchange_map: Dict[int, int], source_bus_nums: Set[int], dest_bus_nums: Set[int], max_stops: int, count: int = 1):
        if source_bus_nums.intersection(dest_bus_nums):
            return count
        elif count < max_stops:
            next_source = {x for bn in source_bus_nums for x in bus_exchange_map[bn] if bn in bus_exchange_map}
            next_dest = {x for bn in dest_bus_nums for x in bus_exchange_map[bn] if bn in bus_exchange_map}
            if len(next_source) < len(next_dest):
                return Solution.bfs(bus_exchange_map, next_source, dest_bus_nums, max_stops, count + 1)
            else:
                return Solution.bfs(bus_exchange_map, source_bus_nums, next_dest, max_stops, count + 1)
        else:
            return -1

    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
        # graph + bfs
        stop_bus_map, bus_exchange_map = Solution.build_graph(routes)

        return Solution.bfs(bus_exchange_map, stop_bus_map[source], stop_bus_map[target], len(routes))


def test_case1():
    routes = [[1, 2, 7], [3, 6, 7]]
    source = 1
    target = 6

    assert Solution().numBusesToDestination(routes, source, target) == 2


def test_case2():
    routes = [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]]
    source = 15
    target = 12
    assert Solution().numBusesToDestination(routes, source, target) == -1


def test_case3():
    routes = [[0, 1, 6, 16, 22, 23], [14, 15, 24, 32], [4, 10, 12, 20, 24, 28, 33], [1, 10, 11, 19, 27, 33], [11, 23, 25, 28],
     [15, 20, 21, 23, 29], [29]]
    source = 4
    target = 21
    assert Solution().numBusesToDestination(routes, source, target) == 2