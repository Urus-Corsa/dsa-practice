from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        we have n courses as specificed in numCourses, and prereqs indicate [a,b], b must be taken before a
        This means for all courses that we need to take we need to ensure all their prereqs have been already taken
        in order to take the courses. So we must take all prereqs. In order to find out what course we can take first, 
        we need to find the course that does not have a prereq to take, and once we take that we can discard it from
        being considered for the courses that it is a prereq to. Here we can apply Kahn's algo where we first calculate
        the indegrees of each course (indegree ~ num of prereqs) and then we start by course with 0 indegrees, process it,
        and decrement the indegree of those courses that had that course as prereq, and course that is now having indegree
        of zero can be taken, and now we process those. If we finished processing all, we can take all courses else we cannot
        In Kahn's algo we can utilize bfs with indegrees, to get indegrees of all courses we need an arr initialized to
        size of all courses (arr since courses are sequential ids, number ids from 0 to n-1) and we can iterate all edges
        to get indegrees.
        Then we need to add those with indegrees zero to the queue of bfs. Then we need to possibly traverse every course/vertex
        and then from there we visit every edge of every V. So time comp would be O(E) to fill indegrees and adj_list + O(V) to find indegrees zero + O(V+E)
        to perfom a bfs (O(V) since we visit each course/vertex at most once and visit their edges once here as well), this would result in total time comp of O(2V+2E) ~ O(V+E)
        Space comp, O(V) indegree arr size + O(V+E) for size of adj_list + O(V) max size of bfs queue. So total space comp is O(3V+E) ~ O(V+E)
        """
        #edge cases: 1 course and prereq to itself (cyclic), handled since indegree won't be zero and queue never populates
        #prereqs = 0, handled queue populates with all courses since all have indegrees of zero and get processed
        #dry run: 3 courses, prereqs =[[0,1],[1,2]]
        indegrees = [0 for _ in range(numCourses)] #we know that numCourses are zero indexed, in dry run it'd be [0,0,0]
        adj_list = defaultdict(list)
        for course, prereq in prerequisites: #indegrees = [1,1,0], adj_list = {0,:[], 1:[0], 2:[1]}
            indegrees[course] += 1
            adj_list[prereq].append(course)
        queue = deque()
        for course, indegree in enumerate(indegrees):  # queue = [2]
            if indegree == 0:
                queue.append(course)
        courses_taken = 0
        while queue:
            prereq = queue.popleft()  # queue = [], 2 popped -> [1], 1 popped -> [0], 0 popped
            courses_taken += 1 # 2 popped, taken = 1 -> 1 popped, taken 2 -> 0 popped, taken = 3
            for course in adj_list[prereq]: # 2 popped, course 1 indegree lowers to zero, 1 is added to queue -> 1 popped, course 0 indegrees lowers to 0 pushed to queue -> 0 not prereq to any course
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    queue.append(course)
        return courses_taken == numCourses # returns true numCourses = 3 and taken = 3