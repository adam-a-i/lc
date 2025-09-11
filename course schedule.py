class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        graph = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            graph[course].append(pre)

        def dfs(node):
            if node in visiting:
                return False
            if graph[node] == []:
                return True
            visiting.add(node)
            for pre in graph[node]:
                if not dfs(pre):
                    return False
            visiting.remove(node)
            graph[course] =[]
            return True
        visiting = set()

        for course in graph:
            if not dfs(course):
                return False

        return True


        
            

        
