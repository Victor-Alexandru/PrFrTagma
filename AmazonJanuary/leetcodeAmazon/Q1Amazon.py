class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = {}

        for vertex in range(numCourses):
            edges[vertex] = []

        for edge in prerequisites:
            edges[edge[0]].append(edge[1])


        def has_cycle(vertex,visited,recStack):
            visited[vertex] = True
            recStack[vertex] = True
            
            for neighbour in edges[vertex]:
                if visited[neighbour] == False:
                    if has_cycle(neighbour,visited,recStack) == True:
                        return True
                elif recStack[neighbour] == True:
                    return True

            recStack[vertex] = False
            return False
        

        visited = [False] * numCourses
        recStack = [False] * numCourses
        for vertex in edges.keys():
            if visited[vertex] == False:
                if has_cycle(vertex,visited,recStack) == True:
                    return False
            

        return True


            
s = Solution()