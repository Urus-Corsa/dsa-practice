class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj_list = defaultdict(list)
        for prereq, course in prerequisites:
            adj_list[prereq].append(course)
        
        memo = {}
        def dfs(course):
            if course in memo:
                return memo[course]
            if not adj_list[course]:
                return set()
            next_courses_set = set()
            for next_course in adj_list[course]:
                next_courses_set.add(next_course)
                next_courses_set.update(dfs(next_course))
            memo[course] = next_courses_set
            return memo[course]

        results = []
        for prereq, course in queries:
            dfs(prereq)
            if prereq in memo and course in memo[prereq]:
                results.append(True)
            else:
                results.append(False)
        return results

