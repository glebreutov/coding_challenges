from typing import List, Set


class Solution:

    def cycle_detector(self, g, course_idx, safe_nodes: Set[int], acc: Set[int] = set()):
        print(f"check {course_idx}, acc = {acc}")
        if course_idx in safe_nodes:
            return False, acc

        if course_idx in acc:
            return True, acc

        for dep in g[course_idx]:
            print(f"check child {dep}")
            is_cycle, _ = self.cycle_detector(g, dep, safe_nodes, acc | {course_idx})
            if is_cycle:
                return True, acc | {course_idx}

        return False, acc

    def build_graph(self, num_courses: int, prerequisites: List[List[int]]):
        g = [set() for _ in range(num_courses)]

        for rule in prerequisites:
            course_idx = rule[0]
            prereq = rule[1]
            g[course_idx].add(prereq)

        return g

    def canFinish(self, num_courses: int, prerequisites: List[List[int]]) -> bool:
        # g is the graph which represents what preconditions course has
        g = self.build_graph(num_courses, prerequisites)

        safe_nodes = set()
        for idx in range(num_courses):
            is_cycle, nodes = self.cycle_detector(g, idx, safe_nodes)
            if is_cycle:
                return False
            else:
                safe_nodes.add(idx)
                safe_nodes.update(nodes)

        return True


def test_case1():
    numCourses = 2
    prerequisites = [[1, 0]]

    assert Solution().canFinish(numCourses, prerequisites)


def test_case2():
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]

    assert not Solution().canFinish(numCourses, prerequisites)


def test_case3():
    prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]
    numCourses = 5

    assert Solution().canFinish(numCourses, prerequisites)


def test_case4():
    prereq = [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]
    numCourses = 4

    assert not Solution().canFinish(numCourses, prereq)


def test_case5():
    prereq = [[1, 0], [0, 3], [0, 2], [3, 2], [2, 5], [4, 5], [5, 6], [2, 4]]
    numCourses = 7

    assert Solution().canFinish(numCourses, prereq)


def test_case_cd1():
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]
    g = Solution().build_graph(numCourses, prerequisites)
    isc, _ = Solution().cycle_detector(g, 0, set())
    assert isc


def test_case_cd2():
    numCourses = 1
    prerequisites = [[0, 0]]
    g = Solution().build_graph(numCourses, prerequisites)
    isc, _ = Solution().cycle_detector(g, 0, set())
    assert isc


def test_case_cd3():
    numCourses = 2
    prerequisites = [[0, 1]]
    g = Solution().build_graph(numCourses, prerequisites)
    isc, _ = Solution().cycle_detector(g, 0, set())
    assert not isc


def test_case_cd4():
    numCourses = 4
    prereq = [[2, 0], [1, 0], [3, 1], [3, 2], [1, 3]]
    g = Solution().build_graph(numCourses, prereq)
    isc, _ = Solution().cycle_detector(g, 1, set())
    assert isc
