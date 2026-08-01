from collections import defaultdict, deque
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        """
        Input: n = 3, relations = [[1,3],[2,3]]
        adj_list = {
        1:[3], 2:[3], 3:[]
        }
        output: 2
        1 -> 3
        2 -> 3
        indegree = [-1,0,0,2]
        queue = [1,2]
        time O(V+E) ~ O(n+e) and e here is at most n-1 where a course can point to every other course so time simplfied is O(n)
        space: our queue may grow to size n + taken set() size which grows up to n + in_degree arr as large as n + adj_list will have at most n keys and n-1 values per key (meaning that every course could have edges to every other course) so O(n^2). So in the worst case space would take O(n^2)
        """
        adj_list = defaultdict(list)
        in_degree = [0 for _ in range(n+1)]
        in_degree[0] = -1
        for prereq, course in relations:
            adj_list[prereq].append(course)
            in_degree[course] += 1
        queue = deque()
        for course, prereq in enumerate(in_degree):
            if prereq == 0:
                queue.append(course)
        semester = 0
        taken = set()
        while queue:
            semester += 1
            for _ in range(len(queue)):
                this_course = queue.popleft()
                taken.add(this_course)
                for next_course in adj_list[this_course]:
                    in_degree[next_course] -= 1
                    if in_degree[next_course] == 0:
                        queue.append(next_course)
        return semester if len(taken) == n else -1
                    