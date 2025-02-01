# Problem: Course Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        incoming = [0]*numCourses

        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
            incoming[pair[0]] += 1
        
        dq = deque()
        for i in range(numCourses):
            if incoming[i] == 0:
                dq.append(i)
        
        while dq:
            curr = dq.popleft()

            for course in graph[curr]:
                incoming[course] -= 1
            
                if incoming[course] == 0:
                    dq.append(course)
        
        print(incoming)

        for i in range(numCourses):
            if incoming[i] != 0:
                return False
        
        return True